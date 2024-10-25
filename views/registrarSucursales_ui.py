# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrarSucursales.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 318)
        self.centralwidget = QWidget(MainWindow)
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
        self.txtTittle.setGeometry(QRect(80, 10, 401, 51))
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
        self.lblDireccion = QLabel(self.centralwidget)
        self.lblDireccion.setObjectName(u"lblDireccion")
        self.lblDireccion.setGeometry(QRect(340, 100, 91, 20))
        font2 = QFont()
        font2.setPointSize(9)
        self.lblDireccion.setFont(font2)
        self.lblDireccion.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.txtNombreSucursal = QLineEdit(self.centralwidget)
        self.txtNombreSucursal.setObjectName(u"txtNombreSucursal")
        self.txtNombreSucursal.setGeometry(QRect(70, 120, 131, 31))
        font3 = QFont()
        font3.setBold(True)
        font3.setKerning(True)
        self.txtNombreSucursal.setFont(font3)
        self.txtNombreSucursal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtNombreSucursal.setAlignment(Qt.AlignCenter)
        self.txtNombreSucursal.setReadOnly(False)
        self.lblNombreSucursal = QLabel(self.centralwidget)
        self.lblNombreSucursal.setObjectName(u"lblNombreSucursal")
        self.lblNombreSucursal.setGeometry(QRect(70, 100, 121, 20))
        self.lblNombreSucursal.setFont(font2)
        self.lblNombreSucursal.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.txtDireccionSucursal = QLineEdit(self.centralwidget)
        self.txtDireccionSucursal.setObjectName(u"txtDireccionSucursal")
        self.txtDireccionSucursal.setGeometry(QRect(340, 120, 131, 31))
        self.txtDireccionSucursal.setFont(font3)
        self.txtDireccionSucursal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtDireccionSucursal.setAlignment(Qt.AlignCenter)
        self.txtDireccionSucursal.setReadOnly(False)
        self.lblDepartamentoSucursal = QLabel(self.centralwidget)
        self.lblDepartamentoSucursal.setObjectName(u"lblDepartamentoSucursal")
        self.lblDepartamentoSucursal.setGeometry(QRect(340, 170, 101, 20))
        self.lblDepartamentoSucursal.setFont(font2)
        self.lblDepartamentoSucursal.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.txtDepartamentoSucursal = QLineEdit(self.centralwidget)
        self.txtDepartamentoSucursal.setObjectName(u"txtDepartamentoSucursal")
        self.txtDepartamentoSucursal.setGeometry(QRect(340, 190, 131, 31))
        self.txtDepartamentoSucursal.setFont(font3)
        self.txtDepartamentoSucursal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtDepartamentoSucursal.setAlignment(Qt.AlignCenter)
        self.txtDepartamentoSucursal.setReadOnly(False)
        self.txtMunicipioSucursal = QLineEdit(self.centralwidget)
        self.txtMunicipioSucursal.setObjectName(u"txtMunicipioSucursal")
        self.txtMunicipioSucursal.setGeometry(QRect(70, 190, 131, 31))
        self.txtMunicipioSucursal.setFont(font3)
        self.txtMunicipioSucursal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius: 4px\n"
"")
        self.txtMunicipioSucursal.setAlignment(Qt.AlignCenter)
        self.txtMunicipioSucursal.setReadOnly(False)
        self.lblMunicipioSucursal = QLabel(self.centralwidget)
        self.lblMunicipioSucursal.setObjectName(u"lblMunicipioSucursal")
        self.lblMunicipioSucursal.setGeometry(QRect(70, 170, 121, 20))
        self.lblMunicipioSucursal.setFont(font2)
        self.lblMunicipioSucursal.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.btnRegresar = QPushButton(self.centralwidget)
        self.btnRegresar.setObjectName(u"btnRegresar")
        self.btnRegresar.setGeometry(QRect(420, 270, 93, 28))
        self.btnRegresar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:8px\n"
"")
        self.btnCrearSucursal = QPushButton(self.centralwidget)
        self.btnCrearSucursal.setObjectName(u"btnCrearSucursal")
        self.btnCrearSucursal.setGeometry(QRect(320, 270, 93, 28))
        self.btnCrearSucursal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:8px\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registrar Sucursales", None))
        self.txtTittle.setText(QCoreApplication.translate("MainWindow", u"Registrar Sucursales", None))
        self.lblDireccion.setText(QCoreApplication.translate("MainWindow", u"Direccion", None))
        self.txtNombreSucursal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lblNombreSucursal.setText(QCoreApplication.translate("MainWindow", u"Nombre Sucursal", None))
        self.txtDireccionSucursal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.lblDepartamentoSucursal.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.txtDepartamentoSucursal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.txtMunicipioSucursal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.lblMunicipioSucursal.setText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.btnRegresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.btnCrearSucursal.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
    # retranslateUi

