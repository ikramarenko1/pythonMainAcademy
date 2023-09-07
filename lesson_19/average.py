# Створіть програму, яка знаходить середнє арифметичне чисел у списку.
get_average = lambda lst: sum(lst) / len(lst)

user_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_average(user_lst))
