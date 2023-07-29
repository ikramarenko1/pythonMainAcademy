# Запис у файл: Напишіть програму, яка зчитує великий текстовий файл "big_file.txt"
# та створює новий файл "shortened_file.txt", в якому кожен рядок містить не більше 50 символів.
import random
import string

with open('big_file.txt', 'w') as file:
    for _ in range(10):
        length = random.randint(10, 100)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        file.write(f'{random_string}\n')

    print('Рядки до файлу записано!')


with open('big_file.txt', 'r') as big_file:
    with open('shortened.txt', 'w') as short_file:
        for line in big_file:
            while len(line) > 50:
                short_file.write(line[:50] + '\n')
                line = line[50:]

            short_file.write(line)

    print('Скорочений запис виконано!')
