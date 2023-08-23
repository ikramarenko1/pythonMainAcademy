# Конвертація температури: Напишіть функції для конвертації температури з Цельсія в Фаренгейт
# і навпаки.

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


celsius_temp = int(input('Введiть градуси по Цельсію: '))
fahrenheit_temp = int(input('Введiть градуси по Фаренгейту: '))

print(f"{celsius_temp}°C = {celsius_to_fahrenheit(celsius_temp):.2f}°F")
print(f"{fahrenheit_temp}°F = {fahrenheit_to_celsius(fahrenheit_temp):.2f}°C")

