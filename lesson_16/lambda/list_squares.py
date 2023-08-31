# Згенеруйте список квадратів чисел від 1 до 10 за допомогою лямбда-функції та map.
square = lambda x: x ** 2
squares_list = list(map(square, range(1, 11)))

print(squares_list)
