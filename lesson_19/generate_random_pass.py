# Створіть функцію, яка генерує випадковий пароль заданої довжини.
import random
import string


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))

    return password


length = int(input('Введiть якої довжини потрiбно згенерувати пароль: '))
print('Згенерований пароль - ' + generate_password(length))
