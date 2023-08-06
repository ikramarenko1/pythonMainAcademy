# Визначення чиcла днів у місяці

month = int(input('Введiть номер мiсяця для визначення кiлькостi днiв у ньому: '))

while month not in range(1, 12):
    print(f'Мiсяця {month} не існує. Перевірте інформацію та повторіть введення.')
    month = int(input('Введiть номер мiсяця для визначення кiлькостi днiв у ньому: \n'))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f'Кiлькiсть днiв в {month}-ому мiсяцi - 31')
elif month == 2:
    print(f'Кiлькiсть днiв в {month}-ому мiсяцi - 28 або 29')
else:
    print(f'Кiлькiсть днiв в {month}-ому мiсяцi - 30')