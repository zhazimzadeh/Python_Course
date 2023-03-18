from datetime import datetime
from pytz import timezone
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *


class WorldClock_Thread(QThread):
    signal_timezone=Signal(datetime)
    def __init__(self,location):
        super().__init__()
        self.loc=location

    def run(self): 
        while True:
            if self.loc=='IR':
                self.signal_timezone.emit(datetime.now())
                # print(datetime.now())
            else:
                tz=timezone(self.loc)
                self.signal_timezone.emit(datetime.now(tz))
                # print(datetime.now(tz))
            time.sleep(1)


