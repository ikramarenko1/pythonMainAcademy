# Рядки: Створіть програму, яка приймає рядок від користувача та перевіряє,
# чи є він паліндромом (читається однаково зліва направо та справа наліво).

def if_palindrome(string):
    for i in range(len(string)):
        if string[i].lower() == string[-i-1].lower():
            return True
        else:
            return False


string = str(input('Введiть рядок для перевiрки на палiндром: '))

print(if_palindrome(string))