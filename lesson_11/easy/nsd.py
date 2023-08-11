# Знаходження найбільшого спільного дільника (НСД): Знайти НСД двох заданих чисел.

def nsd(a, b):
    if a == b:
        return a

    if a == 0:
        return b

    if b == 0:
        return a

    if a % 2 == 0 and b % 2 == 0:
        return 2 * nsd(a // 2, b // 2)

    if a % 2 == 0:
        return nsd(a // 2, b)

    if b % 2 == 0:
        return nsd(a, b // 2)

    if a > b:
        return nsd((a - b) // 2, b)

    return nsd((b - a) // 2, a)


num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

print(f"НСД {num1} та {num2} = {nsd(num1, num2)}")
