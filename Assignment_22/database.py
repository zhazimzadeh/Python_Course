import sqlite3

class Database:
    def __init__(self) :
        self.con=sqlite3.connect("Assignment_22\ToDoList.db")
        self.cursor=self.con.cursor()

    def get_tasks(self):
        query="select * from tasks order by is_done"
        result=self.cursor.execute(query)
        tasks=result.fetchall()
        return tasks

    def add_new_tasks(self,new_title,new_description,priority,DateTime):
        try:
            query=f"insert into tasks(title,description,priority,is_done,dateTime) VALUES('{new_title}','{new_description}',{priority},{0},'{DateTime}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def remove_task(self):
        ...

    def task_done(self):
        ...