import sys
import gtts
import os
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MyTranslator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MyTranslator()
        self.ui.setupUi(self)
        self.ui.btn_Translate.clicked.connect(self.translate)
        self.ui.btn_Add.clicked.connect(self.Add)
        self.ui.btn_Del.clicked.connect(self.Del)
        
    
    def translate(self):
        if self.ui.rdbtn_engToper.isChecked()==True:
            user_word=self.ui.txt_Source.text().split(" " or ".")
            output=""
            for user_W in user_word:
                for word in Word_bank:
                    if user_W==word["en"]:
                        output=output+ word["fa"]+" "
                        break
                else:
                    output=output+user_W+" "
            self.ui.txt_translate.setText(output) 
            temp_Sound=gtts.gTTS(output,lang="ar",slow=False)
            temp_Sound.save("Assignment_19\Translate\sound_ar.mp3")
        else:       
            user_word=self.ui.txt_Source.text().split(" " or ".")
            output=""
            for user_W in user_word:
                for word in Word_bank:
                    if user_W==word["fa"]:
                        output=output+ word["en"]+" "
                        break
                else:
                    output=output+user_W+" "
            self.ui.txt_translate.setText(output) 
            temp_Sound=gtts.gTTS(output,lang="en",slow=False)
            temp_Sound.save("Assignment_19\Translate\sound_en.mp3")

    def Add(self):
        NewItem={"en":self.ui.txt_En.text(),"fa":self.ui.txt_Fa.text()}
        Word_bank.append(NewItem)
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("Your words is added!")
        msgBox.exec_()
        self.ui.txt_En.setText("")
        self.ui.txt_Fa.setText("")
        file = open("Assignment_19\Translate\Translate.txt", "w")
        for word in Word_bank:
            file.write(word['en']+"\n"+word['fa'] +"\n")
        file.close()
    
    def Del(self):
        self.ui.txt_Source.setText("")
        self.ui.txt_translate.setText("")




                
def read_from_file():
    global Word_bank
    result=os.listdir("Assignment_19\Translate")
    if("Translate.txt")not in result:
        return 0
    print(result)
    file=open("Assignment_19\Translate\Translate.txt","r")
    f=file.read().split("\n")
    Word_bank=[]
    for i in range(0,len(f),2):
        if(i!="\n" and i+1<len(f)):
            My_Dict={"en":f[i],"fa":f[i+1]}
            Word_bank.append(My_Dict)
    file.close()



my_app=QApplication(sys.argv)
My_Window=MainWindow()
My_Window.show()
if(read_from_file()==0):
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Critical)
        msgBox.setText("there is no Dictionary file in the path!")
        msgBox.exec_()


my_app.exec()
