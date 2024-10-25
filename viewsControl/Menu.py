from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QDialog
from PyQt6.QtCore import QPropertyAnimation
from viewsControl.RegistrarEmpleado import RegistrarEmpleado  # Importa la clase que creamos
from viewsControl.RegistrarSucursal import RegistrarSucursal

class Menu(QMainWindow):  # Hereda de QMainWindow para consistencia con otras ventanas
    def __init__(self, login_window):
        super().__init__()  # Inicializa el QMainWindow
        uic.loadUi("views/Menu.ui", self)  # Cargar el archivo .ui directamente en la instancia de QMainWindow
        self.login_window = login_window  # Referencia a la ventana de LogIn
        self.iniGui()
        self.show()  # Muestra la ventana de menú

    def iniGui(self):
        # Conectar el botón de "LogOut" a la función logout
        self.btnLogOut.clicked.connect(self.logout)
        self.btnEmpleados.clicked.connect(self.mostrarEntidades)
        self.btnCrearEmpleados.clicked.connect(self.abrirVentanaCrearEmpleado)  # Conecta el botón de crear empleados
        self.btnCrearSucursales.clicked.connect(self.abriVentanaCrearSucursal)

    def abrirVentanaCrearEmpleado(self):
        # Crea una instancia de la ventana de registrar empleado y la muestra
        self.ventanaRegistrarEmpleado = RegistrarEmpleado(self)  # Pasa 'self' como referencia del menú
        self.ventanaRegistrarEmpleado.show()  # Muestra la ventana de RegistrarEmpleado

    def abriVentanaCrearSucursal(self):
        self.ventanaRegistrarSucursal = RegistrarSucursal(self)
        self.ventanaRegistrarSucursal.show()

    def logout(self):
        # Mostrar mensaje de confirmación usando el método personalizado
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")

    def mostrarEntidades(self):
        QMessageBox.information(self, "Información", "Estamos trabajando en ello")

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
