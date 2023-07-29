# Зріз рядка: Створіть програму, яка приймає рядок від користувача та
# виводить на екран кожну другу літеру цього рядка.
def get_every_second_char(string):
    return string[::2]


user_str = str(input('Введiть рядок: '))
print(get_every_second_char(user_str))