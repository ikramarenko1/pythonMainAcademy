# Множини: Створіть програму, яка зчитує два списки від користувача
# та повертає їх перетин, об'єднання та різницю у вигляді множин.

def calculate_set_operations(list1, list2):
    list1, list2 = set(list1), set(list2)

    intersection = list1 & list2
    union = list1 | list2
    difference = list1 - list2

    print(f'Перетин: {intersection}')
    print(f'Обʼєднання: {union}')
    print(f'Різниця: {difference}')

    return intersection, union, difference


user_list1 = input('Введiть елементи першого списку через пробiл: ').split()
user_list2 = input('Введiть елементи другого списку через пробiл: ').split()

calculate_set_operations(user_list1, user_list2)
