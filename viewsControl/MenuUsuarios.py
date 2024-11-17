import subprocess
import webbrowser
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from PyQt6.QtCore import QPropertyAnimation
from conexion import Conexion
from viewsControl.SolicitarPrestamo import SolicitarPrestamo
from viewsControl.VerSolicitudes import VerSolicitudes
from viewsControl.InformeCuotas import InformeCuotas

class MenuUsuarios(QMainWindow):
    def __init__(self, login_window, Usuario):
        super().__init__()
        self.menuUsuarios = uic.loadUi("views/MenuUsuarios.ui", self)
        self.login_window = login_window
        self.Usuario = Usuario  # Guardar el id del empleado
        self.server_process = None  # Variable para guardar el proceso del servidor
        self.iniGui()
        self.show()

    def iniGui(self):
        self.menuUsuarios.btnLogOut.clicked.connect(self.logout)
        self.menuUsuarios.btnPrestamos.clicked.connect(self.abriVentanaSolicitarPrestamo)
        self.menuUsuarios.btnVerSolicitudes.clicked.connect(self.abriVentanaSolicitudes)
        self.menuUsuarios.btnCuotas.clicked.connect(self.abrirVentanaInformeCuotas)
        self.menuUsuarios.btnAyudas.clicked.connect(self.abrirMenuAyuda)

    def abrirMenuAyuda(self):   
        """Abrir la página de ayuda en un servidor web local."""
        ayuda_path = os.path.abspath("config/helps-users/site")  # Ruta a los archivos generados por MkDocs
        if os.path.exists(ayuda_path):
            try:
                # Iniciar un servidor web local en el puerto 8000
                self.server_process = subprocess.Popen(
                    ["python", "-m", "http.server", "8000", "--directory", ayuda_path]
                )
                # Abrir el navegador predeterminado con la URL
                webbrowser.open("http://localhost:8000")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo iniciar el servidor de ayuda: {e}")
        else:
            QMessageBox.warning(self, "Ayuda", "El archivo de ayuda no se encontró.")

    def logout(self):
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")
        if self.Usuario:  # Solo registrar la salida si hay un id_usuario
            self.registrar_auditoria_salida(self.Usuario)

        self.detenerServidorWeb()

    def detenerServidorWeb(self):
        """Detener el servidor web local si está en ejecución."""
        if self.server_process:
            self.server_process.terminate()  # Finalizar el proceso del servidor
            self.server_process = None
            print("Servidor web detenido.")

    def abriVentanaSolicitarPrestamo(self):
        self.menuUsuarios.close()
        self.ventanaSolicitarPrestamo = SolicitarPrestamo(self, self.Usuario)
        self.ventanaSolicitarPrestamo.show()

    def abriVentanaSolicitudes(self):
        self.menuUsuarios.close()
        self.ventanaSolicitudes = VerSolicitudes(self, self.Usuario)
        self.ventanaSolicitudes.show()

    def abrirVentanaInformeCuotas(self):
        self.menuUsuarios.close()
        self.ventanaInformeCuotas = InformeCuotas(self, self.Usuario)
        self.ventanaInformeCuotas.show()

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
            self.animation = QPropertyAnimation(self.menuUsuarios, b"windowOpacity")
            self.animation.setDuration(400)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close_and_show_login)
            self.animation.start()

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
