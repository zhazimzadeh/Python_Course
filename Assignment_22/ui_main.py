# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(318, 373)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grd_tasks = QGridLayout()
        self.grd_tasks.setObjectName(u"grd_tasks")

        self.verticalLayout.addLayout(self.grd_tasks)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.txt_newTask = QLineEdit(self.centralwidget)
        self.txt_newTask.setObjectName(u"txt_newTask")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_newTask.sizePolicy().hasHeightForWidth())
        self.txt_newTask.setSizePolicy(sizePolicy)
        self.txt_newTask.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.txt_newTask)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txt_priority = QLineEdit(self.centralwidget)
        self.txt_priority.setObjectName(u"txt_priority")
        sizePolicy.setHeightForWidth(self.txt_priority.sizePolicy().hasHeightForWidth())
        self.txt_priority.setSizePolicy(sizePolicy)
        self.txt_priority.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout.addWidget(self.txt_priority)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.txt_desc = QTextEdit(self.centralwidget)
        self.txt_desc.setObjectName(u"txt_desc")
        self.txt_desc.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.txt_desc)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout.addWidget(self.dateTimeEdit)

        self.btn_newTask = QPushButton(self.centralwidget)
        self.btn_newTask.setObjectName(u"btn_newTask")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_newTask.sizePolicy().hasHeightForWidth())
        self.btn_newTask.setSizePolicy(sizePolicy1)
        self.btn_newTask.setMinimumSize(QSize(300, 50))
        self.btn_newTask.setMaximumSize(QSize(65, 65))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_newTask.setFont(font)
        self.btn_newTask.setLayoutDirection(Qt.LeftToRight)
        self.btn_newTask.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(0, 170, 0);")

        self.verticalLayout.addWidget(self.btn_newTask)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 318, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Priority:(low<5   High>5)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Date  and Time:", None))
        self.btn_newTask.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

