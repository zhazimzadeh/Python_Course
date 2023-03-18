
import sys
import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
from main_ui import Ui_MainWindow
from stopwatch import Stopwatch_Thread
from timer_ import Timer_Thread
from worldclock import WorldClock_Thread
# from database import MyDB
from pytz import all_timezones
import pyglet
import sqlite3




pyglet.font.add_file("Assignment_25\Seven Segment.ttf")
id=0

# def db():
#     global con
#     global cur
#     con=sqlite3.connect("Assignment_25\Alarm.db")
#     cur=con.cursor()

class MainWindow(QMainWindow):
    # signal_timer_hour=Signal(int)
    # signal_timer_min=Signal(int)
    # signal_timer_sec=Signal(int)
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.con=sqlite3.connect("Assignment_25\Alarm.db")
        self.cur=self.con.cursor()
        self.line_edits=[]
        i=0
        for i in range(12):
                new_btn=QPushButton()
                new_btn.setText("X")
                new_btn.setStyleSheet("background-color: rgb(255, 85, 0);font: 700 12pt"+"Segoe UI;border-radius: 15px; ")
                
                new_btn_edit=QPushButton()
                new_btn_edit.setText("Edit")
                new_btn_edit.setStyleSheet("background-color: rgb(170, 255, 255);font: 700 12pt"+"Segoe UI;border-radius: 15px;")

                new_cell=QLineEdit()
                # new_cell.setFixedSize(45,45)
                new_cell.setStyleSheet("font: 700 10pt "+"Segoe UI;color: rgb(255, 255, 255); ")
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.setText(f"0:0:0_ ...")
                self.ui.gridLayout.addWidget(new_cell,i,0)
                self.ui.gridLayout.addWidget(new_btn,i,1)
                self.ui.gridLayout.addWidget(new_btn_edit,i,2)
                new_btn.clicked.connect(partial(self.Del_alarm,'Del',new_cell))
                new_btn_edit.clicked.connect(partial(self.Edit_Alarm,new_cell))
        
                self.line_edits.append(new_cell)
                
        self.get_Data()
       


        # self.signal_timer_hour.emit(int(self.ui.txt_hour_timer.text()))
        # self.signal_timer_min.emit(int(self.ui.txt_min_timer.text()))
        # self.signal_timer_sec.emit(int(self.ui.txt_sec_timer.text()))

        self.thread_stopwatch=Stopwatch_Thread()
        # self.thread_timer=Timer_Thread(self.signal_timer_hour,self.signal_timer_min,self.signal_timer_sec)
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
        
        self.ui.lbl_stopwatch.setText("0:0:0")
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)
        self.thread_stopwatch.signal_time.connect(self.get_stopwatch_data)

        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        self.thread_timer.signal_show.connect(self.get_timer_data)

        self.ui.btn_add_alarm.clicked.connect(self.Add_Alarm)
        # self.ui.btn_del_alarm.clicked.connect(partial(self.del_edit_alarm,'Del'))
        self.ui.btn_edit_alarm.clicked.connect(self.Edit_Done)
    
    def Edit_Done(self):
        global id
        self.cur.execute(f"update alarms set hour={int(self.ui.txt_hour_Alarm.text())}, min={int(self.ui.txt_min_Alarm.text())},sec={int(self.ui.txt_sec_Alarm.text())}, desc='{self.ui.txt_alarm_desc.text()}'	where id={id}")
        self.con.commit() 
        self.ui.txt_alarm_desc.setText("")
        self.ui.txt_hour_Alarm.setText("0")
        self.ui.txt_min_Alarm.setText("0")
        self.ui.txt_sec_Alarm.setText("0")
        self.get_Data() 

    def Edit_Alarm(self,alarm_data):
            global id
            Alarm_Time=alarm_data.text().split(":")
            sec=Alarm_Time[2].split("_")
            temp =self.cur.execute(f"select id from alarms where hour={int(Alarm_Time[0])} and min={int(Alarm_Time[1])} and sec={int(sec[0])}").fetchall()
            id=temp[0][0]

            # if len(id)==0:
            #     msg_box = QMessageBox()
            #     msg_box.setText('This Alarm does not exist!')
            #     msg_box.setWindowTitle('Alarm')
            #     msg_box.setIcon(QMessageBox.Icon.Critical)
            #     msg_box.exec()
            #     return()
            # else:
            self.ui.txt_hour_Alarm.setText(Alarm_Time[0])
            self.ui.txt_min_Alarm.setText(Alarm_Time[1])
            self.ui.txt_sec_Alarm.setText(sec[0])
            self.ui.txt_alarm_desc.setText(sec[1])

            msg_box = QMessageBox()
            msg_box.setText('Change data then click on Edit button')
            msg_box.setWindowTitle('edit')
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.exec()



        


    def Add_Alarm(self):
            self.cur.execute(f"INSERT into alarms (hour,min,sec,desc) VALUES({int(self.ui.txt_hour_Alarm.text())},{int(self.ui.txt_min_Alarm.text())},{int(self.ui.txt_sec_Alarm.text())},'{self.ui.txt_alarm_desc.text()}')")
            self.con.commit()
            self.ui.txt_alarm_desc.setText("")
            self.ui.txt_hour_Alarm.setText("0")
            self.ui.txt_min_Alarm.setText("0")
            self.ui.txt_sec_Alarm.setText("0")
            self.get_Data() 

    def Del_alarm(self,command,alarm_data):
            Alarm_Time=alarm_data.text().split(":")
            sec=Alarm_Time[2].split("_")[0]
            id =self.cur.execute(f"select id from alarms where hour={int(Alarm_Time[0])} and min={int(Alarm_Time[1])} and sec={int(sec)}").fetchall()
            if len(id)==0:
                msg_box = QMessageBox()
                msg_box.setText('This Alarm does not exist!')
                msg_box.setWindowTitle('Alarm')
                msg_box.setIcon(QMessageBox.Icon.Critical)
                msg_box.exec()
            else:
                self.cur.execute(f"DELETE from alarms where id={id[0][0]}")
                self.con.commit() 

            self.get_Data() 

 


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
        for i in range(12):
             if(self.line_edits[i].text()!=""):
                temp=self.line_edits[i].text().split(":")
                if int(temp[0])==time.hour and int(temp[1])==time.minute:
                    temp2=temp[2].split("_")
                    if int(temp2[0])==time.second:
                        msg_box = QMessageBox()
                        msg_box.setText(f'This is Time to  {temp2[1]}')
                        msg_box.setWindowTitle('Alarm')
                        msg_box.setIcon(QMessageBox.Icon.Information)
                        msg_box.exec()

    def get_DEtime_data(self,time):
        self.ui.lbl_timeDE.setText(f"{time.hour}:{time.minute}:{time.second}")

    def get_UStime_data(self,time):
        self.ui.lbl_timeUS.setText(f"{time.hour}:{time.minute}:{time.second}")


    def get_Data(self):
        result =self.cur.execute("select * from alarms").fetchall()
        i=0
        for i in range(12):
             self.line_edits[i].setText("")
        i=0
        for alarm in result:
                self.line_edits[i].setText(f"{alarm[1]}:{alarm[2]}:{alarm[3]}_{alarm[4]}")
                i+=1
                


if __name__=="__main__":
    # for tz in all_timezones:
    #  print(tz)
    # db()
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec()
