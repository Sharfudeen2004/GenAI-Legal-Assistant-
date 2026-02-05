from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_pdf(text):
    c = canvas.Canvas("report.pdf", pagesize=A4)
    c.drawString(50, 800, "Contract Risk Report")
    c.drawString(50, 770, text[:500])
    c.save()
