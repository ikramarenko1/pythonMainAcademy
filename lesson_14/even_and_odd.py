# Поділ на парні та непарні: Напишіть функцію, яка розділить список чисел на парні та непарні.

def division_into_even_and_odd(*args):
    even = []
    odd = []

    for num in args:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd


even, odd = division_into_even_and_odd(1, 2, 3, 4, 5, 6)

print(f'Парні числа - {even}')
print(f'Непарні числа - {odd}')