from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox


class LogIn():
    def __init__(self) :
        self.login=uic.loadUi("views/LogIn.ui")
        self.initGUI()
        self.login.lblMensajeError.setText("")
        self.login.show()
    #Función para validar y asegurar el ingreso
    def ingresar(self):
        if len(self.login.txtUsuario.text())<2:
            #Mensaje de error
            self.login.lblMensajeError.setText("Ingrese un usuario válido")
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtPassword.text())<3:
            self.login.lblMensajeError.setText("Ingrese una contraseña válida")
            self.login.txtPassword.setFocus()
        else:
            #Carga la intefaz del usuario ingresado
            self.login.lblMensajeError.setText("")
    
    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)