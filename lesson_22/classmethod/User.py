# Створення користувача з файлу: Створіть клас User, а потім напишіть класовий метод,
# який створює користувача з інформацією, зчитаною з файлу.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} рокiв'

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                data = file.read().split(',')

                if len(data) < 2:
                    print('Недостатньо iнформацiї для формування інстанції')
                    return None

                name = data[0].strip()
                age = data[1].strip()

                return cls(name, age)
        except Exception as e:
            print(f'Виникла помилка при читаннi файлу: {e}')
            return None


ilya = User.from_file('user.txt')

print(ilya)
