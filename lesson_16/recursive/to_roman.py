# Напишіть рекурсивну функцію для перетворення числа в римський запис.
def to_roman(n):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    if n == 0:
        return ""

    for i, value in enumerate(val):
        if n >= value:
            return syms[i] + to_roman(n - value)


numbers = [1, 3, 9, 31, 100, 3999]  # ['I', 'III', 'IX', 'XXXI', 'C', 'MMMCMXCIX']
roman_numerals = [to_roman(n) for n in numbers]

print(roman_numerals)

