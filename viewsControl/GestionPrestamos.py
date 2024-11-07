from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from config.EmailService import EmailService
from conexion import Conexion  # Clase de conexión
from datetime import date, timedelta  # Importar para obtener la fecha actual

class GestionPrestamos(QMainWindow):
    def __init__(self, menuTesoreria):
        super().__init__()
        uic.loadUi("views/GestionPrestamos.ui", self)
        self.menuTesoreria = menuTesoreria
        self.db = Conexion()  # Instancia de conexión a la base de datos
        self.iniGui()
        self.cargarPrestamos()

    def iniGui(self):
        # Conexión de botones
        self.btnRegresar.clicked.connect(self.regresarAlMenu)
        self.btnActualizar.clicked.connect(self.cargarPrestamos)
        self.btnAceptar.clicked.connect(self.aprobarPrestamo)
        self.btnRechazar.clicked.connect(self.rechazarPrestamo)
        self.tableWidgetPrestamos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def regresarAlMenu(self):
        """Cierra la ventana actual y muestra el menú principal."""
        self.close()
        self.menuTesoreria.show()

    def obtener_prestamos(self):
        """Obtiene los préstamos pendientes de la base de datos."""
        prestamos = []
        try:
            conn = self.db.connect()  # Conectar a la base de datos
            cursor = conn.cursor()
            # Consulta que une las tablas y filtra solo los préstamos pendientes (código del estado 'Pendiente')
            cursor.execute(""" 
                SELECT 
                    sp.codigo AS idSolicitud, 
                    e.nombre AS NombreUsuario, 
                    e.cedula AS CedulaUsuario, 
                    c.NombreCargo AS Cargo, 
                    sp.monto, 
                    p.numeroMeses AS periodo, 
                    es.estado AS estado,
                    sp.FechaSolicitud AS fechaCreacion,
                    e.email AS EmailUsuario  
                FROM SolicitudPrestamo sp 
                JOIN Empleados e ON sp.Usuario = e.idUsuario  
                JOIN Cargo c ON e.idCargo = c.idCargo  
                JOIN Estado es ON sp.estado = es.codigo
                JOIN Periodo p ON sp.periodo = p.codigo
                WHERE es.estado = 'Pendiente'  -- Solo préstamos pendientes
            """)
            rows = cursor.fetchall()
            for row in rows:
                prestamos.append(row)
            return prestamos
        except Exception as e:
            print(f"Error al obtener préstamos: {e}")
            return []
        finally:
            self.db.close()  # Cierra la conexión

    def actualizar_estado_prestamo(self, id_solicitud, estado):
        """Actualiza el estado del préstamo en la base de datos."""
        estado_id = 2 if estado == "Aprobado" else 3  # Mapeo de estado a ID (suponiendo 2 = Aprobado, 3 = Rechazado)
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE SolicitudPrestamo SET Estado = ? WHERE codigo = ?", (estado_id, id_solicitud))
            conn.commit()  # Confirma los cambios
            return cursor.rowcount > 0  # Retorna True si se actualizó al menos una fila
        except Exception as e:
            print(f"Error al actualizar el estado del préstamo: {e}")
            return False
        finally:
            self.db.close()

    def registrar_prestamo(self, id_solicitud, valor_por_mes, fecha_desembolso, monto_pagar):
        """Registra la solicitud aprobada en la tabla Prestamos con el valor mensual y la fecha de desembolso."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            fecha_actual = date.today()
            # Inserta el registro en la tabla Prestamos con el valor mensual y la fecha de desembolso
            cursor.execute("""
                INSERT INTO Prestamos (codigoSolicitud, fechaCreacion, ValorPorMes, FechaDesembolso, MontoPagar) 
                VALUES (?, ?, ?, ?, ?)
            """, (id_solicitud, fecha_actual, valor_por_mes, fecha_desembolso, monto_pagar))
            conn.commit()
        except Exception as e:
            print(f"Error al registrar el préstamo: {e}")
        finally:
            self.db.close()

    def cargarPrestamos(self):
        """Carga las solicitudes de préstamos en la tabla."""
        self.tableWidgetPrestamos.setRowCount(0)  # Limpia la tabla
        prestamos = self.obtener_prestamos()  # Método que obtiene los préstamos desde la base de datos

        for row_number, prestamo in enumerate(prestamos):
            self.tableWidgetPrestamos.insertRow(row_number)
            for column_number, data in enumerate(prestamo[:-1]):  # No mostramos el email en la tabla
                item = QTableWidgetItem(str(data))
                self.tableWidgetPrestamos.setItem(row_number, column_number, item)
    
    def calcular_monto_mensual(self, monto, interes_anual, numero_meses):
        interes_total = (monto * (interes_anual / 100))
        monto_total = monto + interes_total
        monto_mensual = monto_total / numero_meses
        return round(monto_mensual, 2)
    
    def calcular_monto_pagar(self, monto, interes_anual):
        interes_total = (monto * (interes_anual / 100))
        monto_total = monto + interes_total
        return round(monto_total, 2)
    
    def obtener_interes_periodo(self, id_solicitud):
        """Obtiene el valor del interés asociado al periodo de la solicitud de préstamo."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.interes
                FROM Periodo p
                JOIN SolicitudPrestamo sp ON sp.periodo = p.codigo
                WHERE sp.codigo = ?
            """, (id_solicitud,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error al obtener el interés del periodo: {e}")
            return None
        finally:
            self.db.close()


    def aprobarPrestamo(self):
        """Aprueba el préstamo seleccionado en la tabla."""
        fila = self.tableWidgetPrestamos.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Seleccione una solicitud para aprobar.")
            return

        id_solicitud = self.tableWidgetPrestamos.item(fila, 0).text()
        nombre_usuario = self.tableWidgetPrestamos.item(fila, 1).text()  # Nombre del usuario
        email_usuario = self.obtener_email_usuario(id_solicitud)  # Método para obtener el email

        # Obtener detalles del préstamo
        monto = float(self.tableWidgetPrestamos.item(fila, 4).text())
        interes = self.obtener_interes_periodo(id_solicitud)
        numero_meses = self.obtener_numero_meses_periodo(id_solicitud)
       
        # Calcular el valor mensual del préstamo
        if numero_meses:
            valor_por_mes = self.calcular_monto_mensual(monto, interes, numero_meses)
        else:
            QMessageBox.critical(self, "Error", "No se pudo obtener el número de meses del periodo.")
            return
        
        if monto:
            valor_pagar = self.calcular_monto_pagar(monto,interes)
        else:
            QMessageBox.critical(self, "Error", "No se pudo obtener el monto del préstamo.")
            return

        # Calcular la fecha de desembolso (día 3 del mes siguiente)
        hoy = date.today()
        if hoy.month == 12:  # Si es diciembre, incrementa el año y reinicia el mes a enero
            fecha_desembolso = date(hoy.year + 1, 1, 3)
        else:
            fecha_desembolso = date(hoy.year, hoy.month + 1, 3)

        if self.actualizar_estado_prestamo(id_solicitud, "Aprobado"):
            # Registrar en la tabla Prestamos
            self.registrar_prestamo(id_solicitud, valor_por_mes, fecha_desembolso, valor_pagar)

            # Enviar email de confirmación
            mensaje = (f"Tu solicitud ha sido aprobada. El dinero del préstamo será desembolsado directamente a tu "
                    f"cuenta de banco el día {fecha_desembolso.strftime('%d/%m/%Y')}. Con un codigo de solicitud: #{id_solicitud} elegida a {numero_meses} meses con un interes del {interes}% para un total a pagar de ${valor_pagar} pesos")
            
            EmailService.emailMessages(
                asunto="Solicitud aprobada",
                email=email_usuario,
                nombre=nombre_usuario,
                mensaje=mensaje
            )

            QMessageBox.information(self, "Éxito", "Préstamo aprobado con éxito.")
            self.cargarPrestamos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo aprobar el préstamo.")

    def rechazarPrestamo(self):
        """Rechaza el préstamo seleccionado en la tabla."""
        fila = self.tableWidgetPrestamos.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Seleccione una solicitud para rechazar.")
            return

        id_solicitud = self.tableWidgetPrestamos.item(fila, 0).text()
        nombre_usuario = self.tableWidgetPrestamos.item(fila, 1).text()  # Nombre del usuario
        email_usuario = self.obtener_email_usuario(id_solicitud)  # Método para obtener el email

        if self.actualizar_estado_prestamo(id_solicitud, "Rechazado"):
            # Registrar en la tabla Prestamos
            self.registrar_prestamo(id_solicitud)

            QMessageBox.information(self, "Éxito", "Préstamo rechazado con éxito.")
            # Enviar email de confirmación
            EmailService.emailMessages(
                asunto="Solicitud rechazada",
                email=email_usuario,  # Uso del email del usuario
                nombre=nombre_usuario,  # Uso del nombre del usuario
                mensaje="Tu solicitud ha sido rechazada. Por favor, verifica los requisitos y vuelve a intentarlo."
            )
            self.cargarPrestamos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo rechazar el préstamo.")

    def obtener_email_usuario(self, id_solicitud):
        """Obtiene el correo electrónico del usuario basado en la solicitud de préstamo."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT e.email FROM SolicitudPrestamo sp JOIN Empleados e ON sp.Usuario = e.idUsuario WHERE sp.codigo = ?", (id_solicitud,))
            email = cursor.fetchone()
            return email[0] if email else None
        except Exception as e:
            print(f"Error al obtener el email del usuario: {e}")
            return None
        finally:
            self.db.close()

    def obtener_numero_meses_periodo(self, id_solicitud):
        """Obtiene el número de meses del periodo asociado a la solicitud de préstamo."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            # Consultar el número de meses en la tabla Periodo mediante la relación con SolicitudPrestamo
            cursor.execute("""
                SELECT p.numeroMeses
                FROM Periodo p
                JOIN SolicitudPrestamo sp ON sp.periodo = p.codigo
                WHERE sp.codigo = ?
            """, (id_solicitud,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error al obtener el número de meses del periodo: {e}")
            return None
        finally:
            self.db.close()