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
        self.id_usuario = None  # Variable para almacenar el id del usuario que inicia sesión

    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)

    def ingresar(self):
        usuario = self.login.txtUsuario.text()
        password = self.login.txtPassword.text()

        if len(usuario) < 2:
            QMessageBox.critical(self.login, "Error", "Ingrese un usuario válido")
            self.login.txtUsuario.setFocus()
        elif len(password) < 3:
            QMessageBox.critical(self.login, "Error", "Ingrese una contraseña válida")
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
                    self.id_usuario = resultado["Usuario"]  # Guardar el id del usuario aquí
                    self.registrar_auditoria_entrada(self.id_usuario)  # Registrar entrada en la auditoría
                    if cargo == "Tesorero":
                        self.mostrar_menu_tesoreria(self.id_usuario)
                    else:
                        self.mostrar_menu_usuario(self.id_usuario) 
                else:
                    QMessageBox.critical(self.login, "Error", "Credenciales incorrectas")


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

    def mostrar_menu_tesoreria(self, Usuario):
        self.login.close()
        self.menu_Tesoreria = MenuTesoreria(self.login, Usuario)

    def registrar_auditoria_entrada(self, id_usuario):
        conexion = Conexion()
        conn = conexion.connect()
        if conn:
            try:
                cursor = conn.cursor()
                query = """
                INSERT INTO Auditorias (idUsuario, Ingreso, Salida)
                VALUES (?, GETDATE(), NULL)
                """
                cursor.execute(query, (id_usuario,))
                conn.commit()
                cursor.close()
            except Exception as e:
                print(f"Error al registrar auditoría de entrada: {e}")
            finally:
                conexion.close()