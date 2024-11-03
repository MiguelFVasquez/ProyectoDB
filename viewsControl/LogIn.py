from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from viewsControl.Menu import Menu
from viewsControl.MenuUsuarios import MenuUsuarios
from viewsControl.MenuTesoreria import MenuTesoreria 
from conexion import Conexion

class LogIn:
    def __init__(self):
        self.login = uic.loadUi("views/LogIn.ui") 
        self.initGUI()
        self.login.lblMensajeError.setText("")
        self.login.show()
        self.db = Conexion()  # Instancia de la conexión a la base de datos

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
            if usuario == "admin" and password == "admin":
                self.login.lblMensajeError.setText("")
                self.login.txtUsuario.clear()
                self.login.txtPassword.clear()
                self.mostrar_menu_admin()
            else:
                resultado = self.validar_usuario_db(usuario, password)
                if resultado:
                    self.login.lblMensajeError.setText("")
                    self.login.txtUsuario.clear()
                    self.login.txtPassword.clear()
                    cargo = resultado["cargo"]
                    Usuario = resultado["Usuario"]  # Obtener el id del empleado
                    if cargo == "Tesorero":
                        self.mostrar_menu_tesoreria()
                    else:
                        self.mostrar_menu_usuario(Usuario)  # Pasar el id al menú de usuario
                else:
                    self.login.lblMensajeError.setText("Credenciales incorrectas")

    def validar_usuario_db(self, usuario, password):
        conexion = self.db.connect()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                SELECT E.idUsuario, E.idCargo, C.NombreCargo 
                FROM Empleados E
                JOIN Cargo C ON E.idCargo = C.idCargo
                WHERE E.cedula = ? AND E.clave = ?
                """
                cursor.execute(query, (usuario, password))
                result = cursor.fetchone()
                cursor.close()
                self.db.close()

                if result:
                    return {
                        "Usuario": result[0],  # id del empleado
                        "idCargo": result[1],
                        "cargo": result[2]
                    }
                return False

            except Exception as e:
                print(f"Error en la consulta: {e}")
                return False
        else:
            return False

    def mostrar_menu_admin(self):
        self.login.close()
        self.menu_admin = Menu(self.login)

    def mostrar_menu_usuario(self, Usuario):
        self.login.close()
        self.menu_Usuarios = MenuUsuarios(self.login, Usuario)  # Pasar el id al menú de usuario

    def mostrar_menu_tesoreria(self):
        self.login.close()
        self.menu_Tesoreria = MenuTesoreria(self.login)
