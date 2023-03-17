import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
from mytime import MyTime



class Timer_Thread(QThread):
    signal_show=Signal(MyTime)

    def __init__(self,h,m,s) :
        super().__init__()
        self.time=MyTime(h,m,s)

    def run(self):
        while True:
            self.time.minus()
            # print(self.second)
            self.signal_show.emit(self.time)
            time.sleep(1)
    
    def reset(self):
        self.time.hour=0
        self.time.min=0
        self.time.sec=0
        self.signal_show.emit(self.time)
