# Конвертер числа в римську систему числення:
# Напишіть програму, яка приймає десяткове число і перетворює його на римську систему числення.

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


user_num = int(input('Введiть рiк для його переведення в римську систему числення: '))

print(to_roman(user_num))