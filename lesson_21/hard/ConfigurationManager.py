# Керування конфігурацією: Створіть клас для зберігання та зміни конфігураційних параметрів додатку.
# Захистіть конфігураційні дані від несанкціонованого доступу.
import json


class ConfigurationManager:
    def __init__(self, config_dict=None):
        self.__config_data = config_dict if config_dict else {}

    def set(self, key, value):
        self.__config_data[key] = value

    def get(self, key, default=None):
        return self.__config_data.get(key, default)

    def remove(self, key):
        if key in self.__config_data:
            del self.__config_data[key]

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.__config_data = json.load(file)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__config_data, file)


config = ConfigurationManager()
config.set('db_host', '127.0.0.1')
config.set('db_port', 5525)

db_host = config.get('db_host')
db_port = config.get('db_port')

print(db_host, db_port)
