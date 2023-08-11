# Міні-гра "Камінь-ножиці-папір"
import random


def get_winner(user_choice, computer_choice):
    if user_choice == 'камінь' and computer_choice == 'ножиці':
        return 'Ви'
    elif user_choice == 'камінь' and computer_choice == 'папір':
        return 'Комп\'ютер'
    elif user_choice == 'ножиці' and computer_choice == 'камінь':
        return 'Комп\'ютер'
    elif user_choice == 'ножиці' and computer_choice == 'папір':
        return 'Ви'
    elif user_choice == 'папір' and computer_choice == 'камінь':
        return 'Ви'
    elif user_choice == 'папір' and computer_choice == 'ножиці':
        return 'Комп\'ютер'
    else:
        return 'Нiчия'


print('Зараз будемо грати в "Камінь-ножиці-папір"..')
play = True

while play:
    computer_choice = random.choice(['камінь', 'ножиці', 'папір'])
    user_choice = str(input('\nВведiть ваш вибір (к - камінь, н - ножиці, п - папір, 0 - щоб вийти): ')).lower()

    while user_choice not in ['к', 'н', 'п', '0']:
        user_choice = str(input('Повторiть введення (к - камінь, н - ножиці, п - папір, 0 - щоб вийти): ')).lower()

    if user_choice == '0':
        play = False
        break

    user_choice = 'камінь' if user_choice == 'к' else 'ножиці' if user_choice == 'н' else 'папір'

    print(f'Ваш вибiр - {user_choice}, вибiр комп\'ютера - {computer_choice}')
    print('Переможець:', get_winner(user_choice, computer_choice))

print('\nВи вийшли з гри. Дякую за проведений час!')