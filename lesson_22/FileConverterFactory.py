# Конвертер файлів: Реалізуйте фабричний метод для створення об'єктів,
# які відповідають за конвертацію різних типів файлів (наприклад, JSON в XML або зображень в інші формати).
import json
import xml.etree.ElementTree as ET


class FileConverter:
    def convert(self, input_data):
        raise NotImplementedError('Підкласи повинні реалізовувати цей метод')


class JsonToXmlConverter(FileConverter):
    def convert(self, input_data):
        data = json.loads(input_data)
        root = ET.Element('root')

        for key, value in data.items():
            child = ET.Element(key)
            child.text = str(value)
            root.append(child)

        return ET.tostring(root, encoding='unicode')


class FileConverterFactory:
    @staticmethod
    def create_converter(converter_type):
        if converter_type == 'JsonToXml':
            return JsonToXmlConverter()

        else:
            raise ValueError(f'Тип конвертера {converter_type} не розпізнано')


user_choice = input('Введіть тип конвертера (JsonToXml): ')
converter = FileConverterFactory.create_converter(user_choice)
input_data = '{"name": "Ilya", "age": 20, "city": "Kyiv"}'

print(converter.convert(input_data))
