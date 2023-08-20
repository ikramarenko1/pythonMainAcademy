# Калькулятор з історією: Створіть програму-калькулятор, яка дозволяє користувачеві вводити операцію та два числа.
# Зберігайте історію обчислень у файлі "history.txt". Обробте можливу помилку запису до файлу.

def calculate(operation, num1, num2):
    try:
        with open('history.txt', 'a') as file:
            if operation == '+':
                file.write(f'{num1} + {num2} = {num1 + num2}\n')
                return num1 + num2

            elif operation == '-':
                file.write(f'{num1} - {num2} = {num1 - num2}\n')
                return num1 - num2

            elif operation == '*':
                file.write(f'{num1} * {num2} = {num1 * num2}\n')
                return num1 * num2

            elif operation == '/':
                if num2 == 0:
                    file.write(f'{num1} / {num2} - Ділення на 0 не допустимо!\n')
                    return 'Ділення на 0 не допустимо!'
                else:
                    file.write(f'{num1} / {num2} = {num1 / num2}\n')
                    return num1 / num2

            else:
                file.write('Некоректна операція\n')
                return 'Некоректна операція'

    except FileNotFoundError:
        print('Виникла помилка при спробi запису до файлу. Файл не знайдено.')
    except Exception as e:
        print(e)


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
