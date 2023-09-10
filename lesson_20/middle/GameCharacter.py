# Ігровий персонаж: Розробіть клас для ігрового персонажа з можливістю руху, атак та збереження стану персонажа.
class GameCharacter:
    def __init__(self, name, health=100, strength=10):
        self.name = name
        self.health = health
        self.strength = strength
        self.position = (0, 0)
        self.history = []

    def __str__(self):
        return f'ℹ️ Персонаж "{self.name}":\n' \
               f'    Здоров`я: {self.health}\n' \
               f'    Сила: {self.strength}\n' \
               f'    Позицiя: {self.position}'

    def move(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            if x > 2 or y > 2:
                print(f'❌ Персонаж "{self.name}" не може рухатись бiльш нiж на 2 клiтинки по x/y!')
            else:
                self.position = (self.position[0] + x, self.position[1] + y)
                print(f'✅ Персонаж "{self.name}" рухається на {self.position}')
        else:
            print(f'❌ Потрiбно вказати числа!')

    def attack(self, character):
        if isinstance(character, GameCharacter):
            character.health -= self.strength
            print(f'✅ Персонаж "{self.name}" наносить персонажу "{character.name}" {self.strength} урону. '
                  f'У "{character.name}" залишилось {character.health} хп.')
        else:
            print(f'❌ Персонаж "{self.name}" не може атакувати "{character}"!')

    def save(self):
        self.history.append((self.health, self.position))
        print(f'✅ Персонаж "{self.name}" зберiг стан!')

    def restore(self):
        if self.history:
            self.health, self.position = self.history.pop()
            print(f'✅ Персонаж "{self.name}" відновив попередній стан!')
        else:
            print(f'❌ Персонаж "{self.name}" не має станів для відновлення.')


player1 = GameCharacter('Player 1', 100, 10)
player2 = GameCharacter('Player 2', 120, 15)

print(player1)
print(player2)

print('----' * 3)

player1.move(2, 2)
player2.move(1, 2)

print('----' * 3)

player1.attack(player2)

print('----' * 3)

player1.attack(123)

print('----' * 3)

player2.save()

print('----' * 3)

player1.attack(player2)

print('----' * 3)

player2.restore()
print(player2)
