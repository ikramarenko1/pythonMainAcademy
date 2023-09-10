# Бібліотека книг: Розробіть клас для представлення книг та бібліотеки з можливістю додавання книг,
# пошуку та видачі книг користувачам.
class User:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.owner = None

    def __str__(self):
        return f'ℹ️ Iнформацiя про книгу "{self.name}":\n' \
               f'    Автор: {self.author}\n' \
               f'    Власник: {self.owner}'

    def set_owner(self, user):
        if isinstance(user, User):
            self.owner = f'{user.surname} {user.name}'
            print(f'✅ Людину {user.surname} {user.name} успiшно встановлено як власника для книги "{self.name}"!')


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return f'ℹ️ Iнформацiя про бiблiотеку:\n' \
               f'    Назва: {self.name}' \
               f'    Книжки та власники: ' + ', '.join([f'"{book.name}" - {book.author}: {book.owner}' for book in self.books])

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f'✅ Книгу "{book.name}" успiшно додано до бiблiотеки "{self.name}".')

        else:
            print(f'❌ Неможливо додати {book}, бо це не книга.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'✅ Книгу "{book.name}" видалено з бiблiотеки "{self.name}".')

        else:
            print(f'❌ Неможливо видалити {book}, так як її немає.')

    def search_book(self, book):
        if isinstance(book, Book):
            if book in self.books:
                print('✅ Знайдено!')
                print(book)
            else:
                print('❌ Не знайдено.')
        else:
            print(f'❌ Неможливо знайти {book}, бо це не книга.')


ilya = User('Kramarenko', 'Ilya')
sasha = User('Pyskun', 'Oleksandra')

rule10x = Book('10X Rule', 'Grant Cardone')
atomic_habits = Book('Atomic Habits', 'James Clear')
habits = Book('The 7 Habits of Highly Effective People', 'Stephen R. Covey')

lib = Library('eKnigarnya')

lib.add_book(rule10x)
lib.add_book(atomic_habits)
lib.add_book(habits)
lib.add_book(213123)
print('----' * 3)

rule10x.set_owner(ilya)
habits.set_owner(ilya)
atomic_habits.set_owner(sasha)
print('----' * 3)

lib.search_book(rule10x)
lib.remove_book(rule10x)
lib.search_book(rule10x)
