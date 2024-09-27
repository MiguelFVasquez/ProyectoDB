from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QDialog
from PyQt6.QtCore import QPropertyAnimation

class Menu:
    def __init__(self, login_window):
        self.menu = uic.loadUi("views/Menu.ui")
        self.message = uic.loadUi("views/messageBox.ui")
        self.login_window = login_window  # Referencia a la ventana de LogIn
        self.iniGui()
        self.menu.show()

    def iniGui(self):
        # Conectar el botón de "LogOut" a la función logout
        self.menu.btnLogOut.clicked.connect(self.logout)
        self.menu.btnEntidades.clicked.connect(self.mostrarEntidades)

    # Función para cerrar el menú de admin y regresar al login
        # Función para cerrar el menú de admin y regresar al login
    def logout(self):
        # Mostrar mensaje de confirmación usando el método personalizado
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")

    def mostrarEntidades(self):
        QMessageBox.information(self.menu, "Información", "Estamos trabajando en ello")

    def mensajeConfirmacion(self, title, message):
        # Cargar la interfaz de messageBox.ui
        self.message = QDialog()
        self.message = uic.loadUi("views/messageBox.ui")
        
        # Establecer el título y el mensaje
        self.message.lblTitulo.setText(title)  # Suponiendo que tienes una QLabel con nombre lblTitle
        self.message.lblMensaje.setText(message)  # Suponiendo que tienes una QLabel con nombre lblMessage

        # Conectar botones
        self.message.btnSi.clicked.connect(lambda: self.handleResponse(True))
        self.message.btnNo.clicked.connect(lambda: self.handleResponse(False))

        # Mostrar el cuadro de diálogo
        self.message.exec()  # Mostrar el diálogo de manera modal

    def handleResponse(self, accepted):
        if accepted:
            # Crear animación para desvanecer la ventana
            self.animation = QPropertyAnimation(self.menu, b"windowOpacity")
            self.animation.setDuration(400)  # Duración de 0.4 segundos
            self.animation.setStartValue(1)  # Opacidad inicial
            self.animation.setEndValue(0)  # Opacidad final
            self.animation.finished.connect(self.close_and_show_login)  # Conectar a la función de cierre
            self.animation.start()  # Iniciar la animación
        self.message.close()  # Cerrar el cuadro de diálogo


    def close_and_show_login(self):
        self.menu.close()  # Cerrar el menú de administrador
        self.login_window.show()  # Mostrar nuevamente la ventana de LogIn

