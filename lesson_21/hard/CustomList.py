# Контейнери з даними: Створіть клас, який реалізує власний список
# (аналог списку у Python). Захистіть його від додавання і видалення
# елементів безпосередньо зі списку.
class CustomList:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self.__data = initial_data

    def append(self, item):
        self.__data.append(item)

    def remove(self, item):
        self.__data.remove(item)

    def insert(self, index, item):
        self.__data.insert(index, item)

    def pop(self, index=-1):
        return self.__data.pop(index)

    def __str__(self):
        return str(self.__data)

    def __len__(self):
        return len(self.__data)


custom_list = CustomList([1, 2, 3])
custom_list.append(4)
custom_list.insert(1, 9)

removed_item = custom_list.pop(2)

print(str(custom_list))
print(len(custom_list))
