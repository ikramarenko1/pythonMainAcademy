# Визначте кількість голосних букв у рядку за допомогою лямбда-функції.
count_vowels = lambda string: sum(1 for char in string if char.lower() in 'aeiouаеєиіїоуюя')

user_string = 'Hello, World! Привіт, світ!'

print(f'Кількість голосних в рядку - {count_vowels(user_string)}')
