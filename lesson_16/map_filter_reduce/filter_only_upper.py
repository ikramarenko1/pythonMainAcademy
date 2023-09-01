# Відфільтрувати слова у реченні, які складаються лише з великих літер, використовуючи filter.
string = 'aHeLLo woRLd ITS a task WITH FILTER funCTion'

filtered_string = ' '.join(
    list(filter(lambda word: word.isupper(), string.split()))
)

print(filtered_string)
