# Завдання: Пошук спільних слів у реченнях
# Дано два речення. Створіть список слів, які зустрічаються в обох реченнях.

sentence1 = ['Hello', 'World!', 'How', 'are', 'you']
sentence2 = ['Hello', 'Ilya!', 'are', 'you', 'okay']

common_words = [word for word in sentence1 if word in sentence2]

print(common_words)
