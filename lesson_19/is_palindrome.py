# Напишіть функцію, яка перевіряє, чи є рядок паліндромом (читається однаково зліва направо та справа наліво).
def is_palindrome(string):
    string = string.lower()

    return string == string[::-1]


word = input("Введіть слово для перевірки: ")

if is_palindrome(word):
    print(f"'{word}' є паліндромом.")
else:
    print(f"'{word}' не є паліндромом.")
