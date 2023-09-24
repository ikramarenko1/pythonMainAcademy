# Робота з файловою системою: Напишіть клас, який дозволяє створювати,
# копіювати та переміщати файли на файловій системі за допомогою класових методів.
import os
import shutil


class FileManager:
    @classmethod
    def create_file(cls, file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)

            print(f'Створення файлу {file_path} пройшло успiшно!')
        except Exception as e:
            print(f'Виникла помилка при створеннi файлу: {e}.')

    @classmethod
    def copy_file(cls, source_path, destination_path):
        try:
            shutil.copy(source_path, destination_path)
            print(f'Копiювання вмiсту з файлу {source_path} в {destination_path} пройшло успiшно!')
        except Exception as e:
            print(f'Помилка в copy_file: {e}')

    @classmethod
    def move_file(cls, source_path, destination_path):
        try:
            shutil.move(source_path, destination_path)
            print(f'Перемiщення файлу {source_path} в {destination_path} пройшло успiшно!')
        except Exception as e:
            print(f'Помилка в move_file: {e}')

    @classmethod
    def delete_file(cls, file_path):
        try:
            os.remove(file_path)
            print(f'Видалення файлу {file_path} пройшло успiшно!')
        except Exception as e:
            print(f'Помилка в delete_file: {e}')


FileManager.create_file('test.txt', 'Текст для тестового файлу.')
FileManager.create_file('test1.txt', '')
FileManager.copy_file('test.txt', 'test1.txt')
FileManager.move_file('test1.txt', 'moved_test.txt')

# FileManager.delete_file('test.txt')
FileManager.delete_file('moved_test.txt')
