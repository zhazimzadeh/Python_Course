
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
from mytime import MyTime



class Stopwatch_Thread(QThread):
    signal_time=Signal(MyTime)

    def __init__(self) :
        super().__init__()
        self.time=MyTime(0,0,0)

    def run(self):
        while True:
            self.time.plus()
            # print(self.second)
            self.signal_time.emit(self.time)
            time.sleep(1)
    
    def reset(self):
        self.time.hour=0
        self.time.min=0
        self.time.sec=0
        self.signal_time.emit(self.time)
