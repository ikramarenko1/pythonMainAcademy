# Запис у файл: Створіть список "names" з іменами "John", "Alice" та "Bob".
# Запишіть цей список в текстовий файл "names.txt", кожне ім'я на окремому рядку.
names = ['John', 'Alice', 'Bob']

with open('names.txt', 'w') as file:
    file.write('\n'.join(names))
