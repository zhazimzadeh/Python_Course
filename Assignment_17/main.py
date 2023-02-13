import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader



global flg_empty
flg_empty=0
def sub():
    global A,O
    if(My_Window.txt_1.text()==""): My_Window.txt_1.setText("0")
    A=float(My_Window.txt_1.text())
    My_Window.txt_1.setText("")
    O="-"

def sum():
    global A,O
    if(My_Window.txt_1.text()==""): My_Window.txt_1.setText("0")
    A=float(My_Window.txt_1.text())
    My_Window.txt_1.setText("")
    O="+"

def mul():
    global A,O
    if(My_Window.txt_1.text()==""): My_Window.txt_1.setText("0")
    A=float(My_Window.txt_1.text())
    My_Window.txt_1.setText("")
    O="*"

def div():
    global A,O
    if(My_Window.txt_1.text()==""): My_Window.txt_1.setText("0")
    A=float(My_Window.txt_1.text())
    My_Window.txt_1.setText("")
    O="/"

def sign():
    My_Window.txt_1.setText(str(float(My_Window.txt_1.text())*-1))

def pow():
    global A,O
    if(My_Window.txt_1.text()==""): My_Window.txt_1.setText("0")
    A=float(My_Window.txt_1.text())
    My_Window.txt_1.setText("")
    O="^"

def sqrt():
    global flg_empty
    My_Window.txt_1.setText(str(math.sqrt(float(My_Window.txt_1.text()))))
    flg_empty=1

def log():
    global flg_empty
    My_Window.txt_1.setText(str(math.log(float(My_Window.txt_1.text()))))
    flg_empty=1

def sin():
    global flg_empty
    My_Window.txt_1.setText(str(math.sin(float(My_Window.txt_1.text()))))
    flg_empty=1

def cos():
    global flg_empty
    My_Window.txt_1.setText(str(math.cos(float(My_Window.txt_1.text()))))
    flg_empty=1

def tan():
    global flg_empty
    My_Window.txt_1.setText(str(math.tan(float(My_Window.txt_1.text()))))
    flg_empty=1

def cot():
    global flg_empty
    My_Window.txt_1.setText(str(math.cot(float(My_Window.txt_1.text()))))
    flg_empty=1

def perc():
    global flg_empty
    My_Window.txt_1.setText(str((float(My_Window.txt_1.text()))/100))
    flg_empty=1



def Result():
        global flg_empty
        B=float(My_Window.txt_1.text())
        if(O=="+"):        
            result=A+B 
        elif(O=="-"):
            result=A-B 
        elif(O=="*"):
            result=A*B 
        elif(O=="/"):
            while(B==0):
                B=float(My_Window.txt_1.text())
            result=A/B 
        elif(O=="^"):
            result=(A)**(B )
        My_Window.txt_1.setText(str(result))

        flg_empty=1


def AC():
    My_Window.txt_1.setText("")

def zero():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('0')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'0')

def one():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('1')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'1')

def two():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('2')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'2')

def three():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('3')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'3')

def four():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('4')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'4')

def five():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('5')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'5')

def six():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('6')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'6')

def seven():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('7')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'7')

def eight():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('8')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'8')

def nine():
    global flg_empty
    if(flg_empty):
        My_Window.txt_1.setText('9')
        flg_empty=0
    else:
        My_Window.txt_1.setText(My_Window.txt_1.text()+'9')
    
def decimal_point():
    My_Window.txt_1.setText(My_Window.txt_1.text()+'.')





my_app=QApplication([])
loader=QUiLoader()
My_Window=loader.load("Python_Course\Assignment_17\MyCalc.ui")
My_Window.show()
My_Window.btn_Sub.clicked.connect(sub)
My_Window.btn_Sum.clicked.connect(sum)
My_Window.btn_Multiply.clicked.connect(mul)
My_Window.btn_Dive.clicked.connect(div)
My_Window.btn_Sign.clicked.connect(sign)
My_Window.btn_Pow.clicked.connect(pow)
My_Window.btn_Sqrt.clicked.connect(sqrt)
My_Window.btn_Log.clicked.connect(log)
My_Window.btn_Sin.clicked.connect(sin)
My_Window.btn_Cos.clicked.connect(cos)
My_Window.btn_Tan.clicked.connect(tan)
My_Window.btn_Cot.clicked.connect(cot)
My_Window.btn_Percentage.clicked.connect(perc)
My_Window.btn_AC.clicked.connect(AC)
My_Window.btn_Result.clicked.connect(Result)
My_Window.btn_0.clicked.connect(zero)
My_Window.btn_1.clicked.connect(one)
My_Window.btn_2.clicked.connect(two)
My_Window.btn_3.clicked.connect(three)
My_Window.btn_4.clicked.connect(four)
My_Window.btn_5.clicked.connect(five)
My_Window.btn_6.clicked.connect(six)
My_Window.btn_7.clicked.connect(seven)
My_Window.btn_8.clicked.connect(eight)
My_Window.btn_9.clicked.connect(nine)
My_Window.btn_Dot.clicked.connect(decimal_point)


my_app.exec()
