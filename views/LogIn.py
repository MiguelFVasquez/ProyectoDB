from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from views.Menu import Menu
from conexion import Conexion  # Importa la clase de conexión

class LogIn:
    def __init__(self):
        self.login = uic.loadUi("views/LogIn.ui")
        self.initGUI()
        self.login.lblMensajeError.setText("")
        self.login.show()
        # Crear una instancia de la conexión a la base de datos
        self.db = Conexion()

    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)

    def ingresar(self):
        usuario = self.login.txtUsuario.text()
        password = self.login.txtPassword.text()

        if len(usuario) < 2:
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
                self.mostrar_menu_admin()
            else:
                # Validar usuario desde la base de datos
                if self.validar_usuario_db(usuario, password):
                    self.login.lblMensajeError.setText("")
                    self.login.txtUsuario.clear()
                    self.login.txtPassword.clear()
                    self.mostrar_menu_usuario()
                else:
                    self.login.lblMensajeError.setText("Credenciales incorrectas")
    
    # Función para validar usuarios en la base de datos usando la clase DatabaseConnection
    def validar_usuario_db(self, usuario, password):
        conexion = self.db.connect()  # Conectar a la base de datos
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT * FROM Usuarios WHERE cedula = ? AND clave = ?"
                cursor.execute(query, (usuario, password))
                result = cursor.fetchone()

                cursor.close()
                self.db.close()

                if result:
                    return True
                return False

            except Exception as e:
                print(f"Error en la consulta: {e}")
                return False
        else:
            return False

    def mostrar_menu_admin(self):
        self.login.close()  # Cerrar ventana de login
        self.menu_admin = Menu(self.login)

    def mostrar_menu_usuario(self):
        self.login.close()  # Cerrar ventana de login
        self.menu_admin = Menu(self.login)
