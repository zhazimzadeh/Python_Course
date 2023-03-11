import sys
import random
from sudoku import Sudoku
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


from ui_main import Ui_MainWindow
mode_dark=0
check=1
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_openfile.triggered.connect(self.open_file)
        self.ui.menu_about_2.triggered.connect(self.about)
        self.ui.menu_help_2.triggered.connect(self.help)
        self.ui.menu_exit_2.triggered.connect(self.exit_game)
        self.ui.menu_dark.triggered.connect(partial(self.theme,'rgb(59, 59, 59)','rgb(255, 255, 255)'))
        self.ui.menu_light.triggered.connect(partial(self.theme,'rgb(255, 255, 255)','rgb(0, 0, 0)'))

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
        self.ui.menu_solve.triggered.connect(self.solving)

    def new_game(self):
        global mode_dark
        if mode_dark==0: self.reset_Sheet()
        else:
            self.theme('rgb(59, 59, 59)','rgb(255, 255, 255)')
        self.puzzle=Sudoku(3, seed=random.randint(1,1000)).difficulty(0.5) 
        self.readonly_cells.clear()
        for i in range(9):
            for j in range(9): 
                self.line_edits[i][j].setReadOnly(False) 
                if self.puzzle.board[i][j] !=None:
                    self.line_edits[i][j].setText(str(self.puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)  
                    self.readonly_cells.append([i,j])  
                else:     
                    self.line_edits[i][j].setText("") 
    def error_file(self):
            msg_box = QMessageBox()
            msg_box.setText('File is not valid. \nThe valid file is a text file with 9*9 numbers between 1-9 \n and numbers must be seperated by one Space ')
            msg_box.setWindowTitle('Error')
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.exec()

    def open_file(self):
        try:
            x=QFileDialog.getOpenFileName(self,"Open File ...")[0]
            f=open(x,"r")
            big_text=f.read()
            rows=big_text.split("\n")
            puzzle_board=[[None for i in range(9)] for j in range(9)]
            self.readonly_cells.clear()
            if len(rows)<9 or len(rows)>9:
                self.error_file()
                return 0
            for i in range (len(rows)):
                cells=rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j]=int(cells[j])
        except:
            self.error_file()



        for i in range(9):
            for j in range(9): 
                self.line_edits[i][j].setReadOnly(False)
                if puzzle_board[i][j] !=0:
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)  
                    self.readonly_cells.append([i,j]) 
                else:     
                    self.line_edits[i][j].setText("") 

    def about(self):
        msg_box = QMessageBox()
        msg_box.setText('This game is written by Jila as an assignment!')
        msg_box.setWindowTitle('About')
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()

    def help(self):
        msg_box = QMessageBox()
        msg_box.setText('How to play sudoku:\n  A 9×9 square must be filled in with numbers from 1-9 \n with no repeated numbers in each line, horizontally or vertically. \n To challenge you more, there are 3×3 squares marked out in the grid,\n and each of these squares can not have any repeat numbers either')
        msg_box.setWindowTitle('How to play?')
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()

    def exit_game(self):
        exit(0)

    def theme(self,back_color,font_color):
        global mode_dark
        if back_color=='rgb(59, 59, 59)':
            mode_dark=1
        else : mode_dark=0
        self.setStyleSheet(f'background-color: {back_color}')
        self.ui.menubar.setStyleSheet(f'color: {font_color}')
        for i in range(9):
           for j in range(9):
                x=self.line_edits[i][j].styleSheet()
                if x != "color: rgb(0, 85, 255)":
                    self.line_edits[i][j].setStyleSheet(f'color: {font_color}')
                # self.line_edits[i][j].setStyleSheet("font: 700 12pt "+"Segoe UI")
                # self.line_edits[i][j].setAlignment(Qt.AlignCenter)
        # self.check()

    def check(self,i=-1,j=-1):
        global mode_dark
        if mode_dark==0: self.reset_Sheet()
        else:
            self.theme('rgb(59, 59, 59)','rgb(255, 255, 255)')
            
        for i in range(9):
            for j in range(9):
                num1 = self.line_edits[i][j].text()
                if num1 == '':
                    return False
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
                self.line_edits[i][j].setStyleSheet("font: 700 12pt "+"Segoe UI")
                self.line_edits[i][j].setAlignment(Qt.AlignCenter)

    def validation(self, i, j,text):
        # text=self.line_edits[i][j].text()
        global check
        if check==0:
            return
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

    def solving(self):
        global check
        global mode_dark
        if mode_dark==0: self.reset_Sheet()
        else:
            self.theme('rgb(59, 59, 59)','rgb(255, 255, 255)')
        check=0
        for i in range(9):
            for j in range(9):
                if self.puzzle.board[i][j] is None:
                    self.line_edits[i][j].setText(str(self.puzzle.solve().board[i][j]))
                    self.line_edits[i][j].setStyleSheet('color: rgb(0, 85, 255)')

        self.checkable = True



if __name__== "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()