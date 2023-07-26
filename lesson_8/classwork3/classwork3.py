# Завдання: Зчитати вміст файлу
# Опис: Напишіть програму, яка зчитує вміст з файлу "input.txt" та виводить його на екран.

with open('input.txt', 'r') as file:
    data = file.read()
    print(data)