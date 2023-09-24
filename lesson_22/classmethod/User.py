# Створення користувача з файлу: Створіть клас User, а потім напишіть класовий метод,
# який створює користувача з інформацією, зчитаною з файлу.

# Створення користувача з API: Створіть клас User і класовий метод,
# який створює користувача, отримуючи дані з віддаленого API.

# Валідація введених даних: Створіть клас для представлення користувача з властивістю "вік".
# Використовуйте властивість для перевірки, чи вік є дійсним числом і чи він в межах припустимого діапазону.
import requests


class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def __str__(self):
        return f'{self.name}, {self._age} рокiв'

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

    @classmethod
    def from_api(cls, user_id):
        api_url = f'https://some-api.com/users/{user_id}'

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            user_data = response.json()

            return cls(user_data['name'], user_data['age'])

        except Exception as e:
            return f'Виникла помилка при отриманнi iнформацiї з API: {e}'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if not 0 <= value <= 101:
            raise ValueError('Вiк повинен бути в межах вiд 0 до 101!')

        self._age = value


ilya = User.from_file('user.txt')
print(ilya)

ilya_api = User.from_api(1337)
print(ilya_api)

ilya_age = User('Ilya AGE', '20')
print(ilya_age.age)

ilya_age.age = '123'
print(ilya_age.age)
