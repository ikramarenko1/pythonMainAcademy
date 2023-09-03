# Конвертація результату в інший формат: Напишіть декоратор, який буде конвертувати результат 
# функції в інший формат, наприклад, у JSON.
import json


def convert_to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_result = json.dumps(result)
        
        return json_result
    return wrapper


@convert_to_json
def get_data():
    data = {
        'name': 'Ilya',
        'surname': 'Kramarenko',
        'age': 20,
        'city': 'Kyiv',
        'is_student': True
    }

    return data


print(get_data())
