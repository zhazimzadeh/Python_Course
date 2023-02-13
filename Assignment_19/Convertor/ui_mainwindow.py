# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convertor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(401, 187)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 387, 170))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.rdbtn_weight = QRadioButton(self.widget)
        self.rdbtn_weight.setObjectName(u"rdbtn_weight")

        self.gridLayout.addWidget(self.rdbtn_weight, 0, 1, 1, 1)

        self.rdbtn_lenght = QRadioButton(self.widget)
        self.rdbtn_lenght.setObjectName(u"rdbtn_lenght")

        self.gridLayout.addWidget(self.rdbtn_lenght, 0, 2, 1, 1)

        self.rdbtn_temp = QRadioButton(self.widget)
        self.rdbtn_temp.setObjectName(u"rdbtn_temp")

        self.gridLayout.addWidget(self.rdbtn_temp, 0, 3, 1, 1)

        self.rdbtn_digital = QRadioButton(self.widget)
        self.rdbtn_digital.setObjectName(u"rdbtn_digital")

        self.gridLayout.addWidget(self.rdbtn_digital, 0, 4, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.cmbx_from = QComboBox(self.widget)
        self.cmbx_from.setObjectName(u"cmbx_from")

        self.gridLayout.addWidget(self.cmbx_from, 1, 1, 1, 3)

        self.cmb_To = QComboBox(self.widget)
        self.cmb_To.setObjectName(u"cmb_To")

        self.gridLayout.addWidget(self.cmb_To, 2, 1, 1, 3)

        self.txt_Input = QLineEdit(self.widget)
        self.txt_Input.setObjectName(u"txt_Input")

        self.gridLayout.addWidget(self.txt_Input, 3, 1, 1, 3)

        self.btn_Convert = QPushButton(self.widget)
        self.btn_Convert.setObjectName(u"btn_Convert")
        self.btn_Convert.setStyleSheet(u"background-color: rgb(85, 255, 127);")

        self.gridLayout.addWidget(self.btn_Convert, 4, 1, 1, 3)

        self.txt_result = QLineEdit(self.widget)
        self.txt_result.setObjectName(u"txt_result")

        self.gridLayout.addWidget(self.txt_result, 5, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Convertor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Convert:", None))
        self.rdbtn_weight.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.rdbtn_lenght.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.rdbtn_temp.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.rdbtn_digital.setText(QCoreApplication.translate("MainWindow", u"Digital volume", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.cmbx_from.setCurrentText("")
        self.cmb_To.setCurrentText("")
        self.btn_Convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

