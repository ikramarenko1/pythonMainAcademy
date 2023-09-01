# Відфільтрувати слова у реченні, які починаються на 'a', використовуючи filter.

string = 'aHeLLo woRLd aITS a task WiTh amAp funCTion'

filtered_string = ' '.join(
    list(filter(lambda word: word[0] == 'a', string.split()))
)

print(filtered_string)
