# Делегування роботи генераторам: Створіть генератор, який буде делегувати роботу іншому
# генератору залежно від певних умов.
def to_upper(strings):
    for string in strings:
        yield string.strip().upper()


def to_lower(strings):
    for string in strings:
        yield string.strip().lower()


def delegating_processor(strings, upper=False):
    if upper:
        yield from to_upper(strings)
    else:
        yield from to_lower(strings)


strings = ["  Hello ", "  World ", " Its a test! "]

processed_to_upper = list(delegating_processor(strings, True))
processed_to_lower = list(delegating_processor(strings))

print(processed_to_upper)
print(processed_to_lower)
