# База даних: Створіть клас для взаємодії з базою даних.
# Забезпечте інкапсуляцію запитів до бази даних і захистіть конфіденційні дані.
import sqlite3


class Database:
    def __init__(self, db_name):
        self.__db_name = db_name
        self.__connection = None

    def __connect(self):
        if not self.__connection:
            self.__connection = sqlite3.connect(self.__db_name)

    def __disconnect(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def execute_query(self, query, params=None):
        self.__connect()
        cursor = self.__connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        self.__disconnect()

        return result

    def execute_action(self, query, params=None):
        self.__connect()
        cursor = self.__connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        self.__connection.commit()
        self.__disconnect()
