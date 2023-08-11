# Обчислення числа Пі:
# Використовуючи ряд Лейбніца або інший, обчисліть наближене значення числа Пі.

def get_pi(n):
    pi = 0

    for i in range(n):
        pi += ((-1)**i) / (2*i + 1)

    pi *= 4

    return pi


print(get_pi(10))
