# Зменшити регістр всіх елементів списку слів використовуючи map
lst = ['HeLLo', 'woRLd', 'ITS', 'a', 'task', 'WiTh', 'mAp', 'funCTion']

filtered_lst = list(map(lambda word: word.lower(), lst))

print(lst)
print(filtered_lst)
