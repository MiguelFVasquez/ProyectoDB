# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuTesoreria.ui'
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

class Ui_menuTesoreria(object):
    def setupUi(self, menuTesoreria):
        if not menuTesoreria.objectName():
            menuTesoreria.setObjectName(u"menuTesoreria")
        menuTesoreria.resize(555, 298)
        menuTesoreria.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(menuTesoreria)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.btnVerSolicitudes_2 = QPushButton(self.centralwidget)
        self.btnVerSolicitudes_2.setObjectName(u"btnVerSolicitudes_2")
        self.btnVerSolicitudes_2.setGeometry(QRect(150, 120, 101, 41))
        self.btnVerSolicitudes_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnVerSolicitudes_2.setFocusPolicy(Qt.ClickFocus)
        self.btnVerSolicitudes_2.setLayoutDirection(Qt.RightToLeft)
        self.btnVerSolicitudes_2.setAutoFillBackground(False)
        self.btnVerSolicitudes_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnGestionarSolicitudes = QPushButton(self.centralwidget)
        self.btnGestionarSolicitudes.setObjectName(u"btnGestionarSolicitudes")
        self.btnGestionarSolicitudes.setGeometry(QRect(140, 180, 121, 41))
        self.btnGestionarSolicitudes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGestionarSolicitudes.setFocusPolicy(Qt.ClickFocus)
        self.btnGestionarSolicitudes.setLayoutDirection(Qt.RightToLeft)
        self.btnGestionarSolicitudes.setAutoFillBackground(False)
        self.btnGestionarSolicitudes.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.lblTransacciones = QLabel(self.centralwidget)
        self.lblTransacciones.setObjectName(u"lblTransacciones")
        self.lblTransacciones.setEnabled(False)
        self.lblTransacciones.setGeometry(QRect(220, 70, 141, 41))
        font1 = QFont()
        font1.setPointSize(13)
        self.lblTransacciones.setFont(font1)
        self.lblTransacciones.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.btnVerSolicitudes = QPushButton(self.centralwidget)
        self.btnVerSolicitudes.setObjectName(u"btnVerSolicitudes")
        self.btnVerSolicitudes.setGeometry(QRect(340, 120, 101, 41))
        self.btnVerSolicitudes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnVerSolicitudes.setFocusPolicy(Qt.ClickFocus)
        self.btnVerSolicitudes.setLayoutDirection(Qt.RightToLeft)
        self.btnVerSolicitudes.setAutoFillBackground(False)
        self.btnVerSolicitudes.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnReportes = QPushButton(self.centralwidget)
        self.btnReportes.setObjectName(u"btnReportes")
        self.btnReportes.setGeometry(QRect(340, 180, 101, 41))
        self.btnReportes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnReportes.setFocusPolicy(Qt.ClickFocus)
        self.btnReportes.setLayoutDirection(Qt.RightToLeft)
        self.btnReportes.setAutoFillBackground(False)
        self.btnReportes.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(202, 253, 255);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        self.btnLogOut = QPushButton(self.centralwidget)
        self.btnLogOut.setObjectName(u"btnLogOut")
        self.btnLogOut.setGeometry(QRect(440, 260, 93, 28))
        self.btnLogOut.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogOut.setFocusPolicy(Qt.ClickFocus)
        self.btnLogOut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 99, 175);\n"
"border: 2px solid rgb(0, 0, 0);  \n"
"border-radius: 8px;  ")
        menuTesoreria.setCentralWidget(self.centralwidget)

        self.retranslateUi(menuTesoreria)

        QMetaObject.connectSlotsByName(menuTesoreria)
    # setupUi

    def retranslateUi(self, menuTesoreria):
        menuTesoreria.setWindowTitle(QCoreApplication.translate("menuTesoreria", u"MenuTesoreria", None))
        self.lblMenu.setText(QCoreApplication.translate("menuTesoreria", u"MENU", None))
        self.btnVerSolicitudes_2.setText(QCoreApplication.translate("menuTesoreria", u"Ver Solicitudes \n"
"Prestamos", None))
        self.btnGestionarSolicitudes.setText(QCoreApplication.translate("menuTesoreria", u"Gestionar solicitudes \n"
" de Prestamo", None))
        self.lblTransacciones.setText(QCoreApplication.translate("menuTesoreria", u"Transacciones", None))
        self.btnVerSolicitudes.setText(QCoreApplication.translate("menuTesoreria", u"Ver prestamos", None))
        self.btnReportes.setText(QCoreApplication.translate("menuTesoreria", u"Generar\n"
"Resportes", None))
        self.btnLogOut.setText(QCoreApplication.translate("menuTesoreria", u"Cerrar sesi\u00f3n", None))
    # retranslateUi

