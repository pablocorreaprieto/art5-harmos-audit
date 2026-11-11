"""Reference Word file for pandoc: pandoc's default styles plus a centred page number in the footer, as the
journal's guidelines ask ("Use the automatic page numbering function to number the pages").

python manuscript/make_reference_docx.py      writes manuscript/reference.docx

Written by the main session (claude-opus-5-5) on 2.11.2026, at the pre-submission audit.
"""
import os
import subprocess

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "reference.docx")


def page_field(paragraph):
    run = paragraph.add_run()
    for kind, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if kind:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        run._r.append(el)


def main():
    data = subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                          check=True, capture_output=True).stdout
    open(OUT, "wb").write(data)
    doc = Document(OUT)
    for section in doc.sections:
        footer = section.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        page_field(p)
    doc.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
