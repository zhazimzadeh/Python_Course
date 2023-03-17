import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
from main_ui import Ui_MainWindow
from stopwatch import Stopwatch_Thread
from timer_ import Timer_Thread
from worldclock import WorldClock_Thread
from pytz import all_timezones




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.thread_stopwatch=Stopwatch_Thread()
        self.thread_timer=Timer_Thread(int(self.ui.txt_hour_timer.text()),int(self.ui.txt_min_timer.text()),int(self.ui.txt_sec_timer.text()))
        self.thread_worldclock_US=WorldClock_Thread('UTC')
        self.thread_worldclock_DE=WorldClock_Thread('Europe/Berlin')
        self.thread_worldclock_IR=WorldClock_Thread('IR')
        self.thread_worldclock_US.start()
        self.thread_worldclock_DE.start()
        self.thread_worldclock_IR.start()
        self.thread_worldclock_IR.signal_timezone.connect(self.get_IRtime_data)
        self.thread_worldclock_DE.signal_timezone.connect(self.get_DEtime_data)
        self.thread_worldclock_US.signal_timezone.connect(self.get_UStime_data)
        
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)
        self.thread_stopwatch.signal_time.connect(self.get_stopwatch_data)

        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        self.thread_timer.signal_show.connect(self.get_timer_data)

    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()
    
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()

    def get_stopwatch_data(self,time):
        self.ui.lbl_stopwatch.setText(f"{time.hour}:{time.min}:{time.sec}")

    def start_timer(self):
        self.thread_timer.start()

    def stop_timer(self):
        self.thread_timer.terminate()
    
    def reset_timer(self):
        self.thread_timer.reset()

    def get_timer_data(self,time):
        self.ui.txt_hour_timer.setText(str(time.hour))
        self.ui.txt_min_timer.setText(str(time.min))
        self.ui.txt_sec_timer.setText(str(time.sec))
        if time.hour == 0 and time.min == 0 and time.sec == 0 :
            msg_box = QMessageBox()
            msg_box.setText('Time is Over')
            msg_box.setWindowTitle('Alarm')
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.exec()

    def get_IRtime_data(self,time):
        self.ui.lbl_timeIR.setText(f"{time.hour}:{time.minute}:{time.second}")

    def get_DEtime_data(self,time):
        self.ui.lbl_timeDE.setText(f"{time.hour}:{time.minute}:{time.second}")

    def get_UStime_data(self,time):
        self.ui.lbl_timeUS.setText(f"{time.hour}:{time.minute}:{time.second}")


if __name__=="__main__":
    # for tz in all_timezones:
    #  print(tz)
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()
