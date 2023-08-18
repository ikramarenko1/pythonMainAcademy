# Перетворення рядка в число: Реалізуйте програму, яка перетворює введений
# користувачем рядок в ціле число. Обробте випадок, коли рядок не може бути перетворений в число.
def convert_to_integer(user_input):
    try:
        return int(user_input)
    except ValueError:
        return 'Рядок не може бути перетворений в ціле число.'


while True:
    user_input = input('Введіть рядок, який ви хочете перетворити в ціле число, або "0" для виходу: ')

    if user_input == '0':
        print('Дякую за використання програми!')
        break

    print(convert_to_integer(user_input))
