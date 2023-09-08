# Створіть клас Калькулятор_кредитів, який має атрибути сума_кредиту і відсоткова_ставка.
# Додайте метод розрахувати відсотки, який обчислює розмір відсотків за перший місяць
# (сума_кредиту * відсоткова_ставка / 12).
class Credit_calculator:
    def __init__(self, loan_amount, payment_rate):
        self.loan_amount = loan_amount
        self.payment_rate = payment_rate

    def get_payment_rate_for_first_month(self):
        return f'Розмір відсотків за перший місяць = {self.loan_amount * (self.payment_rate / 100) / 12} грн.'


credit1 = Credit_calculator(12392, 12)

print(credit1.get_payment_rate_for_first_month())
