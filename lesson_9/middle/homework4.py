# Списки: Напишіть функцію, яка приймає список чисел і повертає новий список,
# де кожен елемент - квадрат відповідного числа вхідного списку.
def elem_to_square(list1):
    new_list = []
    for elem in list1:
        new_list.append(elem**2)

    return new_list


list1 = [1, 2, 3, 4, 5]
print(elem_to_square(list1))
