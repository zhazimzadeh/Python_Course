import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtUiTools import QUiLoader


player=1
flg_enable=1
cnt=0
p1_win=0
p2_win=0
p_equal=0



def Status_check():
    flg_win=0
    for i in range(3):
        if(cells[i][0].text()!="" and cells[i][1].text()!="" and cells[i][2].text()!="" and
           cells[i][0].text()== cells[i][1].text()==cells[i][2].text() or
           cells[0][i].text()!="" and cells[1][i].text()!="" and cells[2][i].text()!="" and            
           cells[0][i].text()== cells[1][i].text()==cells[2][i].text() ):        
                flg_win=1
                break

    if(flg_win==0):
        if( cells[1][1].text()!= ""):
                if(cells[0][0].text()== cells[1][1].text()==cells[2][2].text() or 
                    cells[0][2].text()== cells[1][1].text()==cells[2][0].text() ):
                    flg_win=1
    return flg_win

def play(row,col):
    global player,flg_enable,cnt,p1_win,p2_win,p_equal
    
    if flg_enable:
        if ( cells[row][col].text()!=""):
            msgBox=QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("This cell was filled. Choose an empty cell!")
            msgBox.exec_()
            return
            
        if player==1:
            cells[row][col].setText('X')
            cells[row][col].setStyleSheet("color: rgb(255, 255, 0)")
        else :
            cells[row][col].setText('O')
            cells[row][col].setStyleSheet("color: rgb(170, 0, 255)")
        
        cnt+=1
        print(cnt)
        if(cnt>2 and cnt<10):
            if(Status_check()):
                msgBox=QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle("Congratulation")
                if(player==1):
                    msgBox.setText("Player 1 Win!")
                    p1_win+=1
                else:
                    msgBox.setText("Player 2 Win!")
                    p2_win+=1
                flg_enable=0
                msgBox.exec_()
                
            elif(cnt==9):
                msgBox=QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle("Finish")
                msgBox.setText("No one Wins!")
                p_equal+=1
                flg_enable=0
                msgBox.exec_()
                
        player*=-1

        if(flg_enable==1 and My_Window.rbtn_PCpu.isChecked()==True):
            if(player==-1):
                row=random.randint(0,2)
                col=random.randint(0,2)
                while ( cells[row][col].text()!=""):
                    row=random.randint(0,2)
                    col=random.randint(0,2)
                play(row,col)
                    


        My_Window.txtP1_win.setText(str(p1_win))
        My_Window.txtP1_loss.setText(str(p2_win))
        My_Window.txtP1_equal.setText(str(p_equal))
        My_Window.txtP2_win.setText(str(p2_win))
        My_Window.txtP2_loss.setText(str(p1_win))
        My_Window.txtP2_equal.setText(str(p_equal))
             
    else:
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Finish")
        msgBox.setText("The Game Was Finished!")
        msgBox.exec_()

        
def newGame():
    global cnt,flg_enable,player
    for i in range(0,3):
        for j in range(0,3):
            cells[i][j].setText("")
    cnt=0
    flg_enable=1
    player=1
    
def about():
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("About")
        msgBox.setText("This Game is implemented by PySide6!")
        msgBox.exec_()


my_app=QApplication(sys.argv)
loader=QUiLoader()
My_Window=loader.load("Python_Course\Assignment_18\TicTacToe.ui")
My_Window.show()

cells=[[My_Window.btn_1,My_Window.btn_2,My_Window.btn_3],
       [My_Window.btn_4,My_Window.btn_5,My_Window.btn_6],
       [My_Window.btn_7,My_Window.btn_8,My_Window.btn_9]]


     
for i in range(0,3):
        for j in range(0,3):
            cells[i][j].clicked.connect(partial(play,i,j))



My_Window.btn_NewGame.clicked.connect(newGame)
My_Window.rbtn_PCpu.toggled.connect(newGame)
My_Window.rbtn_P1P2.toggled.connect(newGame)
My_Window.btn_about.clicked.connect(about)

my_app.exec()