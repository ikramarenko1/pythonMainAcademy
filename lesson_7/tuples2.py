# Завдання: Перевірити, чи є кортеж пустим
# Опис: Напишіть програму, яка перевіряє, чи є кортеж пустим. Для цього можна використати перевірку
# на булеве значення кортежу. Якщо кортеж має елементи, він вважається непорожнім і виводиться False.
# Якщо кортеж порожній, значення bool() перетворюється на True, і виводиться True на екран.

numbers = (10, 123, 29, 941, 23)
empty_numbers = ()

print(not bool(numbers))  # False
print(not bool(empty_numbers))  # True
