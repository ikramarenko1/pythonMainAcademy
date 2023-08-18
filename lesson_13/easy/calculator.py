# Калькулятор операцій: Напишіть програму-калькулятор, яка дозволяє користувачеві
# вводити операцію та два числа. Обробте випадок, коли користувач вводить некоректну операцію.
def calculate(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return 'Ділення на 0 не допустимо!'
        else:
            return num1 / num2
    else:
        return 'Некоректна операція'


while True:
    choice = input('Введіть операцію (+, -, *, /) або 0 для виходу: ')

    if choice == '0':
        print('Дякую за використання програми!')
        break

    try:
        num1 = float(input('Введіть перше число: '))
        num2 = float(input('Введіть друге число: '))
    except ValueError:
        print('Це не коректне число. Будь ласка, спробуйте знову.')
        continue

    result = calculate(choice, num1, num2)

    print(f'Результат: {result}')
