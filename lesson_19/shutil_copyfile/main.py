# Використовуючи бібліотеку shutil, створіть програму, яка скопіює вміст одного текстового файлу в інший файл.
import shutil
import time

string_to_file = input('Введiть текст для файлу 1, з якого будемо копiювати: ')

try:
    with open('file1.txt', 'w') as file:
        file.write(string_to_file)
        print('✅ Текст до файлу "file1.txt" успiшно записано!')

except Exception as e:
    print(f'Виникла помилка при спробi запису до файлу "file1.txt": {e}')


try:
    shutil.copyfile('file1.txt', 'file2.txt')
    print('✅ Копiювання вмiсту файлу проведено успiшно!')

except Exception as e:
    print(f'Виникла помилка при спробi копiювання вмiсту до файлу "file2.txt": {e}')


try:
    with open('file2.txt', 'r') as file:
        data = file.read()
        time.sleep(1)

        print('✅ Данi з файлу 2 успiшно зчитанi:')
        print(data)

except Exception as e:
    print(f'Виникла помилка при спробi читання з файлу "file2.txt": {e}')
