# Підрахунок голосних: Напишіть генератор для підрахунку кількості голосних в рядку.
def count_vowels(string):
    count = 0

    for char in string.lower():
        if char in 'aeiouаеєиіїоуюя':
            count += 1
            yield count


string = 'Hello, World!'
count_vowels_generator = count_vowels(string)

vowels_in_string = [count for count in count_vowels_generator]
num_of_vowels = vowels_in_string[-1] if vowels_in_string else 0

print(num_of_vowels)
