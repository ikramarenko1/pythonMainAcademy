# Завдання: Копіювати словник
# Опис: Напишіть програму, яка створює словник dict1 та копіює його у словник dict2
# за допомогою функції copy.copy(). Змініть значення ключа в dict2 і виведіть обидва
# словники, щоб побачити, що вони впливають один на одного.
import copy

dict1 = {1: 'value1', 2: 'value2', 3: 'value3', 4: 'value4'}
dict2 = copy.copy(dict1)

dict2[3] = 'NOTvalue4'

print(dict1)
print(dict2)
