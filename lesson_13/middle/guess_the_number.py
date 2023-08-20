# Генерація випадкового числа: Напишіть програму, яка генерує випадкове число від 1 до 100.
# Попросіть користувача вгадати число. Виведіть повідомлення "Вітаємо, ви вгадали!" або "Спробуйте ще раз!"
# в залежності від результату.

import random

computer_choice = random.randint(1, 100)

print('Привiт! Я загадав число вiд 1 до 100, спробуй вiдгадати!')
user_choice = int(input('Введи число: '))
attempts = 0

while user_choice != computer_choice:
    attempts += 1

    if user_choice > computer_choice:
        print('\nНеправильно! Менше. Спробуй ще раз!')
        user_choice = int(input('Введи число: '))
    else:
        print('\nНеправильно! Бiльше. Спробуй ще раз!')
        user_choice = int(input('Введи число: '))

print(f'\nБраво, ти вгадав за {attempts} спроб! Дякую за гру. :)')
