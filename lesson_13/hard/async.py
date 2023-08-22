# Асинхронний код:
# Реалізуйте асинхронну програму, яка виконує паралельні завдання. Обробте помилки,
# пов'язані з асинхронним виконанням, такі як втрата з'єднання, тайм-аути тощо.

import asyncio


async def task_one():
    print("Початок завдання 1")
    await asyncio.sleep(2)
    print("Кiнець завдання 1")


async def task_two():
    print("Початок завдання 2")
    await asyncio.sleep(1)
    raise ConnectionError("Втрата зʼєднання в завданні 2")


async def main():
    try:
        await asyncio.gather(task_one(), task_two())

    except ConnectionError as ce:
        print(ce)


asyncio.run(main())
