# Обчислення середнього: Напишіть програму, яка обчислює середнє арифметичне чисел
# зі списку, введеного користувачем. Обробте випадок, коли список пустий.
user_input = input('Введіть список чисел, через символ "," (наприклад: 1, 2, 3, 4): ')

try:
    numbers = [float(x) for x in user_input.split(',')]
except ValueError:
    print('Будь ласка, введіть коректний список чисел.')
    numbers = []

try:
    average = sum(numbers) / len(numbers)
    print(f'Середнє арифметичне чисел у списку: {average}')
except ZeroDivisionError:
    print('Список чисел пустий, обчислення неможливе.')
