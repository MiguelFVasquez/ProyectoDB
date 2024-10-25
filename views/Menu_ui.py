# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_menuWindow(object):
    def setupUi(self, menuWindow):
        if not menuWindow.objectName():
            menuWindow.setObjectName(u"menuWindow")
        menuWindow.resize(561, 317)
        font = QFont()
        font.setPointSize(10)
        menuWindow.setFont(font)
        menuWindow.setAutoFillBackground(False)
        menuWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        menuWindow.setAnimated(True)
        self.actionEmpleados = QAction(menuWindow)
        self.actionEmpleados.setObjectName(u"actionEmpleados")
        self.actionTesoreria = QAction(menuWindow)
        self.actionTesoreria.setObjectName(u"actionTesoreria")
        self.actionEntidadessEmpleado = QAction(menuWindow)
        self.actionEntidadessEmpleado.setObjectName(u"actionEntidadessEmpleado")
        font1 = QFont()
        self.actionEntidadessEmpleado.setFont(font1)
        self.actionEntidadeSucursales = QAction(menuWindow)
        self.actionEntidadeSucursales.setObjectName(u"actionEntidadeSucursales")
        self.centralwidget = QWidget(menuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnLogOut = QPushButton(self.centralwidget)
        self.btnLogOut.setObjectName(u"btnLogOut")
        self.btnLogOut.setGeometry(QRect(450, 270, 93, 28))
        self.btnLogOut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogOut.setFocusPolicy(Qt.ClickFocus)
        self.btnLogOut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnEmpleados = QPushButton(self.centralwidget)
        self.btnEmpleados.setObjectName(u"btnEmpleados")
        self.btnEmpleados.setGeometry(QRect(40, 190, 111, 41))
        self.btnEmpleados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnEmpleados.setFocusPolicy(Qt.ClickFocus)
        self.btnEmpleados.setAutoFillBackground(False)
        self.btnEmpleados.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.lblEntidades = QLabel(self.centralwidget)
        self.lblEntidades.setObjectName(u"lblEntidades")
        self.lblEntidades.setEnabled(False)
        self.lblEntidades.setGeometry(QRect(60, 80, 81, 41))
        font2 = QFont()
        font2.setPointSize(13)
        self.lblEntidades.setFont(font2)
        self.lblEntidades.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.btnPrestamos = QPushButton(self.centralwidget)
        self.btnPrestamos.setObjectName(u"btnPrestamos")
        self.btnPrestamos.setGeometry(QRect(220, 140, 101, 41))
        self.btnPrestamos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPrestamos.setFocusPolicy(Qt.ClickFocus)
        self.btnPrestamos.setLayoutDirection(Qt.RightToLeft)
        self.btnPrestamos.setAutoFillBackground(False)
        self.btnPrestamos.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.lblTransacciones = QLabel(self.centralwidget)
        self.lblTransacciones.setObjectName(u"lblTransacciones")
        self.lblTransacciones.setEnabled(False)
        self.lblTransacciones.setGeometry(QRect(210, 80, 141, 41))
        self.lblTransacciones.setFont(font2)
        self.lblTransacciones.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.btnReportes = QPushButton(self.centralwidget)
        self.btnReportes.setObjectName(u"btnReportes")
        self.btnReportes.setGeometry(QRect(390, 140, 101, 41))
        self.btnReportes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnReportes.setFocusPolicy(Qt.ClickFocus)
        self.btnReportes.setLayoutDirection(Qt.RightToLeft)
        self.btnReportes.setAutoFillBackground(False)
        self.btnReportes.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.lblInformacion = QLabel(self.centralwidget)
        self.lblInformacion.setObjectName(u"lblInformacion")
        self.lblInformacion.setEnabled(False)
        self.lblInformacion.setGeometry(QRect(390, 80, 121, 41))
        self.lblInformacion.setFont(font2)
        self.lblInformacion.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.lblInformacion.setWordWrap(True)
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
        self.lblMenu.setGeometry(QRect(240, 10, 81, 41))
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
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.lblMenu.setFont(font3)
        self.lblMenu.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lblMenu.setAutoFillBackground(False)
        self.lblMenu.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.btnCrearEmpleados = QPushButton(self.centralwidget)
        self.btnCrearEmpleados.setObjectName(u"btnCrearEmpleados")
        self.btnCrearEmpleados.setGeometry(QRect(40, 140, 111, 41))
        self.btnCrearEmpleados.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCrearEmpleados.setFocusPolicy(Qt.ClickFocus)
        self.btnCrearEmpleados.setAutoFillBackground(False)
        self.btnCrearEmpleados.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnCrearSucursales = QPushButton(self.centralwidget)
        self.btnCrearSucursales.setObjectName(u"btnCrearSucursales")
        self.btnCrearSucursales.setGeometry(QRect(220, 190, 101, 41))
        self.btnCrearSucursales.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCrearSucursales.setFocusPolicy(Qt.ClickFocus)
        self.btnCrearSucursales.setLayoutDirection(Qt.RightToLeft)
        self.btnCrearSucursales.setAutoFillBackground(False)
        self.btnCrearSucursales.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        menuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(menuWindow)

        QMetaObject.connectSlotsByName(menuWindow)
    # setupUi

    def retranslateUi(self, menuWindow):
        menuWindow.setWindowTitle(QCoreApplication.translate("menuWindow", u"Menu", None))
        self.actionEmpleados.setText(QCoreApplication.translate("menuWindow", u"Empleados", None))
        self.actionTesoreria.setText(QCoreApplication.translate("menuWindow", u"Sucursales", None))
        self.actionEntidadessEmpleado.setText(QCoreApplication.translate("menuWindow", u"Empleados", None))
        self.actionEntidadeSucursales.setText(QCoreApplication.translate("menuWindow", u"Sucursales", None))
        self.btnLogOut.setText(QCoreApplication.translate("menuWindow", u"Cerrar sesi\u00f3n", None))
        self.btnEmpleados.setText(QCoreApplication.translate("menuWindow", u"Ver usuarios", None))
        self.lblEntidades.setText(QCoreApplication.translate("menuWindow", u"Usuario", None))
        self.btnPrestamos.setText(QCoreApplication.translate("menuWindow", u"Ver Auditorias\n"
" de Acceso", None))
        self.lblTransacciones.setText(QCoreApplication.translate("menuWindow", u"Transacciones", None))
        self.btnReportes.setText(QCoreApplication.translate("menuWindow", u"Resportes", None))
        self.lblInformacion.setText(QCoreApplication.translate("menuWindow", u"Informacion", None))
        self.lblMenu.setText(QCoreApplication.translate("menuWindow", u"MENU", None))
        self.btnCrearEmpleados.setText(QCoreApplication.translate("menuWindow", u"Crear usuarios", None))
        self.btnCrearSucursales.setText(QCoreApplication.translate("menuWindow", u"Crear Sucursal", None))
    # retranslateUi

