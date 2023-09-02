# Парсинг даних: Напишіть генератор для парсингу структурованих даних, таких як JSON або XML.
import json


def parse_json(file_path, key_list):
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    for key in key_list:
        if key in json_data:
            yield {key: json_data[key]}


keys = ['name', 'age', 'is_student']
json_file = 'file.json'

parsed_data_generator = parse_json(json_file, keys)
parsed_data = [item for item in parsed_data_generator]

print(parsed_data)
