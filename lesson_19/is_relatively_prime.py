# Створіть програму, яка приймає два числа та визначає, чи є вони взаємно простими
# (не мають спільних дільників, крім 1).
def is_relatively_prime(a, b):
    divisors = {
        'a': [],
        'b': []
    }

    for i in range(1, a):
        if a % i == 0:
            divisors['a'].append(a)

    for i in range(1, b):
        if b % i == 0:
            if i in divisors['a']:
                return False

            divisors['b'].append(b)

    return True


a = int(input('Введiть перше число: '))
b = int(input('Введiть друге число: '))

if is_relatively_prime(a, b):
    print(f'Числа {a} та {b} є взаємно простими')
else:
    print(f'Числа {a} та {b} не є взаємно простими')
