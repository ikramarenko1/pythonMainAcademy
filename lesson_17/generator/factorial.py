# Факторіали: Створіть генератор, який буде обчислювати факторіал для заданого числа.
def generate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


factorial = generate_factorial(5)
sequence = [x for x in factorial]

print(sequence)
