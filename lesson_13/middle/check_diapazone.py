# Перевірка діапазону: Напишіть функцію, яка приймає число від користувача та перевіряє, чи воно знаходиться в
# діапазоні від 1 до 10. Якщо число відповідає діапазону, виведіть повідомлення "Число в діапазоні". Якщо ні,
# виведіть повідомлення "Число поза діапазоном".

try:
    user_input = int(input('Введiть число: '))

    if user_input < 1 or user_input > 10:
        raise Exception('Число поза діапазоном')
except ValueError:
    print('Введене значення некоректне.')
except Exception as e:
    print(e)
else:
    print('Число в діапазоні')
