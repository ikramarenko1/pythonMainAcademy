# Відсортуйте список слів за їх довжиною за допомогою лямбда-функції.
sort_list = lambda lst: sorted(lst, key=len)

strings = ['hello', 'world', 'its', 'a', 'task', 'with', 'lambda', 'function']
print(sort_list(strings))
