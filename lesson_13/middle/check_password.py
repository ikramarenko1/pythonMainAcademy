# Контроль паролю: Реалізуйте програму, яка вимагає введення пароля від користувача. Перевірте, чи введений пароль
# відповідає певим критеріям безпеки. Якщо ні, виведіть повідомлення "Пароль ненадійний".

def check_password(password):
    if len(password) < 8:
        raise Exception("Пароль має бути не менше 8 символів.")

    if not any(char.isupper() for char in password):
        raise Exception("Пароль повинен містити хоча б одну велику літеру.")

    if not any(char.isdigit() for char in password):
        raise Exception("Пароль повинен містити хоча б одну цифру.")


while True:
    user_password = input("Введіть ваш пароль: ")

    try:
        check_password(user_password)
        print("Пароль є безпечним.")
        break

    except Exception as e:
        print(e)
        print('Пароль ненадійний')
