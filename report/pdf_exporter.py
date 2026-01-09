from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_pdf(report_text: str, filename="research_report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    x_margin = 40
    y_margin = height - 40

    text = c.beginText(x_margin, y_margin)
    text.setFont("Helvetica", 10)

    for line in report_text.split("\n"):
        text.textLine(line)
        if text.getY() < 40:
            c.drawText(text)
            c.showPage()
            text = c.beginText(x_margin, height - 40)

    c.drawText(text)
    c.save()

    return filename
