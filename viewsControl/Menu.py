import subprocess
import webbrowser
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QDialog
from PyQt6.QtCore import QPropertyAnimation
from viewsControl.RegistrarEmpleado import RegistrarEmpleado  # Importa la clase que creamos
from viewsControl.RegistrarSucursal import RegistrarSucursal
from viewsControl.VerUsuarios import VerUsuarios
from viewsControl.VerAuditorias import VerAuditorias
from viewsControl.VerPrestamosUsuarios import VerPrestamosUsuarios

class Menu(QMainWindow):  # Hereda de QMainWindow para consistencia con otras ventanas
    def __init__(self, login_window):
        super().__init__()  # Inicializa el QMainWindow
        self.menu = uic.loadUi("views/Menu.ui", self)  # Cargar el archivo .ui directamente en la instancia de QMainWindow
        self.login_window = login_window  # Referencia a la ventana de LogIn
        self.server_process = None
        self.iniGui()
        self.show()

    def iniGui(self):
        self.btnLogOut.clicked.connect(self.logout)
        self.btnCrearEmpleados.clicked.connect(self.abrirVentanaCrearEmpleado)
        self.btnCrearSucursales.clicked.connect(self.abriVentanaCrearSucursal)
        self.btnEmpleados.clicked.connect(self.abrirVentanaVerUsuarios)
        self.btnVerAuditorias.clicked.connect(self.abrirVentanaVerAuditorias)
        self.btnVerSolicitudesUsuarios.clicked.connect(self.abrirVentanaVerPrestamosUsuarios)
        self.btnAyudas.clicked.connect(self.abrirMenuAyuda)

    def abrirVentanaCrearEmpleado(self):
        self.menu.close()
        self.ventanaRegistrarEmpleado = RegistrarEmpleado(self)
        self.ventanaRegistrarEmpleado.show()

    def abriVentanaCrearSucursal(self):
        self.menu.close()
        self.ventanaRegistrarSucursal = RegistrarSucursal(self)
        self.ventanaRegistrarSucursal.show()

    def abrirVentanaVerUsuarios(self):
        self.menu.close()
        self.ventanaVerUsuarios = VerUsuarios(self)
        self.ventanaVerUsuarios.show()

    def abrirVentanaVerAuditorias(self):
        self.menu.close()
        self.ventanaVerAuditorias = VerAuditorias(self)
        self.ventanaVerAuditorias.show()

    def abrirVentanaVerPrestamosUsuarios(self):
        self.menu.close()
        self.ventanaVerPrestamosUsuarios = VerPrestamosUsuarios(self)
        self.ventanaVerPrestamosUsuarios.show()

    def abrirMenuAyuda(self):   
        """Abrir la página de ayuda en un servidor web local."""
        ayuda_path = os.path.abspath("config/helps-admin/site")  # Ruta a los archivos generados por MkDocs
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

    def detenerServidorWeb(self):
        """Detener el servidor web local si está en ejecución."""
        if self.server_process:
            self.server_process.terminate()  # Finalizar el proceso del servidor
            self.server_process = None
            print("Servidor web detenido.")

    def logout(self): 
        # Luego, mostrar el mensaje de confirmación
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")
        self.detenerServidorWeb()

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
            self.animation = QPropertyAnimation(self.menu, b"windowOpacity")
            self.animation.setDuration(400)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close_and_show_login)
            self.animation.start()

    def close_and_show_login(self):
        self.close()  # Cerrar el menú de administrador
        self.login_window.show()  # Mostrar nuevamente la ventana de LogIn  
