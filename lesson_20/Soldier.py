# Створіть клас Поручик, який має атрибут звання та метод привітати, який виводить рядок з
# привітанням на основі звання (наприклад, "Привіт, Поручик!").
class Soldier:
    def __init__(self, name, rank='Поручик'):
        self.name = name
        self.rank = rank

    def say_hi(self):
        print(f'Привiт, {self.rank} {self.name}!')


lieutenant = Soldier('Володимир', 'Лейтенант')

lieutenant.say_hi()
