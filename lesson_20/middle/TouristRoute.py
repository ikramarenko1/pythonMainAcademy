# Туристичний маршрут: Створіть клас для представлення туристичного маршруту з можливістю
# додавання точок маршруту та обчислення загальної довжини маршруту.
class RoutePoint:
    def __init__(self, name, length):
        self.name = name
        self.length = length


class TouristRoute:
    def __init__(self, name):
        self.name = name
        self.routes = []

    def __str__(self):
        return f'ℹ️ Iнформацiя про маршрут "{self.name}":\n' \
               f'   Точки маршруту: {", ".join([route.name for route in self.routes])}\n' \
               f'   Довжина маршруту: {self.length} км'

    @property
    def length(self):
        return sum([route.length for route in self.routes])

    def add_point(self, point):
        if isinstance(point, RoutePoint):
            self.routes.append(point)
            print(f'{self.name.upper()}: ✅ Точку {point.name} додано до маршруту {self.name}')
        else:
            print(f'{self.name.upper()}: ❌ Неможливо додати {point} до маршруту {self.name}')

    def remove_point(self, point):
        if isinstance(point, RoutePoint):
            if point in self.routes:
                self.routes.remove(point)
                print(f'{self.name.upper()}: ✅ Точку {point.name} видалено з маршруту {self.name}')
            else:
                print(f'{self.name.upper()}: ❌ Точки {point.name} немає в маршрутi {self.name}')
        else:
            print(f'{self.name.upper()}: ❌ Неможливо додати {point} до маршруту {self.name}')


kharkiv = RoutePoint('Kharkiv', 0)
poltava = RoutePoint('Poltava', 140)
kyiv = RoutePoint('Kyiv', 350)

kharkiv_to_kyiv = TouristRoute('Kharkiv to Kyiv')

kharkiv_to_kyiv.add_point(kharkiv)
kharkiv_to_kyiv.add_point(poltava)
kharkiv_to_kyiv.add_point(kyiv)

print(kharkiv_to_kyiv)
