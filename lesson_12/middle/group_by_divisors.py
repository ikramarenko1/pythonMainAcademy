# Завдання: Групування чисел за дільником
# Дано список чисел. Створіть словник, де ключами будуть дільники, а значеннями - список чисел,
# які діляться на ці дільники.
import random

nums = [random.randint(1, 11) for _ in range(5)]
divisor_dict = {}

for num in nums:
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            if divisor in divisor_dict:
                divisor_dict[divisor].append(num)

            else:
                divisor_dict[divisor] = [num]

print(divisor_dict)
