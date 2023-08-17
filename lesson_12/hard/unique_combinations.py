# Завдання: Генерація унікальних комбінацій списку чисел
# Створіть список унікальних комбінацій чисел від 1 до 6 (включно) з трьох елементів у кожній комбінації.
numbers = [_ for _ in range(1, 7)]

unique_combinations = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            unique_combinations.append((numbers[i], numbers[j], numbers[k]))

print(unique_combinations)
