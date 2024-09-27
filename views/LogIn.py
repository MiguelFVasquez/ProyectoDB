from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QApplication
import sys
from views.Menu import Menu

class LogIn():
    def __init__(self):
        self.login = uic.loadUi("views/LogIn.ui")
        self.initGUI()
        self.login.lblMensajeError.setText("")
        self.login.show()

    # Función para validar y asegurar el ingreso
    def ingresar(self):
        usuario = self.login.txtUsuario.text()
        password = self.login.txtPassword.text()

        # Validación de longitud
        if len(usuario) < 2:
            # Mensaje de error
            self.login.lblMensajeError.setText("Ingrese un usuario válido")
            self.login.txtUsuario.setFocus()
        elif len(password) < 3:
            self.login.lblMensajeError.setText("Ingrese una contraseña válida")
            self.login.txtPassword.setFocus()
        else:
            # Verificar si es admin
            if usuario == "admin" and password == "admin":
                self.login.lblMensajeError.setText("")
                self.login.txtUsuario.clear()
                self.login.txtPassword.clear()
                self.mostrar_menu_admin()  # Aquí no se está pasando el argumento
            else:
                # Aquí agregarías la validación para usuarios normales desde la base de datos
                if self.validar_usuario_db(usuario, password):
                    self.login.lblMensajeError.setText("")
                    self.mostrar_menu_usuario()
                else:
                    self.login.lblMensajeError.setText("Credenciales incorrectas")

    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)

    # Función para mostrar el menú del administrador
    def mostrar_menu_admin(self):
        self.login.close()  # Cerrar ventana de login
        self.menu_admin = Menu(self.login)  # Pasar la referencia de login a Menu

    # Función para mostrar el menú de usuario normal
    def mostrar_menu_usuario(self):
        self.login.close()  # Cerrar ventana de login
        QMessageBox.information(self.login, "Acceso", "Bienvenido Usuario")
        # Ejemplo: Cargar otra ventana de menú de usuario
        # self.menu_usuario = uic.loadUi("views/MenuUsuario.ui")
        # self.menu_usuario.show()

    # Función para validar usuarios normales desde la base de datos
    def validar_usuario_db(self, usuario, password):
        # Simular validación para un usuario normal
        if usuario == "usuario" and password == "123":
            return True
        return False