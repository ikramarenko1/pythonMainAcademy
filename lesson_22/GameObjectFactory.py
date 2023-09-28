# Ігровий генератор: Створіть фабричний метод для генерації різноманітних ігрових об'єктів,
# таких як персонажі, зброя, монстри тощо. Генерація може відбуватися з урахуванням параметрів
# або на основі випадкових значень.
import random


class GameObject:
    def interact(self):
        raise NotImplementedError('Підкласи повинні реалізовувати цей метод')


class Character(GameObject):
    def interact(self):
        return 'Персонаж: Взаємодія з гравцем'


class Weapon(GameObject):
    def interact(self):
        return 'Зброя: підбирається гравцем'


class Monster(GameObject):
    def interact(self):
        return 'Монстр: Атакує гравця'


class GameObjectFactory:
    @staticmethod
    def create_object(object_type):
        if object_type == 'Character':
            return Character()
        elif object_type == 'Weapon':
            return Weapon()
        elif object_type == 'Monster':
            return Monster()
        else:
            raise ValueError(f'Тип об\'єкта {object_type} не розпізнано')


user_choice = input('Введіть тип ігрового об\'єкта (Character/Weapon/Monster) або "random": ')

if user_choice == 'random':
    user_choice = random.choice(['Character', 'Weapon', 'Monster'])

game_object = GameObjectFactory.create_object(user_choice)

print(game_object.interact())
