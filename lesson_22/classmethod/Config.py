# Створення конфігурації програми: Реалізуйте клас Config, який містить параметри конфігурації програми.
# Створіть класовий метод для завантаження конфігурації з файлу.
import json


class Config:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)

            return cls(data)

        except Exception as e:
            print(f'Виникла помилка при читаннi файлу: {e}')

    def __repr__(self):
        return f'Config({vars(self)})'


config = Config.load_from_file('config.json')

print(config)
