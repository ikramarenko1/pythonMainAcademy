# 3. Задача: Визначення частки і залишку
# Опис: Напишіть програму, яка знаходить частку і залишок від ділення двох цілих чисел
# без використання вбудованих операторів ділення та залишку.

def division_without_operators(dividend, divisor):
    if divisor == 0:
        return "Помилка! Дільник не може бути нулем!"

    quotient = 0
    remainder = dividend

    while remainder >= divisor:
        remainder -= divisor
        quotient += 1

    return quotient, remainder


dividend = int(input("Введіть ділене: "))
divisor = int(input("Введіть дільник: "))

quotient, remainder = division_without_operators(dividend, divisor)

print(f"Частка: {quotient}, залишок: {remainder}")
