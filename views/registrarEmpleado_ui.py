# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrarEmpleado.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_registrarEmpleados(object):
    def setupUi(self, registrarEmpleados):
        if not registrarEmpleados.objectName():
            registrarEmpleados.setObjectName(u"registrarEmpleados")
        registrarEmpleados.resize(504, 373)
        registrarEmpleados.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(registrarEmpleados)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 561, 71))
        font = QFont()
        font.setPointSize(5)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(37, 99, 175);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txtTittle = QLabel(self.frame)
        self.txtTittle.setObjectName(u"txtTittle")
        self.txtTittle.setGeometry(QRect(60, 10, 401, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTittle.sizePolicy().hasHeightForWidth())
        self.txtTittle.setSizePolicy(sizePolicy)
        self.txtTittle.setMinimumSize(QSize(5, 0))
        font1 = QFont()
        font1.setPointSize(23)
        font1.setBold(True)
        self.txtTittle.setFont(font1)
        self.txtTittle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(50, 140, 131, 31))
        font2 = QFont()
        font2.setBold(True)
        font2.setKerning(True)
        self.txtCedula.setFont(font2)
        self.txtCedula.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtCedula.setAlignment(Qt.AlignCenter)
        self.txtCedula.setReadOnly(False)
        self.txtContrasenia = QLineEdit(self.centralwidget)
        self.txtContrasenia.setObjectName(u"txtContrasenia")
        self.txtContrasenia.setGeometry(QRect(50, 210, 131, 31))
        self.txtContrasenia.setFont(font2)
        self.txtContrasenia.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtContrasenia.setEchoMode(QLineEdit.Password)
        self.txtContrasenia.setAlignment(Qt.AlignCenter)
        self.txtContrasenia.setReadOnly(False)
        self.btnCrearEmpleado = QPushButton(self.centralwidget)
        self.btnCrearEmpleado.setObjectName(u"btnCrearEmpleado")
        self.btnCrearEmpleado.setGeometry(QRect(280, 330, 93, 28))
        self.btnCrearEmpleado.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:8px\n"
"")
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(320, 140, 131, 31))
        self.txtNombre.setFont(font2)
        self.txtNombre.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtNombre.setAlignment(Qt.AlignCenter)
        self.txtNombre.setReadOnly(False)
        self.comboBoxCargo = QComboBox(self.centralwidget)
        self.comboBoxCargo.setObjectName(u"comboBoxCargo")
        self.comboBoxCargo.setGeometry(QRect(320, 210, 131, 31))
        self.comboBoxCargo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.lblCedula = QLabel(self.centralwidget)
        self.lblCedula.setObjectName(u"lblCedula")
        self.lblCedula.setGeometry(QRect(50, 120, 91, 20))
        font3 = QFont()
        font3.setPointSize(9)
        self.lblCedula.setFont(font3)
        self.lblCedula.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblContrasenia = QLabel(self.centralwidget)
        self.lblContrasenia.setObjectName(u"lblContrasenia")
        self.lblContrasenia.setGeometry(QRect(50, 190, 91, 20))
        self.lblContrasenia.setFont(font3)
        self.lblContrasenia.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(320, 120, 91, 20))
        self.lblNombre.setFont(font3)
        self.lblNombre.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lblCargo = QLabel(self.centralwidget)
        self.lblCargo.setObjectName(u"lblCargo")
        self.lblCargo.setGeometry(QRect(320, 190, 91, 20))
        self.lblCargo.setFont(font3)
        self.lblCargo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.btnRegresar = QPushButton(self.centralwidget)
        self.btnRegresar.setObjectName(u"btnRegresar")
        self.btnRegresar.setGeometry(QRect(380, 330, 93, 28))
        self.btnRegresar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:8px\n"
"")
        self.lblSucursal = QLabel(self.centralwidget)
        self.lblSucursal.setObjectName(u"lblSucursal")
        self.lblSucursal.setGeometry(QRect(50, 250, 91, 20))
        self.lblSucursal.setFont(font3)
        self.lblSucursal.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comboBoxSucursal = QComboBox(self.centralwidget)
        self.comboBoxSucursal.setObjectName(u"comboBoxSucursal")
        self.comboBoxSucursal.setGeometry(QRect(50, 270, 131, 31))
        self.comboBoxSucursal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        registrarEmpleados.setCentralWidget(self.centralwidget)

        self.retranslateUi(registrarEmpleados)

        QMetaObject.connectSlotsByName(registrarEmpleados)
    # setupUi

    def retranslateUi(self, registrarEmpleados):
        registrarEmpleados.setWindowTitle(QCoreApplication.translate("registrarEmpleados", u"Registrar Empleados", None))
        self.txtTittle.setText(QCoreApplication.translate("registrarEmpleados", u"Registrar empleados", None))
        self.txtCedula.setPlaceholderText(QCoreApplication.translate("registrarEmpleados", u"C\u00e9dula", None))
        self.txtContrasenia.setPlaceholderText(QCoreApplication.translate("registrarEmpleados", u"Contrase\u00f1a", None))
        self.btnCrearEmpleado.setText(QCoreApplication.translate("registrarEmpleados", u"Crear", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("registrarEmpleados", u"Nombre", None))
        self.lblCedula.setText(QCoreApplication.translate("registrarEmpleados", u"Cedula", None))
        self.lblContrasenia.setText(QCoreApplication.translate("registrarEmpleados", u"Contrase\u00f1a", None))
        self.lblNombre.setText(QCoreApplication.translate("registrarEmpleados", u"Nombre", None))
        self.lblCargo.setText(QCoreApplication.translate("registrarEmpleados", u"Cargo", None))
        self.btnRegresar.setText(QCoreApplication.translate("registrarEmpleados", u"Regresar", None))
        self.lblSucursal.setText(QCoreApplication.translate("registrarEmpleados", u"Sucursal", None))
    # retranslateUi

