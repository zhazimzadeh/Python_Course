# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_MyTranslator(object):
    def setupUi(self, MyTranslator):
        if not MyTranslator.objectName():
            MyTranslator.setObjectName(u"MyTranslator")
        MyTranslator.resize(438, 217)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(MyTranslator.sizePolicy().hasHeightForWidth())
        MyTranslator.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"C:/Users/Jila/Downloads/google.png", QSize(), QIcon.Normal, QIcon.Off)
        MyTranslator.setWindowIcon(icon)
        self.centralwidget = QWidget(MyTranslator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 1, 431, 211))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_Del = QPushButton(self.widget)
        self.btn_Del.setObjectName(u"btn_Del")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.btn_Del.sizePolicy().hasHeightForWidth())
        self.btn_Del.setSizePolicy(sizePolicy1)
        self.btn_Del.setMinimumSize(QSize(0, 0))
        self.btn_Del.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.btn_Del)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rdbtn_engToper = QRadioButton(self.widget)
        self.rdbtn_engToper.setObjectName(u"rdbtn_engToper")
        self.rdbtn_engToper.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.rdbtn_engToper.setChecked(True)

        self.horizontalLayout.addWidget(self.rdbtn_engToper)

        self.rdbtn_perToeng = QRadioButton(self.widget)
        self.rdbtn_perToeng.setObjectName(u"rdbtn_perToeng")
        self.rdbtn_perToeng.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")
        self.rdbtn_perToeng.setChecked(False)

        self.horizontalLayout.addWidget(self.rdbtn_perToeng)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.txt_Source = QLineEdit(self.widget)
        self.txt_Source.setObjectName(u"txt_Source")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(50)
        sizePolicy2.setVerticalStretch(50)
        sizePolicy2.setHeightForWidth(self.txt_Source.sizePolicy().hasHeightForWidth())
        self.txt_Source.setSizePolicy(sizePolicy2)
        self.txt_Source.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.txt_Source)

        self.txt_translate = QLineEdit(self.widget)
        self.txt_translate.setObjectName(u"txt_translate")
        sizePolicy2.setHeightForWidth(self.txt_translate.sizePolicy().hasHeightForWidth())
        self.txt_translate.setSizePolicy(sizePolicy2)
        self.txt_translate.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.txt_translate)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(100)
        sizePolicy3.setVerticalStretch(100)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.txt_En = QLineEdit(self.groupBox)
        self.txt_En.setObjectName(u"txt_En")
        self.txt_En.setGeometry(QRect(10, 20, 113, 22))
        self.txt_Fa = QLineEdit(self.groupBox)
        self.txt_Fa.setObjectName(u"txt_Fa")
        self.txt_Fa.setGeometry(QRect(160, 20, 113, 22))
        self.btn_Add = QPushButton(self.groupBox)
        self.btn_Add.setObjectName(u"btn_Add")
        self.btn_Add.setGeometry(QRect(300, 20, 121, 24))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(135, 20, 16, 16))
        self.label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 0, 61, 20))
        self.label_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 0, 61, 16))
        self.label_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.groupBox)

        self.btn_Translate = QPushButton(self.widget)
        self.btn_Translate.setObjectName(u"btn_Translate")
        sizePolicy1.setHeightForWidth(self.btn_Translate.sizePolicy().hasHeightForWidth())
        self.btn_Translate.setSizePolicy(sizePolicy1)
        self.btn_Translate.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"background-color: rgb(0, 255, 127);")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.btn_Translate)

        MyTranslator.setCentralWidget(self.centralwidget)

        self.retranslateUi(MyTranslator)

        QMetaObject.connectSlotsByName(MyTranslator)
    # setupUi

    def retranslateUi(self, MyTranslator):
        MyTranslator.setWindowTitle(QCoreApplication.translate("MyTranslator", u"My Translator", None))
        self.btn_Del.setText(QCoreApplication.translate("MyTranslator", u"X", None))
        self.rdbtn_engToper.setText(QCoreApplication.translate("MyTranslator", u"English to Persian", None))
        self.rdbtn_perToeng.setText(QCoreApplication.translate("MyTranslator", u"Persian to English", None))
        self.groupBox.setTitle("")
        self.btn_Add.setText(QCoreApplication.translate("MyTranslator", u"Add New Words", None))
        self.label.setText(QCoreApplication.translate("MyTranslator", u"=", None))
        self.label_2.setText(QCoreApplication.translate("MyTranslator", u"English", None))
        self.label_3.setText(QCoreApplication.translate("MyTranslator", u"Persian", None))
        self.btn_Translate.setText(QCoreApplication.translate("MyTranslator", u"Translate", None))
    # retranslateUi

