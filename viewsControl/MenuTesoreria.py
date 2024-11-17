from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt6.QtCore import QPropertyAnimation
from conexion import Conexion
from viewsControl.GestionPrestamos import GestionPrestamos
from viewsControl.VerPrestamosUsuarios import VerPrestamosUsuarios

class MenuTesoreria(QMainWindow):
    def __init__(self, login_window,Usuario):
        super().__init__()
        self.menuTesoreria = uic.loadUi("views/MenuTesoreria.ui", self)
        self.message = uic.loadUi("views/messageBox.ui")
        self.login_window = login_window  
        self.Usuario = Usuario
        self.iniGui()
        self.show()

    def iniGui(self):
        # Conectar el botón de "LogOut" a la función logout
        self.menuTesoreria.btnLogOut.clicked.connect(self.logout)
        self.menuTesoreria.btnGestionarSolicitudes.clicked.connect(self.abrirVentanaGestionPrestamos)
        self.menuTesoreria.btnVerSolicitudes.clicked.connect(self.abrirVentanaVerPrestamosUsuarios)

    def logout(self):
        if self.Usuario:  # Solo registrar la salida si hay un id_usuario
            self.registrar_auditoria_salida(self.Usuario)
        # Mostrar mensaje de confirmación usando el método personalizado
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")

    def abrirVentanaGestionPrestamos(self):
        self.menuTesoreria.close()
        self.ventanaGestionPrestamos = GestionPrestamos(self)
        self.ventanaGestionPrestamos.show()

    def abrirVentanaVerPrestamosUsuarios(self):
        self.menuTesoreria.close()
        self.ventanaVerPrestamosUsuarios = VerPrestamosUsuarios(self)
        self.ventanaVerPrestamosUsuarios.show()

    def mensajeConfirmacion(self, title, message):
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle(title)
            msg_box.setText(message)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            result = msg_box.exec()

            if result == QMessageBox.StandardButton.Yes:
                self.handleResponse(True)
            else:
                self.handleResponse(False)

    def handleResponse(self, accepted):
        if accepted:
            self.animation = QPropertyAnimation(self.menuTesoreria, b"windowOpacity")
            self.animation.setDuration(400)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close_and_show_login)
            self.animation.start()

    def close_and_show_login(self):
        self.menuTesoreria.close()  # Cerrar el menú de administrador
        self.login_window.show()  # Mostrar nuevamente la ventana de LogIn

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