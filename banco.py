from PyQt6.QtWidgets import QApplication

from views.LogIn import LogIn


class Banco():
    def __init__(self):#Constructor
        self.app= QApplication([])
        self.login = LogIn()

        self.app.exec()
