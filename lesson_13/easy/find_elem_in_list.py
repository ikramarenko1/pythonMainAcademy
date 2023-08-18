# Пошук елементу в списку: Напишіть програму, яка шукає певний елемент у списку,
# введеному користувачем. Обробте випадок, коли такого елементу немає в списку.
user_list = ['hello', 'world', 'some', 'string']
elem = input('Введiть елемент зi списку який потрiбен: ')

try:
    if elem in user_list:
        print(f'{elem} є в списку!')
    else:
        raise Exception
except Exception as e:
    print(f'Елемент не знайдений! {e}')
