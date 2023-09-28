# Синхронізація даних між різними джерелами:
# Створіть мікс, який дозволить автоматично синхронізувати дані об'єкта між різними джерелами даних,
# такими як бази даних, зовнішні API або файли.
class DataSyncMixin:
    def __init__(self, data_source):
        self._data_source = data_source

    def sync_data(self):
        for key, value in self._data_source.items():
            setattr(self, key, value)

    def update_data_source(self):
        for key in self._data_source.keys():
            self._data_source[key] = getattr(self, key, None)


class MyDataClass(DataSyncMixin):
    def __init__(self, data_source, x):
        super().__init__(data_source)
        self.x = x


data_source = {'x': 5, 'y': 7}

obj = MyDataClass(data_source, x=10)
obj.sync_data()
print(obj.x)

obj.x = 20
obj.update_data_source()
print(data_source['x'])
