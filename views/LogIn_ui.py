# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogIn.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_formLogIn(object):
    def setupUi(self, formLogIn):
        if not formLogIn.objectName():
            formLogIn.setObjectName(u"formLogIn")
        formLogIn.resize(482, 318)
        formLogIn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(formLogIn)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 90, 201, 21))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(formLogIn)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 140, 91, 20))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(formLogIn)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 190, 91, 20))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.txtUsuario = QLineEdit(formLogIn)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(210, 140, 181, 20))
        font1 = QFont()
        font1.setBold(True)
        self.txtUsuario.setFont(font1)
        self.txtUsuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtUsuario.setMaxLength(32728)
        self.txtUsuario.setCursorPosition(0)
        self.txtUsuario.setAlignment(Qt.AlignCenter)
        self.txtUsuario.setDragEnabled(False)
        self.txtUsuario.setReadOnly(False)
        self.txtUsuario.setPlaceholderText(u"Ingrese usuario")
        self.txtPassword = QLineEdit(formLogIn)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(210, 180, 181, 20))
        self.txtPassword.setFont(font1)
        self.txtPassword.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.txtPassword.setAlignment(Qt.AlignCenter)
        self.btnAcceder = QPushButton(formLogIn)
        self.btnAcceder.setObjectName(u"btnAcceder")
        self.btnAcceder.setGeometry(QRect(210, 240, 82, 25))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        self.btnAcceder.setFont(font2)
        self.btnAcceder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAcceder.setFocusPolicy(Qt.ClickFocus)
        self.btnAcceder.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:8px\n"
"")
        self.frame = QFrame(formLogIn)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 491, 61))
        self.frame.setStyleSheet(u"background-color: rgb(37, 99, 175);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 0, 231, 51))
        self.label.setStyleSheet(u"background-color: rgb(37, 99, 175);\n"
"color: rgb(255, 255, 255);")
        self.lblMensajeError = QLabel(formLogIn)
        self.lblMensajeError.setObjectName(u"lblMensajeError")
        self.lblMensajeError.setGeometry(QRect(63, 290, 391, 20))
        self.lblMensajeError.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lblMensajeError.setAlignment(Qt.AlignCenter)
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.txtUsuario.raise_()
        self.txtPassword.raise_()
        self.btnAcceder.raise_()
        self.lblMensajeError.raise_()

        self.retranslateUi(formLogIn)

        QMetaObject.connectSlotsByName(formLogIn)
    # setupUi

    def retranslateUi(self, formLogIn):
        formLogIn.setWindowTitle(QCoreApplication.translate("formLogIn", u"Inicio de sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("formLogIn", u"Inicio de sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("formLogIn", u"Usuario", None))
        self.label_4.setText(QCoreApplication.translate("formLogIn", u"Contrase\u00f1a", None))
        self.txtUsuario.setText("")
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("formLogIn", u"Ingrese contrase\u00f1a", None))
        self.btnAcceder.setText(QCoreApplication.translate("formLogIn", u"Acceder", None))
        self.label.setText(QCoreApplication.translate("formLogIn", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Banco UQ</span></p></body></html>", None))
        self.lblMensajeError.setText(QCoreApplication.translate("formLogIn", u"Mensaje", None))
    # retranslateUi

