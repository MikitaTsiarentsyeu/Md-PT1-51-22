import sqlite3

class DB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def user_exists(self, username):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_name` = ?", (username,))
        return bool(len(result.fetchall()))

    def register_user(self, username, password):
        self.cursor.execute("INSERT INTO `users` (`user_name`, `user_password`) VALUES (?, ?)", (username,password,))  
        return self.conn.commit()  

    def get_user_id(self, username):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_name` = ?", (username,))
        return result.fetchone()[0]
    
    def get_user_info(self, username):
        result = self.cursor.execute("SELECT `user_password` FROM `users` WHERE `user_name` = ?", (username,))
        return result.fetchone()[0]

    def get_count_tasks(self):
        result = self.cursor.execute("SELECT COUNT(*) FROM tasks")
        return result.fetchone()[0]
    
    def create_task(self, task_name, json_name):
        self.cursor.execute("INSERT INTO `tasks` (`task_name`, `task_json`) VALUES (?, ?)", (task_name,json_name,))  
        return self.conn.commit() 

    def load_tasks(self, page):
        result = self.cursor.execute("SELECT * FROM `tasks` WHERE `id` > ? LIMIT 5", (page*5-5,))
        return result.fetchall()

    def complete_task(self, user_id, task_id, result):
        result = self.cursor.execute("INSERT INTO `task_logs` (`user_id`, `task_id`, `result`) VALUES (?, ?, ?)", (user_id,task_id, result))
        return self.conn.commit() 

    def get_results_tasks(self, user_id, task_id):
        result = self.cursor.execute("SELECT * FROM `task_logs` WHERE `user_id` = ? AND `task_id` = ?", (user_id,task_id,))
        return result.fetchall()
    
    def check_admin(self, user_id):
        result = self.cursor.execute("SELECT * FROM `admins` WHERE `user_id` = ?", (user_id,))
        return result.fetchall()
    
    def add_admin(self, user_id):
        result = self.cursor.execute("INSERT INTO `admins` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit() 

    def close(self):
        self.conn.close()