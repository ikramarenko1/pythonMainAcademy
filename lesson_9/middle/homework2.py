# Числа: Напишіть функцію, яка знаходить всі прості числа
# в заданому діапазоні від 1 до N, де N - вхідний параметр функції.

def simple_nums(min_num, max_num):
    simple_numbers = []

    for num in range(min_num + 1, max_num + 1):
        for i in range(min_num + 1, num):
            if num % i == 0:
                break
        else:
            simple_numbers.append(num)

    return simple_numbers


min_num = 1
max_num = int(input('Введiть максимальну границю: '))

print(simple_nums(min_num, max_num))
