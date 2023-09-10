# Комплексні числа: Реалізуйте клас для роботи з комплексними числами з підтримкою операцій
# додавання, віднімання та множення.
class ComplexNum:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + {self.imaginary}i' if self.imaginary >= 0 else f'{self.real} - {-self.imaginary}i'

    def __add__(self, num):
        return ComplexNum(self.real + num.real, self.imaginary + num.imaginary)

    def __sub__(self, num):
        return ComplexNum(self.real - num.real, self.imaginary - num.imaginary)

    def __mul__(self, num):
        real = self.real * num.real - self.imaginary * num.imaginary
        imaginary = self.real * num.imaginary + self.imaginary * num.real
        
        return ComplexNum(real, imaginary)


num1 = ComplexNum(3, 2)
num2 = ComplexNum(1, 7)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
