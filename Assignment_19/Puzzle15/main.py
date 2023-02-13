import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons=[[self.ui.btn_1,self.ui.btn_2,self.ui.btn_3,self.ui.btn_4],
                    [self.ui.btn_5,self.ui.btn_6,self.ui.btn_7,self.ui.btn_8],
                    [self.ui.btn_9,self.ui.btn_10,self.ui.btn_11,self.ui.btn_12],
                    [self.ui.btn_13,self.ui.btn_14,self.ui.btn_15,self.ui.btn_16],]
        numbers=[]
        for i in range(0,4):
            for j in range(0,4):
                r=random.randint(1,16)
                while r in numbers:
                    r=random.randint(1,16)
                numbers.append(r)
                if r==16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i=i
                    self.empty_j=j
                else:
                    self.buttons[i][j].setText(str(r))
                
                self.buttons[i][j].clicked.connect(partial(self.play,i,j))
    
    def play(self,i,j):
        if (i==self.empty_i and (j==self.empty_j-1 or j==self.empty_j+1)) \
        or (j==self.empty_j and (i==self.empty_i-1 or i==self.empty_i+1)):

            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setText("16")
            self.buttons[i][j].setVisible(False)
            self.empty_i=i
            self.empty_j=j
            
        else:
            pass
    
        if self.check_win()==True:
            msgBox=QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setText("You Win!")
            msgBox.exec_()
            


    def check_win(self):
        index=1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text())!=index:
                    return False
                index+=1

        return True

                



my_app=QApplication(sys.argv)
My_Window=MainWindow()
My_Window.show()


my_app.exec()
