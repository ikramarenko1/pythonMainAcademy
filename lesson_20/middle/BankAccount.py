# Банківський рахунок: Розробіть клас для банківського рахунку з можливістю
# додавання, зняття грошей та перевірки балансу.
import time


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Банкiвський рахунок "{self.name}":\n' \
               f'   Назва: {self.name}\n' \
               f'   Поточний баланс: {self.balance} у.о.'

    def replenish(self, money):
        print(f'Проводжу операцiю на поповнення на суму {money} у.о...')
        time.sleep(2)

        self.balance += money

        print(f'Дякуємо за поповнення банківського рахунку "{self.name}"! Оплата пройшла успiшно!')

    def withdraw(self, money):
        print(f'Проводжу операцiю на зняття з рахунку на суму {money} у.о...')
        time.sleep(2)

        self.balance -= money

        print(f'Дякуємо за користування банківським рахунком "{self.name}"! '
              f'Зняття готiвки в розмiрi {money} у.о. пройшло успiшно!')

    def check_balance(self):
        print(f'Поточний баланс банківського рахунку "{self.name}": {self.balance} у.о.')


monobank = BankAccount('monobank', 500)

print(monobank)

monobank.replenish(54232)
monobank.check_balance()

monobank.withdraw(2000)
monobank.check_balance()