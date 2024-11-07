from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QDialog
from PyQt6.QtCore import QPropertyAnimation
from viewsControl.RegistrarEmpleado import RegistrarEmpleado  # Importa la clase que creamos
from viewsControl.RegistrarSucursal import RegistrarSucursal
from viewsControl.VerUsuarios import VerUsuarios
from viewsControl.VerAuditorias import VerAuditorias

class Menu(QMainWindow):  # Hereda de QMainWindow para consistencia con otras ventanas
    def __init__(self, login_window):
        super().__init__()  # Inicializa el QMainWindow
        self.menu = uic.loadUi("views/Menu.ui", self)  # Cargar el archivo .ui directamente en la instancia de QMainWindow
        self.login_window = login_window  # Referencia a la ventana de LogIn
        self.iniGui()
        self.show()

    def iniGui(self):
        self.btnLogOut.clicked.connect(self.logout)
        self.btnCrearEmpleados.clicked.connect(self.abrirVentanaCrearEmpleado)
        self.btnCrearSucursales.clicked.connect(self.abriVentanaCrearSucursal)
        self.btnEmpleados.clicked.connect(self.abrirVentanaVerUsuarios)
        self.btnVerAuditorias.clicked.connect(self.abrirVentanaVerAuditorias)

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

    def logout(self): 
        # Luego, mostrar el mensaje de confirmación
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")


    def mensajeConfirmacion(self, title, message):
        # Cargar la interfaz de messageBox.ui
        self.message = QDialog()
        self.message = uic.loadUi("views/messageBox.ui", self.message)
        
        # Establecer el título y el mensaje
        self.message.lblTitulo.setText(title)
        self.message.lblMensaje.setText(message)

        # Conectar botones
        self.message.btnSi.clicked.connect(lambda: self.handleResponse(True))
        self.message.btnNo.clicked.connect(lambda: self.handleResponse(False))

        # Mostrar el cuadro de diálogo
        self.message.exec()

    def handleResponse(self, accepted):
        if accepted:
            # Crear animación para desvanecer la ventana
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(400)  # Duración de 0.4 segundos
            self.animation.setStartValue(1)  # Opacidad inicial
            self.animation.setEndValue(0)  # Opacidad final
            self.animation.finished.connect(self.close_and_show_login)
            self.animation.start()  # Iniciar la animación
        self.message.close()

    def close_and_show_login(self):
        self.close()  # Cerrar el menú de administrador
        self.login_window.show()  # Mostrar nuevamente la ventana de LogIn  
