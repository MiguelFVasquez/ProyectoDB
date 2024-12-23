import smtplib
import os
from datetime import datetime
from email.message import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from conexion import Conexion
from config.EmailService import EmailService

class InformeCuotas(QMainWindow):
    def __init__(self, menuUsuarios, id_usuario):
        super().__init__()
        uic.loadUi("views/InformeCuotas.ui", self)
        self.menuUsuarios = menuUsuarios
        self.db = Conexion()
        self.id_usuario = id_usuario  # ID del usuario que inicia sesión
        self.iniGui()

    def iniGui(self):
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnCrearPagoCuota.clicked.connect(self.registrarPago)

        # Cargar los préstamos en el comboBox
        self.cargarPrestamos()
        self.txtPagoCuota.setEnabled(False)

        # Autocompletar `txtFechaPago` con la fecha actual y deshabilitar el campo
        fecha_actual = QDate.currentDate().toString("dd-MM-yyyy")
        self.txtFechaPago.setText(fecha_actual)
        self.txtFechaPago.setEnabled(False)  # Deshabilitar el campo para evitar ediciones

        # Conectar el cambio de selección del préstamo para actualizar el valor
        self.comboBoxPrestamos.currentIndexChanged.connect(self.actualizarValorPrestamo)
        self.txtValorPago.setEnabled(False)

    def cargarPrestamos(self):
        """Carga los préstamos del usuario en el comboBox, mostrando el codigoSolicitud en lugar del numeroPrestamo."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            # Consulta para obtener el código de solicitud y el valor del préstamo
            cursor.execute("""
                SELECT sp.codigo, p.ValorPorMes 
                FROM Prestamos p
                INNER JOIN SolicitudPrestamo sp ON p.codigoSolicitud = sp.codigo
                WHERE sp.Usuario = ?
            """, (self.id_usuario,))

            prestamos = cursor.fetchall()

            # Limpiar comboBox y añadir los préstamos con el código de solicitud
            self.comboBoxPrestamos.clear()
            for prestamo in prestamos:
                codigo_solicitud, monto = prestamo
                self.comboBoxPrestamos.addItem(f"No.Prestamo {codigo_solicitud}", monto)

            self.comboBoxPrestamos.setCurrentIndex(-1)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudieron cargar los préstamos: {e}")
        finally:
            self.db.close()
    
    def obtenerSiguienteCuota(self, id_prestamo):
        """Obtiene el número de la siguiente cuota para el préstamo seleccionado."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            # Consulta para contar las cuotas pagadas del préstamo seleccionado
            cursor.execute("""
                SELECT COUNT(*) FROM Cuotas WHERE idPrestamo = ?
            """, (id_prestamo,))
            
            # Devuelve el siguiente número de cuota
            num_cuotas_pagas = cursor.fetchone()[0]
            return num_cuotas_pagas + 1  # La siguiente cuota será el número actual + 1
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al obtener el número de la siguiente cuota: {e}")
            return 1  # Por defecto, devuelve 1 si hay un error
        finally:
            self.db.close()

    def actualizarValorPrestamo(self):
        """Actualiza el valor del préstamo seleccionado en el campo de valor."""
        monto = self.comboBoxPrestamos.currentData()  # Obtener el monto del préstamo seleccionado
        if monto:
            self.txtValorPago.setText(str(monto))

        # Obtener el id del préstamo seleccionado
        texto_prestamo = self.comboBoxPrestamos.currentText()
        id_prestamo = texto_prestamo.split()[1]  # Ahora no hay "#", solo el número

        # Validar que el id_prestamo sea un número entero
        if not id_prestamo.isdigit():
            QMessageBox.warning(self, "Error", "El ID del préstamo no es válido.")
            return

        # Obtener y asignar el número de la siguiente cuota
        siguiente_cuota = self.obtenerSiguienteCuota(int(id_prestamo))  # Convierte a entero
        self.txtPagoCuota.setText(str(siguiente_cuota))

    def regresarAlMenu(self):
        # Cierra la ventana actual y muestra el menú principal
        self.close()
        self.menuUsuarios.show()

    def registrarPago(self):
            """Registra el pago de una cuota y actualiza la fecha de la próxima cuota."""
            try:
                # Obtener los datos del formulario
                prestamo_texto = self.comboBoxPrestamos.currentText()
                if not prestamo_texto:
                    QMessageBox.warning(self, "Error", "Debe seleccionar un préstamo.")
                    return
                
                num_prestamo = prestamo_texto.split()[1].strip()
                num_cuota = self.txtPagoCuota.text()
                fecha_pago = self.txtFechaPago.text()  # Fecha ya precargada
                valor_pago = self.txtValorPago.text()

                # Validar que los campos no estén vacíos
                if not num_prestamo or not num_cuota or not valor_pago:
                    QMessageBox.warning(self, "Error", "Todos los campos deben ser completados.")
                    return

                # Validar el formato numérico de la cuota y el valor a pagar
                try:
                    num_cuota = int(num_cuota)
                    valor_pago = float(valor_pago)
                    if valor_pago <= 0:
                        QMessageBox.warning(self, "Error", "El valor a pagar debe ser mayor que cero.")
                        return
                except ValueError:
                    QMessageBox.warning(self, "Error", "El valor de la cuota o el pago no es válido.")
                    return

                # Registrar la cuota pagada en la base de datos
                conn = self.db.connect()
                cursor = conn.cursor()

                # Calcular la fecha de vencimiento (día 10 del siguiente mes)
                fecha_pago_obj = QDate.fromString(fecha_pago, "dd-MM-yyyy")
                siguiente_mes = fecha_pago_obj.addMonths(1)  # Agregar un mes
                fecha_vencimiento = QDate(siguiente_mes.year(), siguiente_mes.month(), 10)

                # Insertar un registro en la tabla de Cuotas
                cursor.execute("""
                    INSERT INTO Cuotas (idPrestamo, numCuota, fechaVencimiento, valorPagado, fechaDePago, idEstado)
                    VALUES (?, ?, ?, ?, ?, (SELECT idEstado FROM EstadoCuota WHERE estado = 'Pagado'))
                """, (int(num_prestamo), num_cuota, fecha_vencimiento.toString("yyyy-MM-dd"), valor_pago, fecha_pago_obj.toString("yyyy-MM-dd")))

                conn.commit()

                # Generar el PDF del informe
                pdf_file_path = self.generarPDF(num_prestamo, num_cuota, valor_pago, fecha_pago_obj, fecha_vencimiento)

                # Enviar el correo con el PDF adjunto
                self.enviarCorreoConPDF(pdf_file_path)

                # Actualizar el campo para mostrar la nueva fecha de vencimiento
                self.txtPagoCuota.setText(str(num_cuota + 1))
                self.txtFechaPago.setText(fecha_vencimiento.toString("dd-MM-yyyy"))

                QMessageBox.information(self, "Éxito", "Pago registrado y correo enviado exitosamente.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Error al registrar el pago: {e}")
            finally:
                self.db.close()


    def generarPDF(self, num_prestamo, num_cuota, valor_pago, fecha_pago_obj, fecha_vencimiento):
        """Genera un PDF con la información del pago y lo guarda en el disco."""
        pdf_file_path = f"informes/pago_prestamo_{num_prestamo}_cuota_{num_cuota}.pdf"
        c = canvas.Canvas(pdf_file_path, pagesize=letter)
        c.drawString(100, 750, f"Informe de Pago de Cuota - Préstamo #{num_prestamo}")
        c.drawString(100, 730, f"Número de Cuota: {num_cuota}")
        c.drawString(100, 710, f"Valor Pagado: ${valor_pago}")
        c.drawString(100, 690, f"Fecha de Pago: {fecha_pago_obj.toString('dd-MM-yyyy')}")
        c.drawString(100, 670, f"Fecha de Vencimiento: {fecha_vencimiento.toString('dd-MM-yyyy')}")
        c.save()

        return pdf_file_path

    def enviarCorreoConPDF(self, pdf_file_path):
        """Envía un correo con el archivo PDF adjunto."""
        try:
            # Obtener el correo del usuario (suponiendo que lo tienes almacenado en la base de datos)
            email_usuario = self.obtenerEmailUsuario()

            # Configurar el asunto y mensaje
            asunto = "Informe de Pago de Cuota"
            mensaje = f"Estimado usuario, adjuntamos el informe del pago de la cuota de su préstamo."

            # Enviar el correo con el archivo adjunto
            EmailService.emailMessages(
                asunto=asunto,
                email=email_usuario,
                nombre="Usuario",  # Puedes reemplazar con el nombre real del usuario
                mensaje=mensaje,
                archivo_adjunto=pdf_file_path
            )

            # Eliminar el archivo PDF después de enviarlo (si lo deseas)
            os.remove(pdf_file_path)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al enviar el correo: {e}")

    def obtenerEmailUsuario(self):
        """Obtiene el correo del usuario desde la base de datos."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM Empleados WHERE idUsuario = ?", (self.id_usuario,))
            email = cursor.fetchone()[0]
            return email
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al obtener el correo del usuario: {e}")
            return ""
        finally:
            self.db.close()


    def cuotaExiste(self, num_prestamo, num_cuota):
        """Verifica si la cuota ya existe en la base de datos."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()

            # Consulta para verificar si la cuota ya está registrada
            cursor.execute("""
                SELECT COUNT(*) FROM Cuotas WHERE idPrestamo = ? AND numCuota = ?
            """, (num_prestamo, num_cuota))

            # Obtener el número de coincidencias (debería ser 0 si no existe)
            resultado = cursor.fetchone()[0]
            return resultado > 0  # Devuelve True si la cuota ya existe, False si no
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al verificar la cuota: {e}")
            return False
        finally:
            self.db.close()

    def marcarComoMoroso(self, num_prestamo, num_cuota):
        """Marca la cuota como morosa si el pago es posterior al 10 de cada mes."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Cuotas 
                SET idEstado = (SELECT idEstado FROM EstadoCuota WHERE estado = 'Moroso')
                WHERE idPrestamo = ? AND numCuota = ?
            """, (num_prestamo, num_cuota))
            conn.commit()
            QMessageBox.warning(self, "Aviso", "El pago se registró tarde, la cuota será marcada como morosa.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al marcar como moroso: {e}")
        finally:
            self.db.close()

