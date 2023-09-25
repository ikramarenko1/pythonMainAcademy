# Історія змін даних: Реалізуйте клас для ведення журналу змін в об'єктах.
# Використовуйте властивість для відстеження історії змін значень властивостей.
class TrackedObject:
    def __init__(self, value):
        self._value = value
        self._history = [(value, 'initial')]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value

        self._history.append((new_value, f'змiнено з {old_value}'))

    def get_history(self):
        return self._history


obj = TrackedObject('test')
obj.value = 'test1'
obj.value = '123'

print(obj.get_history())
