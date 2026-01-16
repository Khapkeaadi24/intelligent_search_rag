from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def export_pdf(report_text):
    file_path = "verisearch_report.pdf"
    doc = SimpleDocTemplate(file_path, pagesize=A4)

    styles = getSampleStyleSheet()
    story = []

    for line in report_text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)
    return file_path
