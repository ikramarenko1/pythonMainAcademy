# Читання та обробка файлу: Створіть програму, яка зчитує текстовий файл "data.csv" з даними
# у форматі CSV (Comma-Separated Values) та обчислює середнє значення чисел у кожному рядку,
# записуючи результати у новий файл "averages.txt".

with open('data.csv', 'r') as data_file:
    with open('averages.txt', 'w') as av_file:
        for line in data_file:
            numbers = line.strip().split(',')

            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])

            average = round(sum(numbers) / len(numbers), 2)
            av_file.write(f'{average}\n')

    print('Готово!')

