# Сортування списку: Напишіть статичний метод, який сортує список об'єктів за певним критерієм.
class ListSorter:
    @staticmethod
    def sort(objects_list, attribute):
        return sorted(objects_list, key=lambda obj: getattr(obj, attribute))


class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f'Назва: {self.name}, рiк випуску: {self.year}'

    # Отримання строкового представлення об'єкта, має бути валідним виразом Python,
    # за допомогою якого можна відтворити об'єкт. Воно призначене для розробників
    # і зазвичай використовується для відлагодження.
    def __repr__(self):
        return f'Назва: {self.name}, рiк випуску: {self.year}'

    # __repr__ — це офіційне строкове представлення об'єкта,
    # а __str__ — більш інформативне та дружнє до користувача.


cars = [
    Car('Audi', 2018),
    Car('BMW', 2021),
    Car('Ford', 2008),
    Car('Mercedes', 2022)
]

sorted_cars = ListSorter.sort(cars, 'year')

print(sorted_cars)
