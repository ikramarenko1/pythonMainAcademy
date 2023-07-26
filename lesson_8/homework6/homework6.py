# Завдання: Копіювати файли
# Опис: Напишіть програму, яка копіює вміст файлу "source.txt" в новий файл "destination.txt".

with open('source.txt', 'r') as source:
    with open('destination.txt', 'w') as destination:
        destination.write(source.read())

    print('Операція закінчена!')
