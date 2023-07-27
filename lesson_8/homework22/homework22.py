# З'єднати вміст декількох файлів у новий файл
# Опис: Напишіть програму, яка з'єднує вміст декількох файлів у новий файл.
# Користувач вводить назви файлів, які треба об'єднати, та назву нового файлу,
# і програма об'єднує їх вміст у новому файлі.
import os


def merge_files(filenames, filename):
    filename = filename.lower().strip()

    with open(filename, 'w') as destination:
        for name in filenames:
            with open(name, 'r') as read_file:
                destination.write(read_file.read())
            destination.write('\n')

    print('Виконано!')
    return True


print('Список доступних файлiв для зʼєднання.\n'
      'УВАГА! Файл для копiюваня в можна придумати свiй, просто впишiть бажану назву.')

for file in os.listdir():
    if 'txt' in file:
        print(file)

filenames = str(input('\nВведіть назви файлiв, які треба обʼєднати, через пробіл: ')).split()
filename_to = str(input('Введіть назву файлу в який обʼєднати файли: '))

merge_files(filenames, filename_to)