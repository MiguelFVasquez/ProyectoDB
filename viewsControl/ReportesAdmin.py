from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from conexion import Conexion
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class ReportesAdmin(QMainWindow):
    def __init__(self, menu):
        super().__init__()
        uic.loadUi('views/ReportesAdmin.ui', self)
        self.menu = menu
        self.db = Conexion()
        self.iniGui()
        self.cargarMunicipios()
        self.cargarSucursales()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnMoroso.clicked.connect(self.generarReporteMorosos)  # Asignar evento al botón
        self.btnReporteMunicipios.clicked.connect(self.generarReportePrestamosMunicipio)
        self.btnReporteSucursal.clicked.connect(self.generarReportePrestamosSucursal)

    def regresarAlMenu(self):
        # Cierra la ventana actual y muestra el menú principal
        self.close()
        self.menu.show()

    def cargarMunicipios(self):
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT idMunicipio, nombre FROM Municipios")
                municipios = cursor.fetchall()

                self.comboBoxMunicipios.clear()

                # Agregar el nombre del municipio al comboBox y asociar el id como "data"
                for idMunicipio, nombreMunicipio in municipios:
                    self.comboBoxMunicipios.addItem(nombreMunicipio, idMunicipio)
                cursor.close()

                self.comboBoxMunicipios.setCurrentIndex(-1)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar los municipios: {str(e)}")
                print(f"Error al cargar los municipios: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def cargarSucursales(self):
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para obtener las sucursales
                cursor.execute("SELECT idSucursal, NombreSucursal FROM Sucursales")
                sucursales = cursor.fetchall()

                # Limpiar el ComboBox antes de llenarlo
                self.comboBoxSucursal.clear()

                # Llenar el ComboBox con los nombres de las sucursales y sus ids
                for id_sucursal, nombre in sucursales:
                    self.comboBoxSucursal.addItem(nombre, id_sucursal)  # Almacenar id en el segundo parámetro
                cursor.close()

                self.comboBoxSucursal.setCurrentIndex(-1)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al cargar las sucursales: {str(e)}")
                print(f"Error al cargar las sucursales: {str(e)}")  # Asegúrate de que se imprima el error
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")

    def generarReporteMorosos(self):
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para obtener empleados con cuotas en estado moroso
                cursor.execute("""
                    SELECT 
                        e.nombre AS empleado,
                        pr.MontoPagar AS monto,
                        COUNT(c.idCuota) AS cuotas_pendientes,
                        (pr.MontoPagar / p.numeroMeses) * COUNT(c.idCuota) AS deuda
                    FROM 
                        Prestamos pr
                    JOIN 
                        SolicitudPrestamo sp ON pr.codigoSolicitud = sp.codigo
                    JOIN 
                        Empleados e ON sp.Usuario = e.idUsuario
                    JOIN 
                        Cuotas c ON pr.codigoSolicitud = c.idPrestamo
                    JOIN 
                        EstadoCuota ec ON c.idEstado = ec.idEstado
                    JOIN 
                        Periodo p ON sp.periodo = p.codigo
                    WHERE 
                        ec.estado = 'Moroso'
                    GROUP BY 
                        e.nombre, pr.MontoPagar, p.numeroMeses
                """)
                morosos = cursor.fetchall()
                cursor.close()

                if not morosos:
                    QMessageBox.information(self, "Información", "No hay empleados con cuotas en estado moroso.")
                    return

                # Crear el directorio si no existe
                ruta_directorio = 'informes/ReportesAdmin'
                os.makedirs(ruta_directorio, exist_ok=True)

                # Generar el PDF
                ruta_pdf = os.path.join(ruta_directorio, 'reporte_morosos.pdf')
                c = canvas.Canvas(ruta_pdf, pagesize=letter)
                c.setFont("Helvetica", 12)

                c.drawString(30, 750, "Reporte de Empleados con Cuotas en Estado Moroso")
                c.drawString(30, 730, "-----------------------------------------------")

                y = 710
                for empleado, monto, cuotas_pendientes, deuda in morosos:
                    c.drawString(30, y, f"Empleado: {empleado}")
                    c.drawString(200, y, f"Monto Prestado: ${monto:,.2f}")
                    c.drawString(400, y, f"Cuotas Pendientes: {cuotas_pendientes}")
                    y -= 20
                    c.drawString(30, y, f"Deuda Total: ${deuda:,.2f}")
                    c.drawString(30, y - 10, "-----------------------------------------------")
                    y -= 30

                    if y < 50:  # Crear una nueva página si el espacio es insuficiente
                        c.showPage()
                        c.setFont("Helvetica", 12)
                        y = 750

                c.save()

                QMessageBox.information(self, "Éxito", f"Reporte generado exitosamente en {ruta_pdf}")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al generar el reporte: {str(e)}")
                print(f"Error al generar el reporte: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")


    def generarReportePrestamosMunicipio(self):
        # Obtener el municipio seleccionado en el ComboBox
        municipio_index = self.comboBoxMunicipios.currentIndex()
        if municipio_index == -1:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione un municipio.")
            return

        id_municipio = self.comboBoxMunicipios.itemData(municipio_index)
        nombre_municipio = self.comboBoxMunicipios.currentText()

        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para obtener el total de préstamos por municipio
                cursor.execute("""
                    SELECT 
                        COUNT(p.codigoSolicitud) AS total_prestamos,
                        COALESCE(SUM(p.MontoPagar), 0) AS total_monto
                    FROM 
                        Prestamos p
                    JOIN 
                        SolicitudPrestamo sp ON p.codigoSolicitud = sp.codigo
                    JOIN 
                        Empleados e ON sp.Usuario = e.idUsuario
                    JOIN 
                        Sucursales s ON e.idSucursal = s.idSucursal
                    WHERE 
                        s.Municipio = ?
                """, (id_municipio,))
                resultado = cursor.fetchone()
                cursor.close()

                if not resultado or resultado[0] == 0:
                    QMessageBox.information(self, "Información", "No se encontraron préstamos para el municipio seleccionado.")
                    return

                total_prestamos, total_monto = resultado

                # Crear el directorio si no existe
                ruta_directorio = 'informes/ReportesAdmin'
                os.makedirs(ruta_directorio, exist_ok=True)

                # Generar el PDF
                ruta_pdf = os.path.join(ruta_directorio, f'reporte_prestamos_{nombre_municipio}.pdf')
                c = canvas.Canvas(ruta_pdf, pagesize=letter)
                c.setFont("Helvetica", 12)

                # Escribir encabezado
                c.drawString(30, 750, f"Reporte de Préstamos - Municipio: {nombre_municipio}")
                c.drawString(30, 730, "-----------------------------------------------")

                # Escribir datos
                c.drawString(30, 710, f"Total de Préstamos: {total_prestamos}")
                c.drawString(30, 690, f"Monto Total Prestado: ${total_monto:,.2f}")
                c.drawString(30, 670, "-----------------------------------------------")

                c.save()

                QMessageBox.information(self, "Éxito", f"Reporte generado exitosamente en {ruta_pdf}")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al generar el reporte: {str(e)}")
                print(f"Error al generar el reporte: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")


    def generarReportePrestamosSucursal(self):
        # Obtener la sucursal seleccionada en el ComboBox
        sucursal_index = self.comboBoxSucursal.currentIndex()
        if sucursal_index == -1:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una sucursal.")
            return

        id_sucursal = self.comboBoxSucursal.itemData(sucursal_index)
        nombre_sucursal = self.comboBoxSucursal.currentText()

        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Consulta para obtener el total de préstamos por sucursal
                cursor.execute("""
                    SELECT 
                        COUNT(p.codigoSolicitud) AS total_prestamos,
                        COALESCE(SUM(p.MontoPagar), 0) AS total_monto
                    FROM 
                        Prestamos p
                    JOIN 
                        SolicitudPrestamo sp ON p.codigoSolicitud = sp.codigo
                    JOIN 
                        Empleados e ON sp.Usuario = e.idUsuario
                    WHERE 
                        e.idSucursal = ?
                """, (id_sucursal,))
                resultado = cursor.fetchone()
                cursor.close()

                if not resultado or resultado[0] == 0:
                    QMessageBox.information(self, "Información", "No se encontraron préstamos para la sucursal seleccionada.")
                    return

                total_prestamos, total_monto = resultado

                # Crear el directorio si no existe
                ruta_directorio = 'informes/ReportesAdmin'
                os.makedirs(ruta_directorio, exist_ok=True)

                # Generar el PDF
                ruta_pdf = os.path.join(ruta_directorio, f'reporte_prestamos_{nombre_sucursal}.pdf')
                c = canvas.Canvas(ruta_pdf, pagesize=letter)
                c.setFont("Helvetica", 12)

                # Escribir encabezado
                c.drawString(30, 750, f"Reporte de Préstamos - Sucursal: {nombre_sucursal}")
                c.drawString(30, 730, "-----------------------------------------------")

                # Escribir datos
                c.drawString(30, 710, f"Total de Préstamos: {total_prestamos}")
                c.drawString(30, 690, f"Monto Total Prestado: ${total_monto:,.2f}")
                c.drawString(30, 670, "-----------------------------------------------")

                c.save()

                QMessageBox.information(self, "Éxito", f"Reporte generado exitosamente en {ruta_pdf}")

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al generar el reporte: {str(e)}")
                print(f"Error al generar el reporte: {str(e)}")
            finally:
                self.db.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo conectar a la base de datos")
