# Використовуючи бібліотеку argparse, створіть програму, яка може обчислювати площу прямокутника або трикутника,
# залежно від переданих аргументів.
import argparse


def calculate_area_rectangle(length, width):
    return length * width


def calculate_area_triangle(base, height):
    return 0.5 * base * height


parser = argparse.ArgumentParser(description='Обчислити площу прямокутника або трикутника')

parser.add_argument('--length', type=float, help='Довжина прямокутника')
parser.add_argument('--width', type=float, help='Ширина прямокутника')
parser.add_argument('--base', type=float, help='Основа трикутника')
parser.add_argument('--height', type=float, help='Висота трикутника')
parser.add_argument('--shape', type=str, choices=['rectangle', 'triangle'], help='Форма для обчислення площі.')

args = parser.parse_args()

if args.shape == 'rectangle':
    if args.length and args.width:
        area = calculate_area_rectangle(args.length, args.width)
        print(f'Площа прямокутника: {area}.')
    else:
        print('Для прямокутника потрiбно вказати довжину та ширину прямокутника.')

elif args.shape == 'triangle':
    if args.base and args.height:
        area = calculate_area_triangle(args.base, args.height)
        print(f'Площа трикутника: {area}.')
    else:
        print('Для трикутника потрiбно вказати основу та висоту трикутника.')

else:
    print('Будь ласка, вкажiть тип фiгури для обчислення площi.')

# Приклади для запуску:
# --shape rectangle --length 5 --width 4
# --shape triangle --base 10 --height 5
