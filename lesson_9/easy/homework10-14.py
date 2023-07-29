# Обчислення: Обчисліть суму чисел від 1 до 10 (включно) і виведіть результат.
nums = []
for i in range(1, 11):
    nums.append(i)
print(sum(nums))

print('------' * 3)
# Зріз рядка: Задано рядок "Hello, world!". Виведіть перші 5 символів цього рядка.
hello_str = "Hello, world!"
print(hello_str[:5])

print('------' * 3)
# Операції зі списками: Створіть список "numbers" з чисел від 1 до 5.
# Додайте число 6 в кінець списку і видаліть перше число з нього. Виведіть оновлений список.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.pop(0)

print(numbers)

print('------' * 3)
# Перевірка ключа: Створіть словник "grades" з ключами "Math" і "History" та
# відповідними значеннями 90 і 85. Перевірте, чи є ключ "Science" у словнику "grades".
grades = {
    'Math': 90,
    'History': 85
}
print(bool(grades.get('Science')))

print('------' * 3)
# Пошук у списку: Створіть список "numbers" з чисел від 1 до 10. Перевірте, чи є число 8 в цьому списку.
nums = []
for i in range(1, 11):
    nums.append(i)

print(8 in nums)