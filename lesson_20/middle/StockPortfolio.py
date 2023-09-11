# Біржовий портфель: Розробіть клас для ведення обліку біржового портфелю з можливістю додавання акцій,
# обчислення загальної вартості та видалення акцій.
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'ℹ️ Акцiя "{self.name}", цiна {self.price} у.о.'


class Portfolio:
    def __init__(self):
        self.stocks = {}

    def __str__(self):
        return 'Біржовий портфель:\n' + '\n'.join(f'{stock_data["stock"]} - {stock_data["quantity"]} шт.'
                                                     for stock_data in self.stocks.values())

    def add_stock(self, stock, quantity):
        if stock.name in self.stocks:
            self.stocks[stock.name]['quantity'] += quantity
        else:
            self.stocks[stock.name] = {'stock': stock, 'quantity': quantity}

        print(f'✅ Акцiя {stock.name} успiшно додана до портфелю.')

    def remove_stock(self, stock, quantity=None):
        if stock.name in self.stocks:
            if quantity is None or self.stocks[stock.name]['quantity'] <= quantity:
                del self.stocks[stock.name]
            else:
                self.stocks[stock.name]['quantity'] -= quantity

            print('✅ Успiшно!')
        else:
            print(f'❌ Акцiя "{stock.name}" не знайдена в портфелi.')

    def total_value(self):
        return sum(stock_data['stock'].price * stock_data['quantity'] for stock_data in self.stocks.values())


apple = Stock('Apple', 150)
google = Stock('Google', 2800)

portfolio = Portfolio()
portfolio.add_stock(apple, 10)
portfolio.add_stock(google, 5)

portfolio.add_stock(apple, 22)
portfolio.remove_stock(apple, 3)

print(portfolio)

print(f'Загальна вартiсть бiржового портфелю: {portfolio.total_value()} у.о.')
