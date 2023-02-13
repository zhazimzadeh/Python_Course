import sys
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_Convert.clicked.connect(self.calculate)
        self.ui.rdbtn_weight.clicked.connect(self.AddItem)
        self.ui.rdbtn_lenght.clicked.connect(self.AddItem)
        self.ui.rdbtn_temp.clicked.connect(self.AddItem)
        self.ui.rdbtn_digital.clicked.connect(self.AddItem)

    def AddItem(self):
        self.ui.cmbx_from.clear()
        self.ui.cmb_To.clear()
        if self.ui.rdbtn_weight.isChecked()==True:
            self.ui.cmbx_from.addItems(["grams","kilograms","tons","pounds"])
            self.ui.cmb_To.addItems(["grams","kilograms","tons","pounds"])
        elif self.ui.rdbtn_lenght.isChecked()==True:
            self.ui.cmbx_from.addItems(["mm","cm","m","km","inch"])
            self.ui.cmb_To.addItems(["mm","cm","m","km","inch"])
        elif self.ui.rdbtn_temp.isChecked()==True:
            self.ui.cmbx_from.addItems(["Celsius","Fahrenheit","Kelvin"])
            self.ui.cmb_To.addItems(["Celsius","Fahrenheit","Kelvin"])
        elif self.ui.rdbtn_digital.isChecked()==True:
            self.ui.cmbx_from.addItems(["bit","byte","kilobyte","megabyte","gigabyte","terabyte"])
            self.ui.cmb_To.addItems(["bit","byte","kilobyte","megabyte","gigabyte","terabyte"])





    def calculate(self):

        if self.ui.rdbtn_weight.isChecked()==True:
            if self.ui.cmbx_from.currentIndex()==0:#Gram
                if self.ui.cmb_To.currentIndex()==0:
                    self.ui.txt_result.setText(str(self.ui.txt_Input.text()))
                elif self.ui.cmb_To.currentIndex()==1:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001 ))
                elif self.ui.cmb_To.currentIndex()==2:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.000001 ))
                elif self.ui.cmb_To.currentIndex()==3:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.0022046226))
            elif self.ui.cmbx_from.currentIndex()==1:#Kg
                if self.ui.cmb_To.currentIndex()==0:
                    self.ui.txt_result.setText(str(self.ui.txt_Input.text()*1000))
                elif self.ui.cmb_To.currentIndex()==1:
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text()) ))
                elif self.ui.cmb_To.currentIndex()==2:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001 ))
                elif self.ui.cmb_To.currentIndex()==3:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*2.20462262))
            elif self.ui.cmbx_from.currentIndex()==2:#ton
                if self.ui.cmb_To.currentIndex()==0:
                    self.ui.txt_result.setText(str(self.ui.txt_Input.text()*1000000))
                elif self.ui.cmb_To.currentIndex()==1:
                    self.ui.txt_result.setText((self.ui.txt_Input.text())*1000 )
                elif self.ui.cmb_To.currentIndex()==2:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text()) ))
                elif self.ui.cmb_To.currentIndex()==3:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*2204.62262))
            elif self.ui.cmbx_from.currentIndex()==3:#pond
                if self.ui.cmb_To.currentIndex()==0:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*453.5923703804))
                elif self.ui.cmb_To.currentIndex()==1:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.4535923704 ))
                elif self.ui.cmb_To.currentIndex()==2:
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text()) ))
                elif self.ui.cmb_To.currentIndex()==3:
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.0004535924))

        elif self.ui.rdbtn_lenght.isChecked()==True:
            if self.ui.cmbx_from.currentIndex()==0:#mm
                if self.ui.cmb_To.currentIndex()==0:#mm
                    self.ui.txt_result.setText(str(self.ui.txt_Input.text()))
                elif self.ui.cmb_To.currentIndex()==1:#cm
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.1 ))
                elif self.ui.cmb_To.currentIndex()==2:#m
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001 ))
                elif self.ui.cmb_To.currentIndex()==3:#km
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.000001))
                elif self.ui.cmb_To.currentIndex()==4:#inch
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.0393700787))
            elif self.ui.cmbx_from.currentIndex()==1:#cm
                if self.ui.cmb_To.currentIndex()==0:#mm
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*10))
                elif self.ui.cmb_To.currentIndex()==1:#cm
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text()) ))
                elif self.ui.cmb_To.currentIndex()==2:#m
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.01 ))
                elif self.ui.cmb_To.currentIndex()==3:#km
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.00001))
                elif self.ui.cmb_To.currentIndex()==4:#inch
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.3937007874))
            elif self.ui.cmbx_from.currentIndex()==2:#m
                if self.ui.cmb_To.currentIndex()==0:#mm
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text())*1000))
                elif self.ui.cmb_To.currentIndex()==1:#cm
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text())*100 ))
                elif self.ui.cmb_To.currentIndex()==2:#m
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text()) ))
                elif self.ui.cmb_To.currentIndex()==3:#km
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001))
                elif self.ui.cmb_To.currentIndex()==4:#inch
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*39.37007874))
            elif self.ui.cmbx_from.currentIndex()==3:#km
                if self.ui.cmb_To.currentIndex()==0:#mm
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text())*1000000 ))
                elif self.ui.cmb_To.currentIndex()==1:#cm
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text())*100000  ))
                elif self.ui.cmb_To.currentIndex()==2:#m
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000  ))
                elif self.ui.cmb_To.currentIndex()==3:#km
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())))
                elif self.ui.cmb_To.currentIndex()==4:#inch
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*39370.07874))
            elif self.ui.cmbx_from.currentIndex()==4:#inch
                if self.ui.cmb_To.currentIndex()==0:#mm
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text())*25.4000000001  ))
                elif self.ui.cmb_To.currentIndex()==1:#cm
                    self.ui.txt_result.setText(str((self.ui.txt_Input.text())*2.54  ))
                elif self.ui.cmb_To.currentIndex()==2:#m
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.0254  ))
                elif self.ui.cmb_To.currentIndex()==3:#km
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.0000254 ))
                elif self.ui.cmb_To.currentIndex()==4:#inch
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())))

        elif self.ui.rdbtn_temp.isChecked()==True:
            if self.ui.cmbx_from.currentIndex()==0:#c
                if self.ui.cmb_To.currentIndex()==0:#c
                    self.ui.txt_result.setText(str(self.ui.txt_Input.text()))
                elif self.ui.cmb_To.currentIndex()==1:#f
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*33.8 ))
                elif self.ui.cmb_To.currentIndex()==2:#k
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*274.15 ))
            elif self.ui.cmbx_from.currentIndex()==1:#f
                if self.ui.cmb_To.currentIndex()==0:#c
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*-17.22222222222222))
                elif self.ui.cmb_To.currentIndex()==1:#f
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text()) ))
                elif self.ui.cmb_To.currentIndex()==2:#k
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*255.92777777777775  ))
            elif self.ui.cmbx_from.currentIndex()==2:#k
                if self.ui.cmb_To.currentIndex()==0:#c
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*-272.15))
                elif self.ui.cmb_To.currentIndex()==1:#f
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*-457.86999999999995 ))
                elif self.ui.cmb_To.currentIndex()==2:#k
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text()) ))

        elif self.ui.rdbtn_digital.isChecked()==True:
            if self.ui.cmbx_from.currentIndex()==0:#bit
                if self.ui.cmb_To.currentIndex()==0:#bit
                    self.ui.txt_result.setText(str(self.ui.txt_Input.text()))
                elif self.ui.cmb_To.currentIndex()==1:#byte
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.125 ))
                elif self.ui.cmb_To.currentIndex()==2:#kb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.000125   ))
                elif self.ui.cmb_To.currentIndex()==3:#mb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1.25e-7  ))
                elif self.ui.cmb_To.currentIndex()==4:#gb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1e-10 ))
                elif self.ui.cmb_To.currentIndex()==5:#tb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1.25e-13 ))
            elif self.ui.cmbx_from.currentIndex()==1:#byte
                if self.ui.cmb_To.currentIndex()==0:#bit
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*8))
                elif self.ui.cmb_To.currentIndex()==1:#byte
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text()) ))
                elif self.ui.cmb_To.currentIndex()==2:#kb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001    ))
                elif self.ui.cmb_To.currentIndex()==3:#mb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.000001    ))
                elif self.ui.cmb_To.currentIndex()==4:#gb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1e-9 ))
                elif self.ui.cmb_To.currentIndex()==5:#tb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1e-12 ))
            elif self.ui.cmbx_from.currentIndex()==2:#kb
                if self.ui.cmb_To.currentIndex()==0:#bit
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*8000 ))
                elif self.ui.cmb_To.currentIndex()==1:#byte
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000  ))
                elif self.ui.cmb_To.currentIndex()==2:#kb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())   ))
                elif self.ui.cmb_To.currentIndex()==3:#mb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001   ))
                elif self.ui.cmb_To.currentIndex()==4:#gb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.000001   ))
                elif self.ui.cmb_To.currentIndex()==5:#tb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1e-9 ))
            elif self.ui.cmbx_from.currentIndex()==3:#mb
                if self.ui.cmb_To.currentIndex()==0:#bit
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*8000000   ))
                elif self.ui.cmb_To.currentIndex()==1:#byte
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000000   ))
                elif self.ui.cmb_To.currentIndex()==2:#kb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000    ))
                elif self.ui.cmb_To.currentIndex()==3:#mb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())   ))
                elif self.ui.cmb_To.currentIndex()==4:#gb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001   ))
                elif self.ui.cmb_To.currentIndex()==5:#tb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.000001  ))
            elif self.ui.cmbx_from.currentIndex()==4:#gb
                if self.ui.cmb_To.currentIndex()==0:#bit
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*7999999999.999999   ))
                elif self.ui.cmb_To.currentIndex()==1:#byte
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*999999999.9999999    ))
                elif self.ui.cmb_To.currentIndex()==2:#kb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000000     ))
                elif self.ui.cmb_To.currentIndex()==3:#mb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000    ))
                elif self.ui.cmb_To.currentIndex()==4:#gb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())   ))
                elif self.ui.cmb_To.currentIndex()==5:#tb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*0.001   ))
            elif self.ui.cmbx_from.currentIndex()==5:#tb
                if self.ui.cmb_To.currentIndex()==0:#bit
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*8000000000000   ))
                elif self.ui.cmb_To.currentIndex()==1:#byte
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000000000000     ))
                elif self.ui.cmb_To.currentIndex()==2:#kb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000000000      ))
                elif self.ui.cmb_To.currentIndex()==3:#mb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000000     ))
                elif self.ui.cmb_To.currentIndex()==4:#gb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())*1000    ))
                elif self.ui.cmb_To.currentIndex()==5:#tb
                    self.ui.txt_result.setText(str(float(self.ui.txt_Input.text())   ))

                


my_app=QApplication(sys.argv)
My_Window=MainWindow()
My_Window.show()

my_app.exec()
        