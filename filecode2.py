# filecode2.py
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def convert_docx_to_pdf(docx_path, pdf_path):
    """
    Converts a DOCX file to a simple PDF.
    Complex formatting may not be preserved.
    """
    doc_pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    docx_doc = Document(docx_path)
    for paragraph in docx_doc.paragraphs:
        story.append(Paragraph(paragraph.text, styles['Normal']))

    doc_pdf.build(story)
