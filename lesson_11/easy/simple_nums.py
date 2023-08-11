# Пошук простих чисел: Знайти і вивести всі прості числа у заданому діапазоні.

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