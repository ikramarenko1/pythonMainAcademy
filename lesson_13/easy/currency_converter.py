# Конвертер валют: Реалізуйте програму-конвертер валют, яка перетворює суму
# з однієї валюти в іншу. Обробте можливі помилки, наприклад, введення некоректних
# значень або недоступності валютного курсу.

# Актуально на 18.08.2023
rates = {
    'USD_EUR': 0.91,
    'EUR_USD': 1.08,
    'UAH_USD': 0.027,
    'USD_UAH': 36.93,
    'UAH_EUR': 0.025,
    'EUR_UAH': 40.13
}


def get_exchange_rate(from_currency, to_currency):
    return rates.get(f'{from_currency}_{to_currency}')


print('Актуальнi валютнi пари на даний момент:')
for key in rates.keys():
    print(key)

amount = input('Введiть суму для конвертації: ')
from_cur = str(input('Введiть валюту з якої конвертувати: ')).strip().upper()
to_cur = str(input('Введiть валюту в яку конвертувати: ')).strip().upper()

try:
    amount = float(amount)
except ValueError:
    print('Введена некорректна сума, повторiть введення.')
else:
    exchange_rate = get_exchange_rate(from_cur, to_cur)

    if exchange_rate is None:
        print('Неможливо отримати курс для цїєї валютної пари.')
    else:
        result = exchange_rate * amount
        print(f'Результат: {result} {to_cur}')
