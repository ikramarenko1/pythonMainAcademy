# Генерація PDF-документу: Створіть клас PDFGenerator і класовий метод для генерації PDF-документів з заданим змістом.
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PDFGenerator:
    @classmethod
    def generate(cls, file_name, content):
        c = canvas.Canvas(file_name, pagesize=letter)

        width, height = letter
        c.drawString(100, height - 100, content)

        c.save()


PDFGenerator.generate("sample.pdf", "Try to create PDF document...")
