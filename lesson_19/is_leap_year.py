# Напишіть функцію, яка визначає, чи є заданий рік високосним.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

    return False


year = int(input("Введіть рік: "))

if is_leap_year(year):
    print(f'Рік {year} є високосним.')

else:
    print(f'Рік {year} не є високосним.')
