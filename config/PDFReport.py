from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class GeneradorPDF:
    def __init__(self, nombre_pdf, num_prestamo, num_cuota, fecha_pago, valor_pago, fecha_vencimiento):
        self.nombre_pdf = nombre_pdf
        self.num_prestamo = num_prestamo
        self.num_cuota = num_cuota
        self.fecha_pago = fecha_pago
        self.valor_pago = valor_pago
        self.fecha_vencimiento = fecha_vencimiento

    def generar_pdf(self):
        try:
            c = canvas.Canvas(self.nombre_pdf, pagesize=letter)
            width, height = letter

            c.setFont("Helvetica", 12)
            c.drawString(100, height - 50, f"Informe de Pago de Cuota")
            c.drawString(100, height - 100, f"Préstamo: {self.num_prestamo}")
            c.drawString(100, height - 130, f"Cuota: {self.num_cuota}")
            c.drawString(100, height - 160, f"Fecha de Pago: {self.fecha_pago}")
            c.drawString(100, height - 190, f"Valor Pagado: {self.valor_pago}")
            c.drawString(100, height - 220, f"Fecha de Vencimiento: {self.fecha_vencimiento}")

            # Guardar el archivo PDF
            c.save()
            print(f"PDF generado con éxito: {self.nombre_pdf}")
        except Exception as e:
            print(f"Error al generar el PDF: {e}")
