# Гра "Двадцять одно" (Blackjack):
# Ми реалізуємо просту версію гри "Двадцять одно", де гравець може брати картки
# і намагатися набрати 21 очко. Використовуємо цикли для управління ходом гри та взаємодії з гравцем.

import random


def blackjack():
    # * 4 тому, що в картах 4 масти, так я множу список i вiдтворюю реальну колоду
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(deck)

    print('Ласкаво просимо до гри Blackjack!')

    player_hand = [deck.pop(), deck.pop()]
    print(f'\nВашi карти: {player_hand} з сумарною кiлькiстю {sum(player_hand)}')

    while sum(player_hand) < 21:
        action = input('Хочете додати чи залишити? (введiть першу лiтеру) ').lower()

        if action == "д":
            player_hand.append(deck.pop())
            print(f'\nВашi карти: {player_hand} з сумарною кiлькiстю {sum(player_hand)}')
        elif action == "з":
            break

    if sum(player_hand) == 21:
        print('Вітаємо! У Вас Blackjack!')
    elif sum(player_hand) > 21:
        print('Ви перевищили 21, на жаль. :(')
    else:
        print(f'Ви вирiшили залишитися з {sum(player_hand)} очками.')


blackjack()
