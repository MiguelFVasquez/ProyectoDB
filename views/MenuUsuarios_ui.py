# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuUsuarios.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_menuUsuarios(object):
    def setupUi(self, menuUsuarios):
        if not menuUsuarios.objectName():
            menuUsuarios.setObjectName(u"menuUsuarios")
        menuUsuarios.resize(552, 315)
        menuUsuarios.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(menuUsuarios)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCuotas = QPushButton(self.centralwidget)
        self.btnCuotas.setObjectName(u"btnCuotas")
        self.btnCuotas.setGeometry(QRect(230, 140, 101, 41))
        self.btnCuotas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCuotas.setFocusPolicy(Qt.ClickFocus)
        self.btnCuotas.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnPrestamos = QPushButton(self.centralwidget)
        self.btnPrestamos.setObjectName(u"btnPrestamos")
        self.btnPrestamos.setGeometry(QRect(70, 140, 101, 41))
        self.btnPrestamos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrestamos.setFocusPolicy(Qt.ClickFocus)
        self.btnPrestamos.setLayoutDirection(Qt.RightToLeft)
        self.btnPrestamos.setAutoFillBackground(False)
        self.btnPrestamos.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 561, 51))
        self.frame.setStyleSheet(u"background-color: rgb(37, 99, 175);\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(3)
        self.lblMenu = QLabel(self.frame)
        self.lblMenu.setObjectName(u"lblMenu")
        self.lblMenu.setEnabled(False)
        self.lblMenu.setGeometry(QRect(250, 10, 81, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lblMenu.setPalette(palette)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lblMenu.setFont(font)
        self.lblMenu.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lblMenu.setAutoFillBackground(False)
        self.lblMenu.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.btnVerSolicitudes = QPushButton(self.centralwidget)
        self.btnVerSolicitudes.setObjectName(u"btnVerSolicitudes")
        self.btnVerSolicitudes.setGeometry(QRect(70, 200, 101, 41))
        self.btnVerSolicitudes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnVerSolicitudes.setFocusPolicy(Qt.ClickFocus)
        self.btnVerSolicitudes.setLayoutDirection(Qt.RightToLeft)
        self.btnVerSolicitudes.setAutoFillBackground(False)
        self.btnVerSolicitudes.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.lblTransacciones = QLabel(self.centralwidget)
        self.lblTransacciones.setObjectName(u"lblTransacciones")
        self.lblTransacciones.setEnabled(False)
        self.lblTransacciones.setGeometry(QRect(50, 90, 141, 41))
        font1 = QFont()
        font1.setPointSize(13)
        self.lblTransacciones.setFont(font1)
        self.lblTransacciones.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.lblPagos = QLabel(self.centralwidget)
        self.lblPagos.setObjectName(u"lblPagos")
        self.lblPagos.setEnabled(False)
        self.lblPagos.setGeometry(QRect(250, 90, 61, 41))
        self.lblPagos.setFont(font1)
        self.lblPagos.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.lblInformacion_2 = QLabel(self.centralwidget)
        self.lblInformacion_2.setObjectName(u"lblInformacion_2")
        self.lblInformacion_2.setEnabled(False)
        self.lblInformacion_2.setGeometry(QRect(380, 90, 121, 41))
        self.lblInformacion_2.setFont(font1)
        self.lblInformacion_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.lblInformacion_2.setWordWrap(True)
        self.btnConsultas = QPushButton(self.centralwidget)
        self.btnConsultas.setObjectName(u"btnConsultas")
        self.btnConsultas.setGeometry(QRect(380, 140, 101, 41))
        self.btnConsultas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnConsultas.setFocusPolicy(Qt.ClickFocus)
        self.btnConsultas.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnLogOut = QPushButton(self.centralwidget)
        self.btnLogOut.setObjectName(u"btnLogOut")
        self.btnLogOut.setGeometry(QRect(430, 260, 93, 28))
        self.btnLogOut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogOut.setFocusPolicy(Qt.ClickFocus)
        self.btnLogOut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        menuUsuarios.setCentralWidget(self.centralwidget)

        self.retranslateUi(menuUsuarios)

        QMetaObject.connectSlotsByName(menuUsuarios)
    # setupUi

    def retranslateUi(self, menuUsuarios):
        menuUsuarios.setWindowTitle(QCoreApplication.translate("menuUsuarios", u"MenuUsuarios", None))
        self.btnCuotas.setText(QCoreApplication.translate("menuUsuarios", u"Gestion de\n"
"Cuotas", None))
        self.btnPrestamos.setText(QCoreApplication.translate("menuUsuarios", u"Solicitar \n"
"Prestamos", None))
        self.lblMenu.setText(QCoreApplication.translate("menuUsuarios", u"MENU", None))
        self.btnVerSolicitudes.setText(QCoreApplication.translate("menuUsuarios", u"Ver solicitudes", None))
        self.lblTransacciones.setText(QCoreApplication.translate("menuUsuarios", u"Transacciones", None))
        self.lblPagos.setText(QCoreApplication.translate("menuUsuarios", u"Pagos", None))
        self.lblInformacion_2.setText(QCoreApplication.translate("menuUsuarios", u"Informacion", None))
        self.btnConsultas.setText(QCoreApplication.translate("menuUsuarios", u"Historial de \n"
"prestamos", None))
        self.btnLogOut.setText(QCoreApplication.translate("menuUsuarios", u"Cerrar sesi\u00f3n", None))
    # retranslateUi

