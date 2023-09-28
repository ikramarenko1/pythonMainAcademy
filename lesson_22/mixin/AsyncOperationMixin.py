# Реалізація механізму асинхронного виконання:
# Розробіть мікс, який дозволить об'єкту виконувати асинхронні операції та координувати їхнє виконання в
# асинхронному середовищі Python, наприклад, за допомогою бібліотеки asyncio.
import asyncio


class AsyncOperationMixin:
    async def async_operation(self, duration):
        print(f'Починаю асинхронну функцiю на {duration} секунд.')
        await asyncio.sleep(duration)

        print('Асинхронна функцiя виконана.')


class MyClass(AsyncOperationMixin):
    def __init__(self, name):
        self.name = name


async def main():
    obj = MyClass('test')
    await obj.async_operation(2)


asyncio.run(main())
