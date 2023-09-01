# Перетворити список рядків на список їх заголовків (перша буква велика, інші малі) використовуючи map.
strings = ['hello world', 'world hello', 'its', 'a', 'task', 'with', 'map', 'function']

titles = list(map(lambda word: word.title(), strings))

print(titles)
