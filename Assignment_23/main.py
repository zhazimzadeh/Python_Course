import sys
import random
from sudoku import Sudoku
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_openfile.triggered.connect(self.open_file)
        self.line_edits=[[None for i in range(9)]  for j in range(9)] 
        self.readonly_cells = []
        for i in range(9):
            for j in range(9):
                new_cell=QLineEdit()
                new_cell.setFixedSize(45,45)
                new_cell.setStyleSheet("font: 700 12pt "+"Segoe UI")
                new_cell.setAlignment(Qt.AlignCenter)
                self.ui.grd_main.addWidget(new_cell,i,j)
                new_cell.textChanged.connect(partial(self.validation,i,j))
                self.line_edits[i][j]=new_cell

        self.new_game()

    def new_game(self):
        puzzle=Sudoku(3, seed=random.randint(1,1000)).difficulty(0.5) 
        self.readonly_cells.clear()
        for i in range(9):
            for j in range(9): 
                self.line_edits[i][j].setReadOnly(False) 
                if puzzle.board[i][j] !=None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)  
                    self.readonly_cells.append([i,j])  
                else:     
                    self.line_edits[i][j].setText("") 
                   
                    
    def open_file(self):
        x=QFileDialog.getOpenFileName(self,"Open File ...")[0]
        f=open(x,"r")
        big_text=f.read()
        rows=big_text.split("\n")
        puzzle_board=[[None for i in range(9)] for j in range(9)]
        self.readonly_cells.clear()
        for i in range (len(rows)):
            cells=rows[i].split(" ")
            for j in range(len(cells)):
                puzzle_board[i][j]=int(cells[j])

        for i in range(9):
            for j in range(9): 
                self.line_edits[i][j].setReadOnly(False)
                if puzzle_board[i][j] !=0:
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)  
                    self.readonly_cells.append([i,j]) 
                else:     
                    self.line_edits[i][j].setText("") 

    def check(self,i=-1,j=-1):
        self.reset_Sheet()
        for i in range(9):
            for j in range(9):
                num1 = self.line_edits[i][j].text()
                if num1 == '':
                    return False
                elif [i,j] in self.readonly_cells:
                    self.line_edits[i][j].setStyleSheet('color: rgb(255, 85, 255);')
                for i_9 in range(i+1,9):
                    num2 = self.line_edits[i_9][j].text()
                    if num1 == num2 and num2 != '':
                        self.false_number(i,j)
                        self.false_number(i_9,j)
                        return False

                for j_9 in range(j+1,9):
                    num2 = self.line_edits[i][j_9].text()
                    if num1 == num2 and num2 != '':
                        self.false_number(i,j)
                        self.false_number(i,j_9)
                        return False

        for n in range(0, 9, 3):
            for m in range(0, 9, 3):
                for i in range(n, n + 3):
                    for j in range(m, m + 3):
                        num1 = self.line_edits[i][j].text()
                        for i_3 in range(n, n + 3):
                            for j_3 in range(m, m +3):
                                num2 = self.line_edits[i_3][i_3].text()
                                if num1 == num2 and num2 != '' and not (i == i_3 and j == j_3):
                                    self.false_number(i,j)
                                    self.false_number(i_3,j_3)
                                    return False

            
                                    
        return True
    def reset_Sheet(self):
        self.setStyleSheet('')
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setStyleSheet('')

    def validation(self, i, j,text):
        # text=self.line_edits[i][j].text()
        if text not in ["1","2","3","4","5","6","7","8","9"]:
            self.line_edits[i][j].setText("")
        if self.check(i,j):
                msg_box = QMessageBox()
                msg_box.setText('You are win!')
                msg_box.setWindowTitle('Win')
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.exec()
    
    def false_number(self,i,j):
        if [i,j] not in self.readonly_cells:
            self.line_edits[i][j].setStyleSheet('background-color: rgb(255, 215, 203)')
        else:
            self.line_edits[i][j].setStyleSheet('background-color: rgb(255, 0, 0);')




if __name__== "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()