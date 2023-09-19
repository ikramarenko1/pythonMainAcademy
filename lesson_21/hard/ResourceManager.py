# Керування ресурсами: Створіть клас для керування ресурсами
# (наприклад, відкриття та закриття файлів, сокетів або з'єднань з базою даних).
# Захистіть ресурси від незаконного доступу.
class ResourceManager:
    def __init__(self, filename, mode):
        self.__filename = filename
        self.__mode = mode
        self.__resource = None

    def __enter__(self):
        self.__resource = open(self.__filename, self.__mode)
        return self.__resource

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__resource:
            self.__resource.close()


with ResourceManager('file.txt', 'r') as file:
    data = file.read()
    print(data)
