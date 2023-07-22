# Task 1
# Напишіть програму, яка приймає список чисел і обчислює суму цих чисел.
# Для розв'язання цього завдання використовується вбудована функція sum(),
# яка приймає список як аргумент і повертає суму його елементів.
# Після обчислення суми вона виводить її на екран.

new_list = [2, 4, 6, 8, 10]
print(new_list)
print(sum(new_list))

print('=====' * 3)

# Task 2
# Напишіть програму, яка перевіряє, чи є список пустим. Для цього використовується перевірка на булеве значення списку.
# Якщо список має елементи, він вважається непорожнім і виводиться False.
# Якщо список порожній, значення bool() перетворюється на True, і виводиться True на екран.
print(new_list)
print(bool(new_list))
new_list = []
print(bool(new_list))

print('=====' * 3)

# Task 3
# Напишіть програму, яка знаходить максимальне значення в списку чисел
new_list = [2, 6, 8, 4, 10]
print(new_list)
print(max(new_list))

print('=====' * 3)

# Task 4
# Напишіть програму, яка сортує список чисел у зростаючому порядку.
print(new_list)
print(sorted(new_list))

print('=====' * 3)

# Task 5
# Напишіть програму, яка знаходить кількість входжень певного елемента в список.
new_list = [2, 2, 8, 2, 10]
print(new_list)
print(new_list.count(2))

print('=====' * 3)

# Task 6
# Напишіть програму, яка приймає список і перевіряє, чи міститься певний елемент
# у списку без використання розгалужень або циклів.
print(new_list)
print(2 in new_list)
print(3 in new_list)

print('=====' * 3)

# Task 7
new_list = ['Hello, ', 'World', '!']
print(new_list)
print(''.join(new_list))