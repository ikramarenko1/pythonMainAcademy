# Генерація паролю: Створіть статичний метод, який генерує випадковий пароль з заданою довжиною.
import random
import string


class PasswordGenerator:
    @staticmethod
    def generate(length=8):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))

        return password


length = int(input('Введiть якої довжини потрiбно згенерувати пароль: '))
new_pass = PasswordGenerator.generate(length)

print(f'Згенерований пароль - {new_pass}')
