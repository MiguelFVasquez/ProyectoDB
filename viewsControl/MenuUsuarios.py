from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QDialog, QMainWindow
from PyQt6.QtCore import QPropertyAnimation
from conexion import Conexion
from viewsControl.SolicitarPrestamo import SolicitarPrestamo
from viewsControl.VerSolicitudes import VerSolicitudes
from viewsControl.InformeCuotas import InformeCuotas

class MenuUsuarios(QMainWindow):
    def __init__(self, login_window, Usuario):
        super().__init__()
        self.menuUsuarios = uic.loadUi("views/MenuUsuarios.ui", self)
        self.message = uic.loadUi("views/messageBox.ui")
        self.login_window = login_window
        self.Usuario = Usuario  # Guardar el id del empleado
        self.iniGui()
        self.show()

    def iniGui(self):
        self.menuUsuarios.btnLogOut.clicked.connect(self.logout)
        self.menuUsuarios.btnPrestamos.clicked.connect(self.abriVentanaSolicitarPrestamo)
        self.menuUsuarios.btnVerSolicitudes.clicked.connect(self.abriVentanaSolicitudes)
        self.menuUsuarios.btnCuotas.clicked.connect(self.abrirVentanaInformeCuotas)

    def logout(self):
        if self.Usuario:  # Solo registrar la salida si hay un id_usuario
            self.registrar_auditoria_salida(self.Usuario)
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")

    def abriVentanaSolicitarPrestamo(self):
        self.menuUsuarios.close()
        self.ventanaSolicitarPrestamo = SolicitarPrestamo(self, self.Usuario)  # Pasar el id al abrir la ventana
        self.ventanaSolicitarPrestamo.show()

    def abriVentanaSolicitudes(self):
        self.menuUsuarios.close()
        self.ventanaSolicitudes = VerSolicitudes(self, self.Usuario)
        self.ventanaSolicitudes.show()

    def abrirVentanaInformeCuotas(self):
        self.menuUsuarios.close()
        self.ventanaInformeCuotas = InformeCuotas(self,self.Usuario)
        self.ventanaInformeCuotas.show()

    def mensajeConfirmacion(self, title, message):
        self.message = QDialog()
        self.message = uic.loadUi("views/messageBox.ui")
        self.message.lblTitulo.setText(title)
        self.message.lblMensaje.setText(message)
        self.message.btnSi.clicked.connect(lambda: self.handleResponse(True))
        self.message.btnNo.clicked.connect(lambda: self.handleResponse(False))
        self.message.exec()

    def handleResponse(self, accepted):
        if accepted:
            self.animation = QPropertyAnimation(self.menuUsuarios, b"windowOpacity")
            self.animation.setDuration(400)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close_and_show_login)
            self.animation.start()
        self.message.close()

    def close_and_show_login(self):
        self.menuUsuarios.close()
        self.login_window.show()

    def registrar_auditoria_salida(self, Usuario):
        conexion = Conexion()
        conn = conexion.connect()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                UPDATE Auditorias
                SET Salida = GETDATE()
                WHERE idUsuario = ? AND Salida IS NULL
                AND Ingreso = (
                    SELECT TOP 1 Ingreso
                    FROM Auditorias
                    WHERE idUsuario = ? AND Salida IS NULL
                    ORDER BY Ingreso DESC
                )
                """
                cursor.execute(query, (Usuario, Usuario))
                conn.commit()

                if cursor.rowcount > 0:
                    print(f"Salida registrada correctamente para el usuario con ID: {Usuario}")
                else:
                    print(f"No se encontró el registro de entrada para el usuario con ID: {Usuario}")
                
                cursor.close()
            except Exception as e:
                print(f"Error al registrar auditoría de salida: {e}")
            finally:
                conexion.close()