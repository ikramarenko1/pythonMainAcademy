# Реалізуйте рекурсивну функцію для перевірки паліндрома (слово, яке читається однаково ззаду наперед).

def is_palindrome(string):
    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1]) if string[0] == string[-1] else False


word = input("Введіть слово для перевірки: ").lower()

if is_palindrome(word):
    print(f"'{word}' є паліндромом.")
else:
    print(f"'{word}' не є паліндромом.")
