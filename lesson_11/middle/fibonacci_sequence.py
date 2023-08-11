# Послідовність Фібоначчі:
# Створіть функцію, яка генерує послідовність Фібоначчі до певного N-го члена.
def fibonacci(n):
    if n <= 0:
        return []

    elif n == 1:
        return [0]

    elif n == 2:
        return [0, 1]

    else:
        sequence = [0, 1]

        for i in range(2, n):
            next_value = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_value)

        return sequence


n = int(input('Введiть N-ий член послiдовностi Фібоначчі: '))
print(fibonacci(n))