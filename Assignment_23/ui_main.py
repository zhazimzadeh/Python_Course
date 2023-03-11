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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 514)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_openfile = QAction(MainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.menu_help = QAction(MainWindow)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_about = QAction(MainWindow)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.menu_dark = QAction(MainWindow)
        self.menu_dark.setObjectName(u"menu_dark")
        self.menu_light = QAction(MainWindow)
        self.menu_light.setObjectName(u"menu_light")
        self.menu_solve = QAction(MainWindow)
        self.menu_solve.setObjectName(u"menu_solve")
        self.menu_help_2 = QAction(MainWindow)
        self.menu_help_2.setObjectName(u"menu_help_2")
        self.menu_about_2 = QAction(MainWindow)
        self.menu_about_2.setObjectName(u"menu_about_2")
        self.menu_exit_2 = QAction(MainWindow)
        self.menu_exit_2.setObjectName(u"menu_exit_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 541, 471))
        self.grd_main = QGridLayout(self.gridLayoutWidget)
        self.grd_main.setObjectName(u"grd_main")
        self.grd_main.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuTheme = QMenu(self.menubar)
        self.menuTheme.setObjectName(u"menuTheme")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addAction(self.menu_openfile)
        self.menuGame.addAction(self.menu_solve)
        self.menuGame.addAction(self.menu_exit_2)
        self.menuTheme.addAction(self.menu_dark)
        self.menuTheme.addAction(self.menu_light)
        self.menuHelp.addAction(self.menu_help_2)
        self.menuHelp.addAction(self.menu_about_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.menu_openfile.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.menu_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_dark.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.menu_light.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.menu_solve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.menu_help_2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_about_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_exit_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

