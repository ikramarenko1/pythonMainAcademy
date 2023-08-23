# Підрахунок суми цифр: Напишіть функцію, яка обчислює суму цифр даного числа.

def get_sum_of_nums(num):
    result = 0

    for num in str(num):
        result += int(num)

    return result


user_input = int(input('Введiть число для обчислення суми його цифр: '))

print(get_sum_of_nums(user_input))
