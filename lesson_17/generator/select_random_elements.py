# Вибірка зі списку: Створіть генератор, який буде вибирати певну кількість випадкових елементів зі списку.
import random

def select_random_elements(lst, count):
    sampled_list = random.sample(lst, min(count, len(lst)))

    for item in sampled_list:
        yield item


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst = [1, 2]
count = 3

random_elements_generator = select_random_elements(lst, count)
random_elements = [num for num in random_elements_generator]

print(random_elements)
