# Відшукання найменшого спільного кратного (НСК): Знайти НСК двох заданих чисел.

def nsk(a, b):
    max_num = max(a, b)

    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num

        max_num += 1


num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

print(f"НСК {num1} та {num2} = {nsk(num1, num2)}")
