# Піднести кожен елемент списку до квадрату використовуючи map.
lst = [1, 2, 3, 4, 5]
squares_lst = lambda lst: list(map(lambda x: x ** 2, lst))

print(squares_lst(lst))
