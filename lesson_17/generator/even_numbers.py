# Парні числа: Напишіть генератор, який буде генерувати послідовність парних чисел.
def generate_even_numbers():
    n = 2
    while True:
        yield n
        n += 2


even_numbers = generate_even_numbers()

for _ in range(10):
    print(next(even_numbers))
