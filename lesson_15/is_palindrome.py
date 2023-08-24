# Задача зі списками: Напишіть програму, яка визначає, чи є список
# паліндромом (однаковий, читається зліва направо і справа наліво).

def is_palindrome(word):
    length = len(word)

    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False

    return True


word = input("Введіть слово для перевірки: ").lower()

if is_palindrome(word):
    print(f"'{word}' є паліндромом.")
else:
    print(f"'{word}' не є паліндромом.")
