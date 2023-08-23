# Конвертація числа в римський запис: Напишіть функцію, яка конвертує дане число в римський запис.

def to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]

    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]

    roman_num = ''
    i = 0

    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]

        i += 1

    return roman_num


user_num = int(input('Введiть число для його переведення в римську систему числення: '))

print(to_roman(user_num))
