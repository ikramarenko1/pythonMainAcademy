# Банківський рахунок: Створіть клас BankAccount, який має приватні змінні балансу
# і номеру рахунку. Реалізуйте методи для додавання та зняття коштів, а також метод
# для перевірки балансу. Забезпечте захист від несанкціонованого доступу до змінних.
class BankAccount:
    def __init__(self, name, number, balance=0):
        self.name = name
        self.__number = number
        self.__balance = balance

    def add_to_balance(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__balance += value
            print(f'Рахунок "{self.name.upper()}": Успiшно додано до балансу {value} у.о.')
        else:
            print(f'Рахунок "{self.name.upper()}": Вiдмовлено! {value} повинно бути числом та бiльше 0!')

    def get_from_balance(self, value):
        if isinstance(value, (int, float)) and value > 0:
            if self.__balance >= value:
                self.__balance -= value
                print(f'Рахунок "{self.name.upper()}": Успiшно знято з балансу {value} у.о.')
            else:
                print(f'Рахунок "{self.name.upper()}": Вiдмовлено! Недостатньо коштiв.')
        else:
            print(f'Рахунок "{self.name.upper()}": Вiдмовлено! {value} повинно бути числом та бiльше 0!')

    def get_balance(self):
        return f'Рахунок "{self.name.upper()}": поточний баланс = {self.__balance} у.о.'


monobank = BankAccount('monobank', '5375 4141 0101 0101')
monobank.add_to_balance(10000)
monobank.add_to_balance(-20)

monobank.get_from_balance(3700)
monobank.get_from_balance(-100)

print(monobank.get_balance())
