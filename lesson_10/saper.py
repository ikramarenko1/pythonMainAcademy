# Задача: Гра "Сапер"
# Створіть гру "Сапер", в якій комп'ютер генерує поле з мінами та порожніми клітинами.
# Користувач повинен вводити координати клітин, і комп'ютер повинен вказувати, чи вибрана клітина
# містить міну або виводити кількість сусідніх клітин з мінами. Використайте умовний оператор для
# перевірки стану клітини та визначення результату дії користувача.

import random


def make_field(size, mines_count):
    field = []
    mines = []

    for i in range(size):
        row = []

        for j in range(size):
            row.append(' ')

        field.append(row)

    while len(mines) < mines_count:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)

        if (x, y) not in mines:
            mines.append((x, y))
            field[y][x] = 'M'

    return field


def count_mines_around(x, y, field, size):
    mine_count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = x + i, y + j

            if 0 <= nx < size and 0 <= ny < size and field[ny][nx] == 'M':
                mine_count += 1

    return mine_count


size = 5
mines_count = 5
field = make_field(size, mines_count)

while True:
    x, y = map(int, input(f"Введіть координати x y клітини через пробiл, де 0 <= x,y < {size}): ").split())

    if 0 <= x < size and 0 <= y < size:
        if field[y][x] == 'M':
            print("Ви натрапили на мiну!")
            break
        else:
            mines_around = count_mines_around(x, y, field, size)
            print(f"Навколо клітини {mines_around} мін.")

    else:
        print("Некоректні координати! Спробуйте ще раз.")
