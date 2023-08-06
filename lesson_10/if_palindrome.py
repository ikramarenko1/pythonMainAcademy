# Перевірка рядка на паліндром

def if_palindrome(string):
    for i in range(len(string)):
        if string[i].lower() == string[-i-1].lower():
            return True
        else:
            return False


string = str(input('Введiть рядок для перевiрки на палiндром: '))

print(if_palindrome(string))