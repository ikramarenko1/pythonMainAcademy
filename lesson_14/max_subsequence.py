# Пошук максимальної підпослідовності: Напишіть функцію, яка знаходить найбільшу
# зростаючу підпослідовність у списку чисел.

def max_increasing_subsequence(numbers):
    subsequences = [[num] for num in numbers]

    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] > numbers[j] and len(subsequences[i]) < len(subsequences[j]) + 1:
                subsequences[i] = subsequences[j] + [numbers[i]]

    return max(subsequences, key=len)


numbers = map(int, input('Введiть список чисел через пробiл для пошуку максимальної підпослідовності: ').split())

print(max_increasing_subsequence(*numbers))
