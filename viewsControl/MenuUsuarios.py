from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QDialog
from PyQt6.QtCore import QPropertyAnimation

class MenuUsuarios:
    def __init__(self, login_window):
        self.menuUsuarios = uic.loadUi("views/MenuUsuarios.ui")
        self.message = uic.loadUi("views/messageBox.ui")
        self.login_window = login_window
        self.iniGui()
        self.menuUsuarios.show()

    def iniGui(self):
        # Conectar el botón de "LogOut" a la función logout
        self.menuUsuarios.btnLogOut.clicked.connect(self.logout)

    def logout(self):
        # Mostrar mensaje de confirmación usando el método personalizado
        self.mensajeConfirmacion("Salir", "¿Estás seguro de que quieres cerrar sesión?")

    def mensajeConfirmacion(self, title, message):
        # Cargar la interfaz de messageBox.ui
        self.message = QDialog()
        self.message = uic.loadUi("views/messageBox.ui")
        
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
            self.animation = QPropertyAnimation(self.menuUsuarios, b"windowOpacity")
            self.animation.setDuration(400)  # Duración de 0.4 segundos
            self.animation.setStartValue(1)  # Opacidad inicial
            self.animation.setEndValue(0)  # Opacidad final
            self.animation.finished.connect(self.close_and_show_login)
            self.animation.start()  # Iniciar la animación
        self.message.close()

    def close_and_show_login(self):
        self.menuUsuarios.close()  # Cerrar el menú de administrador
        self.login_window.show()  # Mostrar nuevamente la ventana de LogIn