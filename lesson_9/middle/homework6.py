# Кортежі: Напишіть функцію, яка приймає два кортежі однакового розміру та повертає новий кортеж,
# який складається з сум елементів на відповідних позиціях у вхідних кортежах.
def get_new_tuple(tuple1, tuple2):
    result = []

    for i in range(min(len(tuple1), len(tuple2))):
        result.append(tuple1[i] + tuple2[i])

    return tuple(result)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
print(get_new_tuple(tuple1, tuple2))