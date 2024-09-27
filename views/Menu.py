from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QPropertyAnimation

class Menu:
    def __init__(self, login_window):
        self.menu = uic.loadUi("views/Menu.ui")
        self.login_window = login_window  # Referencia a la ventana de LogIn
        self.iniGui()
        self.menu.show()

    def iniGui(self):
        # Conectar el botón de "LogOut" a la función logout
        self.menu.btnLogOut.clicked.connect(self.logout)
        self.menu.btnEntidades.clicked.connect(self.mostrarEntidades)

    # Función para cerrar el menú de admin y regresar al login
    def logout(self):
        # Mostrar mensaje de confirmación
        reply = QMessageBox.question(self.menu, 'Salir', 
                                     '¿Estás seguro de que quieres cerrar sesión?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            # Crear animación para desvanecer la ventana
            self.animation = QPropertyAnimation(self.menu, b"windowOpacity")
            self.animation.setDuration(400)  # Duración de 0.5 segundos
            self.animation.setStartValue(1)  # Opacidad inicial
            self.animation.setEndValue(0)  # Opacidad final
            self.animation.finished.connect(self.close_and_show_login)  # Conectar a la función de cierre
            self.animation.start()  # Iniciar la animación

    def mostrarEntidades(self):
        reply = QMessageBox.information(self.menu, "Informacion","Estmos trabajando en ello")

    def close_and_show_login(self):
        self.menu.close()  # Cerrar el menú de administrador
        self.login_window.show()  # Mostrar nuevamente la ventana de LogIn

