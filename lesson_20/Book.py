# Створіть клас Книга, який має атрибути назва і автор. Виведіть інформацію про книгу.

# Розширте клас Книга, додавши метод прочитати, який виводить рядок про те, що книга була прочитана.

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def about(self):
        print(f'Iнформацiя про книгу "{self.name}":\n   Назва: "{self.name}"\n   Автор: {self.author}')

    def read(self):
        print(f'Вiтаю! Книга "{self.name}" була повнiстю прочитана!')


rule10x = Book('10X Rule', 'Grant Cardone')
atomic_habits = Book('Atomic Habits', 'James Clear')

rule10x.about()
rule10x.read()

atomic_habits.about()
