# Аутентифікація та авторизація:
# Створіть систему аутентифікації та авторизації користувачів. Обробте помилки,
# пов'язані з некоректними або відсутніми обліковими записами, недостатнім рівнем
# доступу та іншими ситуаціями.

import sqlite3


def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password TEXT,
            access_level INTEGER
        );
        ''')
        
        conn.commit()


def add_user(username, password, access_level=1):
    try:
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f'INSERT INTO users (username, password, access_level) VALUES (?, ?, ?);',
                           (username, password, access_level))

            conn.commit()

    except sqlite3.IntegrityError:
        print('Користувач вже існує!')


def authenticate(username, password):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?;', (username, password))

        # Повертає наступний рядок результату запиту. Результат представлено у вигляді кортежу.
        user = cursor.fetchone()

        if user:
            return user

        else:
            print('Невірний логін або пароль!')
            return None


def authorize(user, required_level):
    if user[2] >= required_level:
        print(f'Ласкаво просимо, {user[0]}!')

    else:
        print(f'{user[0]}, у вас недостатній рівень доступу.')


init_db()
add_user('admin', 'qwerty12345', 3)
add_user('user', '12345', 1)

user = authenticate('admin', 'qwerty12345')
if user:
    authorize(user, 2)

user = authenticate('user', '12345')
if user:
    authorize(user, 2)
