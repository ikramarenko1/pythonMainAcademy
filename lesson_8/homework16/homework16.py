# Скопіювати вміст одного файлу в інший
# Опис: Напишіть програму, яка копіює вміст одного файлу в інший.
# Користувач вводить назви двох файлів, і програма копіює вміст з першого файлу в другий.
import os


def copy_to_another(filename1, filename2):
    filename1 = filename1.lower().strip()
    filename2 = filename2.lower().strip()

    with open(filename1, 'r') as file1:
        with open(filename2, 'w') as file2:
            file2.write(file1.read())

    print('Виконано!')
    return True


print('Список доступних файлiв для копiювання.\n'
      'УВАГА! Файл для копiюваня в можна придумати свiй, просто впишiть бажану назву.')

for file in os.listdir():
    if 'txt' in file:
        print(file)

filename_from = str(input('\nВведіть назву файлу з якого скопіювати вміст: '))
filename_to = str(input('Введіть назву файлу в який скопіювати вміст: '))

copy_to_another(filename_from, filename_to)
