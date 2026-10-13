#!/usr/bin/env python3
"""
office_segments.py - lossless text extraction / re-injection for DOCX, PPTX and XLSX.

Edits the Office XML directly (in a COPY of the file), so styles, layout, images, charts,
numbering, headers/footers and footnotes survive. Inline formatting inside a paragraph is
exposed as tags so the translator can move it with the words:

    <g1>plain or formatted text run(s)</g1>   formatting group  (keep pair, translate inside)
    <c2>hyperlink / field text</c2>          container         (keep pair, translate inside)
    <x3/>                                    object: image, tab, break, field code, note mark
                                             (keep exactly, never translate)

A paragraph with a single formatting group and nothing else is exported as plain text.

Usage
  python3 office_segments.py extract INPUT -o segments.json
  python3 office_segments.py apply INPUT translations.json -o OUTPUT [--lang ar] [--rtl-sheets]

translations.json is {"<segment id>": "<translated text>"}; it may also be a segments file
whose "text" values were replaced by translations ({"segments":[{"id":..,"text":..}]}).
Segments missing from translations.json keep their original text (reported).

Requires: lxml  (pip install lxml)
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
import zipfile

try:
    from lxml import etree
except ImportError:  # pragma: no cover
    sys.exit("office_segments.py needs lxml:  pip install lxml")

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
S = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"


def q(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


# --------------------------------------------------------------------------- format profiles
class Profile:
    def __init__(self, ns, parts, para, run, text, props, rpr, heavy, markers_lead=(),
                 markers_tail=(), drop=(), ignorable_in_run=(), placeholder_children=()):
        self.ns = ns
        self.parts = [re.compile(p) for p in parts]
        self.para = para
        self.run = run
        self.text = text
        self.props = set(props)            # paragraph-level property elements kept in place
        self.rpr = rpr                     # run properties tag
        self.heavy = set(heavy)            # descendants that make a whole child an object
        self.markers_lead = set(markers_lead)
        self.markers_tail = set(markers_tail)
        self.drop = set(drop)
        self.ignorable_in_run = set(ignorable_in_run)
        self.placeholder_children = set(placeholder_children)  # whole child = object


DOCX = Profile(
    ns=W,
    parts=[r"^word/document\.xml$", r"^word/header\d*\.xml$", r"^word/footer\d*\.xml$",
           r"^word/footnotes\.xml$", r"^word/endnotes\.xml$", r"^word/comments\.xml$",
           r"^word/charts/chart\d+\.xml$"],
    para=q(W, "p"), run=q(W, "r"), text=q(W, "t"),
    props=[q(W, "pPr")], rpr=q(W, "rPr"),
    heavy=[q(W, "p"), q(W, "drawing"), q(W, "pict"), q(W, "object"), q(W, "fldChar"),
           q(W, "instrText"), q(W, "footnoteReference"), q(W, "endnoteReference"),
           q(W, "commentReference"), q(W, "delText"), q(W, "sym"), q(W, "ruby"),
           "{http://schemas.openxmlformats.org/markup-compatibility/2006}AlternateContent",
           "{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath"],
    markers_lead=[q(W, "bookmarkStart"), q(W, "commentRangeStart"), q(W, "permStart"),
                  q(W, "moveFromRangeStart"), q(W, "moveToRangeStart")],
    markers_tail=[q(W, "bookmarkEnd"), q(W, "commentRangeEnd"), q(W, "permEnd"),
                  q(W, "moveFromRangeEnd"), q(W, "moveToRangeEnd")],
    drop=[q(W, "proofErr")],
    ignorable_in_run=[q(W, "lastRenderedPageBreak")],
    placeholder_children=[q(W, "del"), q(W, "moveFrom"),
                          "{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath",
                          "{http://schemas.openxmlformats.org/officeDocument/2006/math}oMathPara"],
)

PPTX = Profile(
    ns=A,
    parts=[r"^ppt/slides/slide\d+\.xml$", r"^ppt/notesSlides/notesSlide\d+\.xml$",
           r"^ppt/charts/chart\d+\.xml$", r"^ppt/diagrams/data\d+\.xml$",
           r"^ppt/diagrams/drawing\d+\.xml$"],
    para=q(A, "p"), run=q(A, "r"), text=q(A, "t"),
    props=[q(A, "pPr"), q(A, "endParaRPr")], rpr=q(A, "rPr"),
    heavy=[q(A, "p")],
    placeholder_children=[q(A, "br"), q(A, "fld"),
                          "{http://schemas.openxmlformats.org/markup-compatibility/2006}AlternateContent",
                          "{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath"],
)

XLSX = Profile(
    ns=S,
    parts=[r"^xl/sharedStrings\.xml$", r"^xl/worksheets/sheet\d+\.xml$",
           r"^xl/charts/chart\d+\.xml$"],
    para=q(S, "si"), run=q(S, "r"), text=q(S, "t"),
    props=[q(S, "rPh"), q(S, "phoneticPr")], rpr=q(S, "rPr"),
    heavy=[],
)
XLSX_INLINE = q(S, "is")  # inline strings in worksheets behave like <si>

PROFILES = {"docx": DOCX, "docm": DOCX, "dotx": DOCX,
            "pptx": PPTX, "pptm": PPTX, "potx": PPTX,
            "xlsx": XLSX, "xlsm": XLSX, "xltx": XLSX}

# Charts inside DOCX/XLSX use DrawingML paragraphs (a:p) for titles/labels.
CHART_PART = re.compile(r"/charts/chart\d+\.xml$")

TAG_RE = re.compile(r"<([gc])(\d+)>(.*?)</\1\2>|<x(\d+)/>", re.S)
LETTER_RE = re.compile(r"[^\W\d_]", re.U)


# --------------------------------------------------------------------------- language data
LANG_DEFAULTS = {
    "ar": "ar-SA", "en": "en-US", "en-us": "en-US", "en-gb": "en-GB",
    "zh": "zh-CN", "zh-cn": "zh-CN", "zh-tw": "zh-TW", "zh-hk": "zh-HK",
    "es": "es-MX", "es-419": "es-MX", "es-es": "es-ES", "es-mx": "es-MX",
    "hi": "hi-IN", "fr": "fr-FR", "fr-fr": "fr-FR", "fr-ca": "fr-CA",
    "pt": "pt-BR", "pt-br": "pt-BR", "pt-pt": "pt-PT", "ru": "ru-RU",
    "bn": "bn-BD", "bn-bd": "bn-BD", "bn-in": "bn-IN", "ur": "ur-PK", "ur-pk": "ur-PK",
    "ur-in": "ur-IN", "id": "id-ID", "de": "de-DE", "de-de": "de-DE", "de-ch": "de-CH",
    "de-at": "de-AT", "ja": "ja-JP", "tr": "tr-TR", "ko": "ko-KR",
}
RTL = {"ar", "ur", "fa", "he", "ps", "sd", "ug", "yi"}
EAST_ASIAN = {"zh", "ja", "ko"}
COMPLEX = RTL | {"hi", "bn", "ta", "te", "mr", "gu", "pa", "kn", "ml", "th", "ne", "si"}


def lang_info(lang: str | None):
    if not lang:
        return None
    key = lang.lower().lstrip("-")
    bcp = LANG_DEFAULTS.get(key, lang)
    base = bcp.split("-")[0].lower()
    return {"bcp": bcp, "base": base, "rtl": base in RTL,
            "east_asian": base in EAST_ASIAN, "complex": base in COMPLEX}


# --------------------------------------------------------------------------- helpers
def detect_kind(path: str) -> str:
    ext = path.rsplit(".", 1)[-1].lower()
    if ext not in PROFILES:
        sys.exit(f"Unsupported file type .{ext} (supported: {', '.join(sorted(PROFILES))}). "
                 "Convert legacy .doc/.ppt/.xls with LibreOffice first.")
    return ext


def profile_for(kind: str, part: str) -> Profile:
    if CHART_PART.search(part) and kind not in ("pptx", "pptm", "potx"):
        return PPTX  # DrawingML text inside charts
    return PROFILES[kind]


def text_of(el, prof: Profile) -> str:
    """Text of t-elements belonging to this element (not to nested paragraphs)."""
    out = []
    for t in el.iter(prof.text):
        anc = t.getparent()
        nested = False
        while anc is not None and anc is not el:
            if anc.tag == prof.para or anc.tag == XLSX_INLINE:
                nested = True
                break
            anc = anc.getparent()
        if not nested:
            out.append(t.text or "")
    return "".join(out)


def has_heavy(el, prof: Profile) -> bool:
    for d in el.iterdescendants():
        if d.tag in prof.heavy:
            return True
    return False


def sig(run, prof: Profile) -> str:
    rpr = run.find(prof.rpr)
    return "" if rpr is None else etree.tostring(rpr, method="c14n").decode()


def paragraphs(root, prof: Profile, part: str):
    tags = {prof.para}
    if prof is XLSX:
        tags.add(XLSX_INLINE)
    return [el for el in root.iter() if el.tag in tags]


# --------------------------------------------------------------------------- analysis
class Piece:
    __slots__ = ("kind", "el", "run", "text", "sig")

    def __init__(self, kind, el=None, run=None, text="", sig_=""):
        self.kind, self.el, self.run, self.text, self.sig = kind, el, run, text, sig_


def analyse(p, prof: Profile):
    """Split a paragraph into pieces: text / container / object (+ markers)."""
    pieces, lead, tail = [], [], []
    content_children = []
    for child in list(p):
        if not isinstance(child.tag, str):          # comments / processing instructions
            continue
        if child.tag in prof.props:
            continue
        content_children.append(child)
        if child.tag in prof.drop:
            continue
        if child.tag in prof.markers_lead:
            lead.append(child)
            continue
        if child.tag in prof.markers_tail:
            tail.append(child)
            continue
        if child.tag == prof.text:                    # xlsx <si><t>…</t></si>
            pieces.append(Piece("text", el=child, run=child, text=child.text or "", sig_="__t__"))
            continue
        if child.tag in prof.placeholder_children:
            pieces.append(Piece("object", el=child))
            continue
        if child.tag == prof.run:
            if has_heavy(child, prof):
                pieces.append(Piece("object", el=child))
                continue
            s = sig(child, prof)
            for rc in child:
                if not isinstance(rc.tag, str) or rc.tag == prof.rpr:
                    continue
                if rc.tag == prof.text:
                    pieces.append(Piece("text", el=rc, run=child, text=rc.text or "", sig_=s))
                elif rc.tag in prof.ignorable_in_run:
                    continue
                else:
                    pieces.append(Piece("runobj", el=rc, run=child))
            continue
        # anything else (hyperlink, smartTag, ins, sdt, fldSimple …)
        if not has_heavy(child, prof) and text_of(child, prof).strip():
            pieces.append(Piece("container", el=child, text=text_of(child, prof)))
        else:
            pieces.append(Piece("object", el=child))
    return pieces, lead, tail, content_children


def build_segment(pieces):
    """Return (segment_text, tagmap) where tagmap maps tag names to pieces."""
    tokens = []           # (type, id, text)
    tagmap = {}
    g = c = x = 0
    last_sig = None
    for pc in pieces:
        if pc.kind == "text":
            if tokens and tokens[-1][0] == "g" and last_sig == pc.sig:
                t = tokens[-1]
                tokens[-1] = ("g", t[1], t[2] + pc.text)
            else:
                g += 1
                tokens.append(("g", g, pc.text))
                tagmap[f"g{g}"] = pc
                last_sig = pc.sig
            continue
        last_sig = None
        if pc.kind == "container":
            c += 1
            tokens.append(("c", c, pc.text))
            tagmap[f"c{c}"] = pc
        else:
            x += 1
            tokens.append(("x", x, ""))
            tagmap[f"x{x}"] = pc
    if len(tokens) == 1 and tokens[0][0] == "g":
        return tokens[0][2], tagmap, False
    out = []
    for typ, n, txt in tokens:
        out.append(f"<x{n}/>" if typ == "x" else f"<{typ}{n}>{txt}</{typ}{n}>")
    return "".join(out), tagmap, True


def iter_parts(zf: zipfile.ZipFile, kind: str):
    for name in zf.namelist():
        if any(rx.search(name) for rx in PROFILES[kind].parts):
            yield name, profile_for(kind, name)


def walk(zf, kind):
    """Yield (part, root, [(seg_id, p, prof, pieces, lead, tail, content, text, tagmap, tagged)])."""
    for part, prof in iter_parts(zf, kind):
        root = etree.fromstring(zf.read(part))
        items = []
        for i, p in enumerate(paragraphs(root, prof, part)):
            pieces, lead, tail, content = analyse(p, prof)
            text, tagmap, tagged = build_segment(pieces)
            plain = "".join(pc.text for pc in pieces if pc.kind in ("text", "container"))
            if not LETTER_RE.search(plain):
                continue
            items.append((f"{part}#{i}", p, prof, pieces, lead, tail, content, text, tagmap, tagged))
        yield part, root, prof, items


def stats(zf, kind):
    st = {"tables": 0, "images": 0, "charts": 0}
    for name in zf.namelist():
        if name.startswith(("word/media/", "ppt/media/", "xl/media/")):
            st["images"] += 1
        if re.search(r"/charts/chart\d+\.xml$", name):
            st["charts"] += 1
        if name in ("word/document.xml",) or re.match(r"ppt/slides/slide\d+\.xml$", name):
            root = etree.fromstring(zf.read(name))
            st["tables"] += len(root.findall(f".//{q(W, 'tbl')}")) + len(root.findall(f".//{q(A, 'tbl')}"))
    return st


# --------------------------------------------------------------------------- extract
def cmd_extract(args):
    kind = detect_kind(args.input)
    segs = []
    with zipfile.ZipFile(args.input) as zf:
        for part, _root, _prof, items in walk(zf, kind):
            for seg_id, *_rest, text, _tagmap, tagged in items:
                segs.append({"id": seg_id, "text": text, "tagged": tagged})
        st = stats(zf, kind)
    st["segments"] = len(segs)
    st["tagged_segments"] = sum(s["tagged"] for s in segs)
    st["words_approx"] = sum(len(re.sub(r"<[^>]+>", " ", s["text"]).split()) for s in segs)
    data = {"source": args.input, "format": kind, "stats": st, "segments": segs}
    out = args.output or args.input.rsplit(".", 1)[0] + ".segments.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f"[extract] {len(segs)} segments → {out}")
    print(f"[extract] stats: {json.dumps(st, ensure_ascii=False)}")
    print("[extract] translate the 'text' values; keep every <gN>…</gN>, <cN>…</cN>, <xN/> tag.")


# --------------------------------------------------------------------------- apply helpers
def set_text(t_el, text):
    t_el.text = text
    if t_el.tag in (q(W, "t"), q(S, "t")):      # DrawingML <a:t> keeps spaces natively
        t_el.set(XML_SPACE, "preserve")


def make_text_run(pc: Piece, text: str, prof: Profile):
    if pc.run is pc.el:            # xlsx bare <t>
        t = copy.deepcopy(pc.el)
        set_text(t, text)
        return t
    run = copy.deepcopy(pc.run)
    for ch in list(run):
        if ch.tag != prof.rpr:
            run.remove(ch)
    t = etree.SubElement(run, prof.text)
    set_text(t, text)
    return run


def make_runobj(pc: Piece, prof: Profile):
    run = copy.deepcopy(pc.run)
    for ch in list(run):
        if ch.tag != prof.rpr:
            run.remove(ch)
    run.append(copy.deepcopy(pc.el))
    return run


def fill_container(pc: Piece, text: str, prof: Profile):
    el = pc.el
    ts = [t for t in el.iter(prof.text)]
    if ts:
        set_text(ts[0], text)
        for t in ts[1:]:
            t.text = ""
    return el


def parse_translation(s: str):
    toks, pos = [], 0
    for m in TAG_RE.finditer(s):
        if m.start() > pos:
            toks.append(("plain", None, s[pos:m.start()]))
        if m.group(4):
            toks.append(("x", int(m.group(4)), ""))
        else:
            toks.append((m.group(1), int(m.group(2)), m.group(3)))
        pos = m.end()
    if pos < len(s):
        toks.append(("plain", None, s[pos:]))
    return toks


def rebuild(seg_id, p, prof, pieces, lead, tail, content, tagmap, tagged, translation, issues):
    first_text = next((pc for pc in pieces if pc.kind == "text"), None)
    toks = parse_translation(translation) if tagged else [("g", 1, translation)]
    if not tagged and "g1" not in tagmap:
        issues.append(("MAJOR", seg_id, "no text run to carry translation"))
        return
    new = list(lead)
    used = set()
    for typ, n, txt in toks:
        if typ == "plain":
            if not txt:
                continue
            tpl = tagmap.get("g1") or first_text
            if tpl is None:
                tpl_run = etree.Element(prof.run)
                t = etree.SubElement(tpl_run, prof.text)
                set_text(t, txt)
                new.append(tpl_run)
            else:
                new.append(make_text_run(tpl, txt, prof))
            continue
        key = f"{typ}{n}"
        pc = tagmap.get(key)
        if pc is None:
            issues.append(("MAJOR", seg_id, f"unknown tag <{key}> in translation — text kept untagged"))
            tpl = tagmap.get("g1") or first_text
            if tpl is not None and txt:
                new.append(make_text_run(tpl, txt, prof))
            continue
        if typ == "g":
            new.append(make_text_run(pc, txt, prof))
        elif typ == "c":
            if key in used:
                issues.append(("MAJOR", seg_id, f"container <{key}> used twice — second copy dropped"))
                continue
            new.append(fill_container(pc, txt, prof))
        else:  # object
            if key in used:
                issues.append(("MAJOR", seg_id, f"object <{key}/> duplicated — extra copy dropped"))
                continue
            # move the original object (not a copy) so nested text boxes keep their edits
            new.append(pc.el if pc.kind == "object" else make_runobj(pc, prof))
        used.add(key)
    for key, pc in tagmap.items():
        if key[0] in "cx" and key not in used:
            sev = "CRITICAL" if key[0] == "x" else "MAJOR"
            issues.append((sev, seg_id, f"tag <{key}> missing in translation — original re-appended at end"))
            if key[0] == "x":
                new.append(pc.el if pc.kind == "object" else make_runobj(pc, prof))
            else:
                new.append(pc.el)
    new.extend(tail)

    # replace content children, keeping property elements where they are
    children = list(p)
    idx = children.index(content[0])   # props (pPr) stay before, endParaRPr/rPh stay after
    for ch in content:
        p.remove(ch)
    for k, el in enumerate(new):
        p.insert(idx + k, el)


# --------------------------------------------------------------------------- language / RTL
RPR_ORDER = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike", "dstrike",
             "outline", "shadow", "emboss", "imprint", "noProof", "snapToGrid", "vanish",
             "webHidden", "color", "spacing", "w", "kern", "position", "sz", "szCs", "highlight",
             "u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang",
             "eastAsianLayout", "specVanish", "oMath"]
PPR_ORDER = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl",
             "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens", "kinsoku",
             "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi",
             "adjustRightInd", "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents",
             "suppressOverlap", "jc", "textDirection", "textAlignment", "textboxTightWrap",
             "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr", "pPrChange"]
TBLPR_ORDER = ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize",
               "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders", "shd",
               "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription"]


def ensure_child(parent, local, order, ns=W):
    tag = q(ns, local)
    el = parent.find(tag)
    if el is not None:
        return el
    el = etree.Element(tag)
    pos = order.index(local)
    insert_at = len(parent)
    for i, ch in enumerate(parent):
        if isinstance(ch.tag, str) and ch.tag.startswith("{" + ns + "}"):
            name = etree.QName(ch).localname
            if name in order and order.index(name) > pos:
                insert_at = i
                break
    parent.insert(insert_at, el)
    return el


def ensure_first(parent, tag):
    el = parent.find(tag)
    if el is None:
        el = etree.Element(tag)
        parent.insert(0, el)
    return el


def docx_rpr_lang(rpr, li):
    lang = ensure_child(rpr, "lang", RPR_ORDER)
    attr = "bidi" if li["complex"] else ("eastAsia" if li["east_asian"] else "val")
    lang.set(q(W, attr), li["bcp"])
    if li["complex"]:
        # complex-script runs use the *Cs formatting slots: mirror bold/italic/size
        for a, b in (("b", "bCs"), ("i", "iCs")):
            src = rpr.find(q(W, a))
            if src is not None and rpr.find(q(W, b)) is None:
                el = ensure_child(rpr, b, RPR_ORDER)
                for k, v in src.attrib.items():
                    el.set(k, v)
        sz = rpr.find(q(W, "sz"))
        if sz is not None and rpr.find(q(W, "szCs")) is None:
            ensure_child(rpr, "szCs", RPR_ORDER).set(q(W, "val"), sz.get(q(W, "val")))


RTL_CHARS = re.compile("[\u0590-\u08FF\uFB1D-\uFDFF\uFE70-\uFEFF]")


def apply_lang_docx(root, li, translated_paras):
    if li["rtl"]:  # whole part becomes RTL, incl. image-only / empty paragraphs
        for p in root.iter(q(W, "p")):
            ppr = ensure_first(p, q(W, "pPr"))
            ensure_child(ppr, "bidi", PPR_ORDER)
    for p in translated_paras:
        for r in p.iter(q(W, "r")):
            if r.find(q(W, "t")) is None:
                continue
            rpr = r.find(q(W, "rPr"))
            if rpr is None:
                rpr = etree.Element(q(W, "rPr"))
                r.insert(0, rpr)
            docx_rpr_lang(rpr, li)
            # mark a run as RTL only when it really contains RTL letters (like Word does)
            if li["rtl"] and RTL_CHARS.search("".join(t.text or "" for t in r.iter(q(W, "t")))):
                ensure_child(rpr, "rtl", RPR_ORDER)
    if li["rtl"]:
        for tbl in root.iter(q(W, "tbl")):
            tblpr = ensure_first(tbl, q(W, "tblPr"))
            ensure_child(tblpr, "bidiVisual", TBLPR_ORDER)


def apply_lang_drawingml(li, translated_paras):
    for p in translated_paras:
        if li["rtl"]:
            ppr = ensure_first(p, q(A, "pPr"))
            ppr.set("rtl", "1")
            if ppr.get("algn") in (None, "l"):
                ppr.set("algn", "r")
        for r in p.iter(q(A, "r")):
            rpr = r.find(q(A, "rPr"))
            if rpr is None:
                rpr = etree.Element(q(A, "rPr"))
                r.insert(0, rpr)
            rpr.set("lang", li["bcp"])
        epr = p.find(q(A, "endParaRPr"))
        if epr is not None:
            epr.set("lang", li["bcp"])


def apply_lang_styles(xml_bytes, li):
    root = etree.fromstring(xml_bytes)
    dd = root.find(q(W, "docDefaults"))
    if dd is None:
        return xml_bytes
    rprd = dd.find(q(W, "rPrDefault"))
    if rprd is None:
        rprd = etree.Element(q(W, "rPrDefault"))
        dd.insert(0, rprd)
    rpr = rprd.find(q(W, "rPr"))
    if rpr is None:
        rpr = etree.SubElement(rprd, q(W, "rPr"))
    lang = ensure_child(rpr, "lang", RPR_ORDER)
    attr = "bidi" if li["complex"] else ("eastAsia" if li["east_asian"] else "val")
    lang.set(q(W, attr), li["bcp"])
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def rtl_sheet(xml_bytes):
    root = etree.fromstring(xml_bytes)
    for sv in root.iter(q(S, "sheetView")):
        sv.set("rightToLeft", "1")
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


# --------------------------------------------------------------------------- apply
def load_translations(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict) and "segments" in data:
        return {s["id"]: s["text"] for s in data["segments"]}
    if isinstance(data, list):
        return {s["id"]: s["text"] for s in data}
    return data


def cmd_apply(args):
    kind = detect_kind(args.input)
    if args.output is None:
        sys.exit("apply needs -o OUTPUT (the input file is never overwritten)")
    if args.output == args.input:
        sys.exit("Refusing to overwrite the input file. Choose another -o path.")
    tr = load_translations(args.translations)
    li = lang_info(args.lang)
    issues, done, missing = [], 0, []
    new_parts = {}
    with zipfile.ZipFile(args.input) as zf:
        seen = set()
        for part, root, prof, items in walk(zf, kind):
            translated = []
            for seg_id, p, prof_, pieces, lead, tail, content, text, tagmap, tagged in items:
                seen.add(seg_id)
                if seg_id not in tr:
                    missing.append(seg_id)
                    continue
                rebuild(seg_id, p, prof_, pieces, lead, tail, content, tagmap, tagged,
                        tr[seg_id], issues)
                translated.append(p)
                done += 1
            if li and translated:
                if prof is DOCX:
                    apply_lang_docx(root, li, translated)
                elif prof is PPTX:
                    apply_lang_drawingml(li, translated)
            if translated:
                new_parts[part] = etree.tostring(root, xml_declaration=True, encoding="UTF-8",
                                                 standalone=True)
        extra = sorted(set(tr) - seen)
        if li and kind in ("docx", "docm", "dotx") and "word/styles.xml" in zf.namelist():
            new_parts["word/styles.xml"] = apply_lang_styles(zf.read("word/styles.xml"), li)
        if args.rtl_sheets and kind in ("xlsx", "xlsm", "xltx"):
            for name in zf.namelist():
                if re.match(r"xl/worksheets/sheet\d+\.xml$", name):
                    new_parts[name] = rtl_sheet(new_parts.get(name, zf.read(name)))
        with zipfile.ZipFile(args.output, "w") as out:
            for info in zf.infolist():
                data = new_parts.get(info.filename)
                if data is None:
                    out.writestr(info, zf.read(info.filename))  # byte-identical (images etc.)
                else:
                    ni = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                    ni.compress_type = zipfile.ZIP_DEFLATED
                    ni.external_attr = info.external_attr
                    out.writestr(ni, data)
    # verify the output parses
    with zipfile.ZipFile(args.output) as zf:
        for name in new_parts:
            etree.fromstring(zf.read(name))
    print(f"[apply] {done} segments written → {args.output}")
    if missing:
        print(f"[apply] MAJOR: {len(missing)} segments had no translation and keep source text, e.g. {missing[:5]}")
    if extra:
        print(f"[apply] MINOR: {len(extra)} translation ids do not exist in the file, e.g. {extra[:5]}")
    for sev, sid, msg in issues:
        print(f"[apply] {sev}: {sid}: {msg}")
    crit = sum(1 for s in issues if s[0] == "CRITICAL")
    if li:
        print(f"[apply] language set to {li['bcp']} (rtl={li['rtl']})")
    return 2 if crit else (1 if missing or issues else 0)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract", help="extract translatable segments to JSON")
    e.add_argument("input")
    e.add_argument("-o", "--output")
    a = sub.add_parser("apply", help="write translations into a copy of the file")
    a.add_argument("input")
    a.add_argument("translations")
    a.add_argument("-o", "--output", required=True)
    a.add_argument("--lang", help="target language tag, e.g. ar, pt-br, zh-tw (sets language + RTL)")
    a.add_argument("--rtl-sheets", action="store_true", help="XLSX: display sheets right-to-left")
    args = ap.parse_args(argv)
    if args.cmd == "extract":
        cmd_extract(args)
        return 0
    return cmd_apply(args)


if __name__ == "__main__":
    sys.exit(main())
