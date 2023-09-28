# Автоматичне зберігання змінних об'єкта в базі даних:
# Створіть мікс, який дозволить автоматично зберігати стан об'єкта
# в базі даних при його зміні і виконанні певних дій.
class Database:
    def __init__(self):
        self._data = {}

    def save(self, object_id, attributes):
        self._data[object_id] = attributes

    def load(self, object_id):
        return self._data.get(object_id)


class AutoSaveMixin:
    def __init__(self, db, object_id):
        self._db = db
        self._object_id = object_id

    def _save_to_db(self):
        self._db.save(self._object_id, self.__dict__)


class MyClass(AutoSaveMixin):
    def __init__(self, db, object_id, x):
        super().__init__(db, object_id)
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._save_to_db()


db = Database()
obj = MyClass(db, 'object_id', 5)

obj.x = 10
