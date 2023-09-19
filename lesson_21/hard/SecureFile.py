# Робота з файлами: Створіть клас для роботи з файлами, який забезпечує інкапсуляцію
# відкриття, читання та запису файлів. Захистіть від несанкціонованого доступу до файлових операцій.
class SecureFile:
    def __init__(self, path):
        self.__path = path

    def read(self):
        try:
            with open(self.__path, 'r') as file:
                data = file.read()
                return data
        except Exception as e:
            return f'Виникла помилка при читаннi файлу: {e}'

    def write(self, content):
        try:
            with open(self.__path, 'w') as file:
                file.write(content)
                print('Успiшно записано контент до файлу.')
        except Exception as e:
            print(f'Виникла помилка при спробi запису до файлу: {e}')


txt_file = SecureFile('file.txt')
wrong_file = SecureFile('wrong.txt')

txt_file.write('Test content for file.')
print(txt_file.read())
print(wrong_file.read())
