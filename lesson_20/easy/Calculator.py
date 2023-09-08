# Створіть клас Калькулятор, який має методи додати і відняти, які приймають два числа і повертають їх суму або різницю.

# Розширте клас Калькулятор, додавши методи помножити і поділити, які виконують відповідні математичні операції.

class Calculator:
    def __init__(self, name):
        self.name = name

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError

        return num1 / num2


calc = Calculator("Найкращий калькулятор в свiтi!")

print(calc.add(10, 7))
print(calc.subtract(10, 7))
print(calc.multiply(10, 7))
print(calc.divide(10, 7))
