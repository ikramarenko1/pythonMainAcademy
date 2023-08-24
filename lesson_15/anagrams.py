# Задача з анаграмами: Напишіть функцію, яка перевіряє, чи є дві задані строки
# анаграмами (містять одні й ті ж символи в тому ж кількості, але можуть бути переставлені).
import re

def is_anagrams(string1, string2):
    string1 = ''.join(sorted(string1.replace(' ', '').lower()))
    string2 = ''.join(sorted(string2.replace(' ', '').lower()))

    return string1 == string2


string1 = input('Введiть перший рядок: ')  # 'hello'
string2 = input('Введiть другий рядок: ')  # 'hlloe'

if is_anagrams(string1, string2):
    print(f'{string1} та {string2} є анаграмами')
else:
    print(f'{string1} та {string2} не є анаграмами')
