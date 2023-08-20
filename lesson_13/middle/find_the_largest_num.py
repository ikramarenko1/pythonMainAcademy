# Пошук найбільшого числа: Напишіть програму, яка приймає список чисел від користувача та
# знаходить найбільше число у списку. Обробте випадок, коли список порожній, виведіть повідомлення "Список порожній".

try:
    user_input = input('Введiть список чисел через символ пробiлу: ')
    numbers = list(map(int, user_input.split()))

    if not numbers:
        raise Exception('Список порожній')

    print(f'Найбільше число у списку - {max(numbers)}')

except ValueError:
    print('Введено некоректнi данi.')
except Exception as e:
    print(e)
