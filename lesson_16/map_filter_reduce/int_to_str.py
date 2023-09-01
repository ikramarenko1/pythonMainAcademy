# Перетворити список чисел на список їх строкових представлень використовуючи map.
lst = [1, 2, 3, 4, 5]

string_lst = list(map(lambda x: str(x), lst))

print(string_lst)
