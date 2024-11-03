from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from config.EmailService import EmailService
from conexion import Conexion  # Clase de conexión
from datetime import date  # Importar para obtener la fecha actual

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

    def registrar_prestamo(self, id_solicitud):
        """Registra la solicitud en la tabla Prestamos una vez aprobada o rechazada."""
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            fecha_actual = date.today()
            # Inserta el registro en la tabla Prestamos
            cursor.execute("""
                INSERT INTO Prestamos (codigoSolicitud, fechaCreacion) 
                VALUES (?, ?)
            """, (id_solicitud, fecha_actual))
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

    def aprobarPrestamo(self):
        """Aprueba el préstamo seleccionado en la tabla."""
        fila = self.tableWidgetPrestamos.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Seleccione una solicitud para aprobar.")
            return

        id_solicitud = self.tableWidgetPrestamos.item(fila, 0).text()
        nombre_usuario = self.tableWidgetPrestamos.item(fila, 1).text()  # Nombre del usuario
        email_usuario = self.obtener_email_usuario(id_solicitud)  # Método para obtener el email

        if self.actualizar_estado_prestamo(id_solicitud, "Aprobado"):
            # Registrar en la tabla Prestamos
            self.registrar_prestamo(id_solicitud)

            QMessageBox.information(self, "Éxito", "Préstamo aprobado con éxito.")
            # Enviar email de confirmación
            EmailService.emailMessages(
                asunto="Solicitud aprobada",
                email=email_usuario,  # Uso del email del usuario
                nombre=nombre_usuario,  # Uso del nombre del usuario
                mensaje="Tu solicitud ha sido aprobada. El dinero se ha desembolsado en su cuenta."
            )
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