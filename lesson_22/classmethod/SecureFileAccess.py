# Обмеження доступу до ресурсів: Створіть клас для роботи з важливими системними ресурсами,
# такими як доступ до файлів. Використовуйте властивість для забезпечення, що доступ до ресурсу
# відбувається з врахуванням обмежень і прав доступу.
import os


class SecureFileAccess:
    def __init__(self, file_path):
        self.file_path = file_path

    @property
    def content(self):
        if not os.access(self.file_path, os.R_OK):
            raise PermissionError('Вiдмовлено в правах доступу!')

        with open(self.file_path, 'r') as file:
            return file.read()


file_path = 'test.txt'
secure_file = SecureFileAccess(file_path)

try:
    print(secure_file.content)
except Exception as e:
    print(e)
