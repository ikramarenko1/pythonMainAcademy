# Імітація простого вірусу:
# У цій задачі ми створюємо простий вірус, який "інфікує" файли у вказаному каталозі,
# додаючи до них певний код. Використовуємо цикли та функції для обробки файлів та додавання коду.
import os


def indect_files(directory, text):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'a') as file:
                file.write(text)

    print('Успiх! Файли було iнфiковано!')


directory = 'txt_files_to_add_virus'
text = '\nHAHAHAHAH! You got the virus!!! X_x\n'

indect_files(directory, text)
