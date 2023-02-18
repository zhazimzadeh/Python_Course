import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtUiTools import QUiLoader
from ui_game import Ui_MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

import game_qrc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.user=1
        self.comp_1=1
        self.comp_2=1

        # self.icon1 = QtGui.QIcon(":/qrc1/hand1.png")
        # self.icon2 = QtGui.QIcon(":/qrc1/hand2.png")
        # self.icon3 = QtGui.QIcon(":/qrc1/question.png")
        # self.ui.btn_1.setIcon(self.icon1)
        # self.ui.btn_2.setIcon(self.icon2)
        # self.ui.btn_3.setIcon(self.icon3)
        # self.ui.btn_4.setIcon(self.icon3)
        self.ui.btn_1.clicked.connect(partial(self.select,1))
        self.ui.btn_2.clicked.connect(partial(self.select,2))

    def select(self,opt):

        print("salam")
        if(opt==1):
            self.user=1
            self.ui.btn_2.setVisible(False)
            icon = QIcon()
            icon.addFile(u":/qrc1/hand1.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_1.setIcon(icon)
            self.ui.btn_1.setIconSize(QSize(100, 100))
        else:
            self.user=2
            self.ui.btn_1.setVisible(False)
            self.ui.btn_2.setIcon(self.icon2)

        if(random.choice(1,2)==1):
            self.ui.btn_3.setIcon("")
            self.ui.btn_2.setIcon(self.icon1)
        else:
            self.ui.btn_2.setIcon(self.icon2)

        if(random.choice(1,2)==1):
            self.ui.btn_2.setIcon(self.icon2)
        else:
            self.ui.btn_2.setIcon(self.icon2)

# user=1
# comp_1=1
# comp_2=1
# def select(opt):
#     global user,comp_1,comp_2
#     if(opt==1):
#             user=1
#             My_Window.btn_2.setVisible=False

#     else:
#             user=2
#             My_Window.btn_1.setVisible=False


my_app=QApplication(sys.argv)
loader=QUiLoader()
My_Window=loader.load("Assignment_20\Python\game.ui")
My_Window.show()


# My_Window.btn_1.clicked.connect(partial(select,1))

my_app.exec()