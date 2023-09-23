# Робота з базою даних: Напишіть класовий метод для підключення до бази даних та виконання запитів.
import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)

        self.connection.commit()

    def fetch_all(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


db = Database('my_database.db')

db.execute_query('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
db.execute_query('''INSERT INTO users (name) VALUES (?)''', ('Ilya',))

users = db.fetch_all('''SELECT * FROM users''')
print(users)

db.close()
