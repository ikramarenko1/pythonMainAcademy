# Перетворення рядка: Реалізуйте програму, яка приймає рядок від користувача та намагається
# перетворити його в ціле число. Якщо це не вдається, виведіть повідомлення "Неможливо перетворити в число".
def convert_to_integer(user_input):
    try:
        return int(user_input)
    except ValueError:
        return 'Неможливо перетворити в число'


while True:
    user_input = input('Введіть рядок, який ви хочете перетворити в ціле число, або "0" для виходу: ')

    if user_input == '0':
        print('Дякую за використання програми!')
        break

    print(convert_to_integer(user_input))
