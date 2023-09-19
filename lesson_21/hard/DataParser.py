# Парсинг даних: Розробіть клас для парсингу та обробки структурованих даних
# (наприклад, XML або JSON). Забезпечте інкапсуляцію парсингу та доступу до даних.
import json


class DataParser:
    def __init__(self):
        self.__data = None

    def load_data(self, json_string):
        self.__data = json.loads(json_string)

    def get_data(self, key):
        return self.__data.get(key) if self.__data else None


parser = DataParser()

json_string = '{"name": "Ilya", "age": 20, "city": "Kyiv"}'
parser.load_data(json_string)

name = parser.get_data('name')
age = parser.get_data('age')

print(name, age)
