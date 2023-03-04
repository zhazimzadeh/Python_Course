import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_main import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.db=Database()      
        self.ui.btn_newTask.clicked.connect(self.new_task)
        self.read_from_db()
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def read_from_db(self):
        tasks=self.db.get_tasks()
        for i in range(len(tasks)):
            chbx=QCheckBox()
            lbl=QLabel()
            lbl_priority=QLabel()
            btn=QPushButton()
            btn_info=QPushButton()
            chbx.toggled.connect(partial(self.done_tasks,tasks[i][0]))
            btn.clicked.connect(partial(self.del_tasks,tasks[i][0]))
            btn_info.clicked.connect(partial(self.show_info,tasks[i][0]))
            
            if(tasks[i][4]==1):
                chbx.setChecked(True)
            chbx.setText(tasks[i][1])
            lbl_priority.setText(str(tasks[i][3]))
            if(int(lbl_priority.text())>5):
                chbx.setStyleSheet("color: rgb(255, 0, 0)")
            else:
                chbx.setStyleSheet("color: rgb(0, 170, 0)")

            btn_info.setText("Info")
            btn.setText("❌")
            self.ui.grd_tasks.addWidget(chbx,i,1)
            # self.ui.grd_tasks.addWidget(lbl,i,0)
            self.ui.grd_tasks.addWidget(btn_info,i,0)
            self.ui.grd_tasks.addWidget(btn,i,2)
            self.ui.grd_tasks.addWidget(lbl_priority,i,3)


    def new_task(self):
        new_title=self.ui.txt_newTask.text()
        new_description=self.ui.txt_desc.toPlainText()
        new_priority=int(self.ui.txt_priority.text())
        new_DateTime=self.ui.dateTimeEdit.text()
        feedback=self.db.add_new_tasks(new_title,new_description,new_priority,new_DateTime)
        if feedback==True:
            self.read_from_db()
            self.ui.txt_desc.setText("")
            self.ui.txt_newTask.setText("")
            self.ui.txt_priority.setText("")
            self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        else:
            msg_box=QMessageBox()
            msg_box.setText("We have a problem!")
            msg_box.exec()

    def done_tasks(self, id, checked):
        self.db.task_done(id, checked)

            
    def del_tasks(self,id):
        self.db.remove_task(id)
        children = []
        for i in range(self.ui.grd_tasks.count()):
            child = self.ui.grd_tasks.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()
        self.read_from_db()

    def show_info(self,id):
        result=self.db.get_taskInfo(id)
        self.ui.txt_desc.setText(str(result[0][2])+"\n"+str(result[0][5]))
        # self.ui.txt_desc.setStyleSheet("color: rgb(255, 0, 0)")
        # self.ui.dateTimeEdit.setDateTime(QDateTime(result[0][5]))
    
    

        



if __name__=="__main__":
    app=QApplication(sys.argv)

    main_window=MainWindow()
    main_window.show()

    app.exec()