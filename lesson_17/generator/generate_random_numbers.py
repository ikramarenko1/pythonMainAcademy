# Генерація псевдовипадкових чисел: Напишіть генератор, який буде генерувати послідовність псевдовипадкових чисел.
import random


def generate_random_numbers(count):
    for _ in range(count):
        yield random.randint(1, 51)


count = 10

random_numbers_generator = generate_random_numbers(count)

random_numbers = [num for num in random_numbers_generator]

print(random_numbers)
