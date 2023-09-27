# Автоматична серіалізація в JSON:
# Створіть мікс, який дозволяє об'єктам автоматично серіалізуватися в формат JSON.
# Це може бути корисно для передачі даних через API або зберігання даних у зручному форматі.
import json


class JsonSerializableMixin:
    def to_json(self):
        return self.__dict__

    @classmethod
    def from_json(cls, json_str):
        data = json.dumps(json_str)
        return cls(**data)


class Person(JsonSerializableMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


ilya = Person('Ilya', 20)
print(ilya.to_json())
