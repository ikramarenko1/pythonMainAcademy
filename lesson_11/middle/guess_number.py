# Гра вгадай число:
# Створіть гру, в якій комп'ютер вибирає випадкове число,
# а користувач повинен вгадати його, отримуючи підказки "більше" або "менше".
import random

min_num, max_num = 0, 30
comp_choice = random.randint(min_num, max_num)
tries = 0

print(f'Комп\'ютер загадав число вiд {min_num} до {max_num}. Спробуй вiдгадати!')

while True:
    num = int(input('Яке число загадав комп\'ютер?: '))
    tries += 1

    if num == comp_choice:
        print(f'\n🎉 Ви виграли! Кiлькiсть спроб, що знадобилася - {tries}')
        break
    elif num > comp_choice:
        print('Менше, спробуй ще!')
    else:
        print('Бiльше, спробуй ще!')

