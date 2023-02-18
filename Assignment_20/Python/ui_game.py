# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import game_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(348, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(20, 30, 151, 141))
        icon = QIcon()
        icon.addFile(u":/qrc1/hand1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_1.setIcon(icon)
        self.btn_1.setIconSize(QSize(100, 100))
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(180, 30, 151, 141))
        icon1 = QIcon()
        icon1.addFile(u":/qrc1/hand2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_2.setIcon(icon1)
        self.btn_2.setIconSize(QSize(100, 100))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 81, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 190, 81, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 390, 81, 16))
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setGeometry(QRect(100, 220, 151, 141))
        icon2 = QIcon()
        icon2.addFile(u":/qrc1/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_3.setIcon(icon2)
        self.btn_3.setIconSize(QSize(100, 100))
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setGeometry(QRect(100, 420, 151, 141))
        self.btn_4.setIcon(icon2)
        self.btn_4.setIconSize(QSize(100, 100))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_1.setText("")
        self.btn_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select one:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Computer 1:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Computer 2:", None))
        self.btn_3.setText("")
        self.btn_4.setText("")
    # retranslateUi

