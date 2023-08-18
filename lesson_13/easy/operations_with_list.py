# Робота зі списками: Реалізуйте програму, яка дозволяє користувачеві додавати та видаляти
# елементи зі списку. Обробте можливі помилки, які можуть виникнути при доступі до індексу,
# який не існує.
def print_menu():
    print()
    print('0. Вийти з програми')
    print('1. Додати елемент до списку')
    print('2. Видалили елемент iз списку')
    print('3. Вивести поточний список')
    print()


user_list = []

while True:
    print_menu()

    choice = int(input('Виберiть опцiю: '))

    if choice == 0:
        print('Дякую за використання програми!')
        break

    elif choice == 1:
        elem = input('Введiть елемент, який додати до списку: ')
        user_list.append(elem)

        print('Елемент успiшно додано!')

    elif choice == 2:
        index = input('Введiть iндекс елементу, який видалити iз списку: ')
        try:
            index = int(index)
            removed_elem = user_list.pop(index)

            print(f'Видалено елемент {removed_elem}')
        except ValueError:
            print('Введено некорректний iндекс.')
        except IndexError:
            print('Iндекс знаходиться не в межах списку.')

    elif choice == 3:
        print(f'Поточний список - {user_list}')
