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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(447, 361)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, -1, 441, 361))
        self.tabWidget.setStyleSheet(u"background-color: rgb(79, 79, 79);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 91, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 150, 121, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 230, 101, 20))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.lbl_timeIR = QLabel(self.tab)
        self.lbl_timeIR.setObjectName(u"lbl_timeIR")
        self.lbl_timeIR.setGeometry(QRect(190, 70, 221, 20))
        font1 = QFont()
        font1.setFamilies([u"Seven Segment"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.lbl_timeIR.setFont(font1)
        self.lbl_timeIR.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"Seven Segment\";")
        self.lbl_timeDE = QLabel(self.tab)
        self.lbl_timeDE.setObjectName(u"lbl_timeDE")
        self.lbl_timeDE.setGeometry(QRect(190, 150, 221, 20))
        self.lbl_timeDE.setFont(font1)
        self.lbl_timeDE.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"Seven Segment\";")
        self.lbl_timeUS = QLabel(self.tab)
        self.lbl_timeUS.setObjectName(u"lbl_timeUS")
        self.lbl_timeUS.setGeometry(QRect(190, 230, 221, 20))
        self.lbl_timeUS.setFont(font1)
        self.lbl_timeUS.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"Seven Segment\";")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.btn_add_alarm = QPushButton(self.tab_2)
        self.btn_add_alarm.setObjectName(u"btn_add_alarm")
        self.btn_add_alarm.setGeometry(QRect(20, 180, 81, 41))
        self.btn_add_alarm.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius:15px;\n"
"")
        self.txt_min_Alarm = QLineEdit(self.tab_2)
        self.txt_min_Alarm.setObjectName(u"txt_min_Alarm")
        self.txt_min_Alarm.setGeometry(QRect(90, 30, 51, 51))
        self.txt_min_Alarm.setStyleSheet(u"font: 20pt \"Seven Segment\";\n"
"color: rgb(255, 255, 255);")
        self.txt_min_Alarm.setAlignment(Qt.AlignCenter)
        self.txt_hour_Alarm = QLineEdit(self.tab_2)
        self.txt_hour_Alarm.setObjectName(u"txt_hour_Alarm")
        self.txt_hour_Alarm.setGeometry(QRect(20, 30, 51, 51))
        self.txt_hour_Alarm.setStyleSheet(u"font: 20pt \"Seven Segment\";\n"
"color: rgb(255, 255, 255);")
        self.txt_hour_Alarm.setAlignment(Qt.AlignCenter)
        self.txt_sec_Alarm = QLineEdit(self.tab_2)
        self.txt_sec_Alarm.setObjectName(u"txt_sec_Alarm")
        self.txt_sec_Alarm.setGeometry(QRect(160, 30, 51, 51))
        self.txt_sec_Alarm.setStyleSheet(u"font: 20pt \"Seven Segment\";\n"
"color: rgb(255, 255, 255);")
        self.txt_sec_Alarm.setAlignment(Qt.AlignCenter)
        self.btn_edit_alarm = QPushButton(self.tab_2)
        self.btn_edit_alarm.setObjectName(u"btn_edit_alarm")
        self.btn_edit_alarm.setGeometry(QRect(20, 230, 81, 41))
        self.btn_edit_alarm.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 15px;\n"
"")
        self.txt_alarm_desc = QLineEdit(self.tab_2)
        self.txt_alarm_desc.setObjectName(u"txt_alarm_desc")
        self.txt_alarm_desc.setGeometry(QRect(20, 130, 191, 41))
        self.txt_alarm_desc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 91, 16))
        self.label_4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(230, 0, 201, 331))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(140, 170, 75, 71))
        self.btn_start_stopwatch.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius:25px;\n"
"")
        self.lbl_stopwatch = QLabel(self.tab_3)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(170, 100, 111, 41))
        self.lbl_stopwatch.setStyleSheet(u"\n"
"font: 20pt \"Seven Segment\";\n"
"color: rgb(255, 255, 255);")
        self.lbl_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(230, 170, 75, 71))
        self.btn_stop_stopwatch.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 25px;\n"
"")
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(140, 20, 161, 41))
        self.btn_reset_stopwatch.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 15px;\n"
"")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.txt_hour_timer = QLineEdit(self.tab_4)
        self.txt_hour_timer.setObjectName(u"txt_hour_timer")
        self.txt_hour_timer.setGeometry(QRect(110, 80, 61, 71))
        self.txt_hour_timer.setStyleSheet(u"font: 20pt \"Seven Segment\";\n"
"color: rgb(255, 255, 255);")
        self.txt_hour_timer.setAlignment(Qt.AlignCenter)
        self.txt_min_timer = QLineEdit(self.tab_4)
        self.txt_min_timer.setObjectName(u"txt_min_timer")
        self.txt_min_timer.setGeometry(QRect(180, 80, 61, 71))
        self.txt_min_timer.setStyleSheet(u"font: 20pt \"Seven Segment\";\n"
"color: rgb(255, 255, 255);")
        self.txt_min_timer.setAlignment(Qt.AlignCenter)
        self.txt_sec_timer = QLineEdit(self.tab_4)
        self.txt_sec_timer.setObjectName(u"txt_sec_timer")
        self.txt_sec_timer.setGeometry(QRect(250, 80, 61, 71))
        self.txt_sec_timer.setStyleSheet(u"font: 20pt \"Seven Segment\";\n"
"color: rgb(255, 255, 255);")
        self.txt_sec_timer.setAlignment(Qt.AlignCenter)
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(220, 180, 75, 71))
        self.btn_stop_timer.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 25px;\n"
"")
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(130, 10, 161, 41))
        self.btn_reset_timer.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius: 15px;\n"
"")
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(130, 180, 75, 71))
        self.btn_start_timer.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-radius:25px;\n"
"")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IR (Iran)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DE (Germany)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"US (USA)", None))
        self.lbl_timeIR.setText("")
        self.lbl_timeDE.setText("")
        self.lbl_timeUS.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.btn_add_alarm.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.txt_min_Alarm.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_hour_Alarm.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_sec_Alarm.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_edit_alarm.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.txt_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_min_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.txt_sec_timer.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

