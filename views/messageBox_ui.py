# Form implementation generated from reading ui file 'c:\Users\juan2\OneDrive\Escritorio\University\ProyectoBases\ProyectoBD\ProyectoDB\views\messageBox.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 148)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnSi = QtWidgets.QPushButton(parent=Dialog)
        self.btnSi.setEnabled(True)
        self.btnSi.setGeometry(QtCore.QRect(168, 100, 81, 28))
        self.btnSi.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnSi.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.btnSi.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnSi.setObjectName("btnSi")
        self.btnNo = QtWidgets.QPushButton(parent=Dialog)
        self.btnNo.setEnabled(True)
        self.btnNo.setGeometry(QtCore.QRect(260, 100, 81, 28))
        self.btnNo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnNo.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.btnNo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnNo.setObjectName("btnNo")
        self.lblTitulo = QtWidgets.QLabel(parent=Dialog)
        self.lblTitulo.setGeometry(QtCore.QRect(140, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblTitulo.setObjectName("lblTitulo")
        self.lblMensaje = QtWidgets.QLabel(parent=Dialog)
        self.lblMensaje.setGeometry(QtCore.QRect(10, 40, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblMensaje.setFont(font)
        self.lblMensaje.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lblMensaje.setObjectName("lblMensaje")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialogo"))
        self.btnSi.setText(_translate("Dialog", "Aceptar"))
        self.btnNo.setText(_translate("Dialog", "Cancelar"))
        self.lblTitulo.setText(_translate("Dialog", "TextLabel"))
        self.lblMensaje.setText(_translate("Dialog", "TextLabel"))
