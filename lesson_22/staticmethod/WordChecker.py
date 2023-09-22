# Перевірка паліндрому: Створіть статичний метод для перевірки, чи є дане слово або фраза паліндромом.
class WordChecker:
    @staticmethod
    def is_palindrome(word):
        if len(word) <= 1:
            return True

        return WordChecker.is_palindrome(word[1:-1]) if word[0] == word[-1] else False


word = input("Введіть слово для перевірки: ")

if WordChecker.is_palindrome(word.lower()):
    print(f"'{word}' є паліндромом.")
else:
    print(f"'{word}' не є паліндромом.")
