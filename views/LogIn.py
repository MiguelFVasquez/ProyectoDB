from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox


class LogIn():
    def __init__(self) :
        self.login=uic.loadUi("views/LogIn.ui")
        self.login.show()