# База даних та транзакції:
# Створіть програму для роботи з базою даних, яка дозволяє додавати та оновлювати записи.
# Реалізуйте механізм транзакцій, який дозволяє відмінити зміни у випадку виникнення помилки
# під час виконання транзакції.

import sqlite3


def create_db():
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        );
        ''')


def add_user(name, age):
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(f'INSERT INTO users (name, age) VALUES ("{name}", {age});')
            connection.commit()

        except sqlite3.Error as e:
            connection.rollback()
            print(f'Виникла помилка під час додавання користувача! {e}')


def update_user(id, name, age):
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(f'UPDATE users SET name = "{name}", age = {age} WHERE id = {id};')
            connection.commit()

        except sqlite3.Error as e:
            connection.rollback()
            print(f'Виникла помилка під час оновлення користувача! {e}')


create_db()
add_user('Iлля', 20)
add_user('Саша', 19)

update_user(10, 'Марина', 40)