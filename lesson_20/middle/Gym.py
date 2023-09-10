# Спортивний зал: Розробіть систему для керування спортивним залом з
# можливістю реєстрації клієнтів, запису на тренування та ведення обліку абонементів.
import datetime


class Gym:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.trainings = []
        self.subscriptions = []

    def __str__(self):
        return f'==========\n' \
               f'Iнформацiя про спортивний зал "{self.name}":\n' \
               f'Назва: "{self.name}"\n' \
               f'Клієнти: {", ".join([client.name for client in self.clients])}\n' \
               f'Тренування: {", ".join([training.name for training in self.trainings])}\n' \
               f'Абонементи: {", ".join([subscription.name for subscription in self.subscriptions])}\n' \
               f'=========='

    def add_client(self, client):
        self.clients.append(client)
        print(f'Клієнта {client.name} успiшно записано до спортивного залу "{self.name}".')

    def remove_client(self, client):
        self.clients.append(client)
        print(f'Клієнта {client.name} виключено з спортивного залу "{self.name}".')

    def add_training(self, training):
        self.trainings.append(training)
        print(f'Додано тренування "{training.name}" до спортивного залу "{self.name}".')

    def remove_training(self, training):
        self.trainings.remove(training)
        print(f'Видалено тренування "{training.name}" з спортивного залу "{self.name}".')

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)
        print(f'Додано абонемент "{subscription.name}" до спортивного залу "{self.name}".')

    def remove_subscription(self, subscription):
        self.subscriptions.remove(subscription)
        print(f'Видалено абонемент "{subscription.name}" з спортивного залу "{self.name}".')


class Training:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def __str__(self):
        return f'Тренування "{self.name}":\n' \
               f'Клієнти: ' + ', '.join([client.name for client in self.clients])

    def add_client(self, client):
        self.clients.append(client)
        print(f'Клієнта {client.name} успiшно записано на тренування "{self.name}".')

    def remove_client(self, client):
        self.clients.remove(client)
        print(f'Клієнта {client.name} виключено з тренування "{self.name}".')


class Subscription:
    def __init__(self, name, days=30):
        self.name = name
        self.days = days

    def __str__(self):
        return f'Абонемент "{self.name}", дiйснiсть: {self.days} днiв.'


class Client:
    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.subscription = None

    def __str__(self):
        return f'Інформація про клієнта {self.name}:\n' \
               f'    Iм`я: {self.name}\n' \
               f'    Прiзвище: {self.surname}\n' \
               f'    Номер телефону: {self.phone}\n' \
               f'    Абонемент: {self.subscription}'

    def add_subscription(self, subscription):
        self.subscription = subscription
        print(f'Додано абонемент "{subscription.name}" для "{self.name} {self.surname}".')


# ==== MAIN ====
remaster = Gym('Re:Master')

strength_training = Training('Силове тренування')
cardio_training = Training('Кардiо тренування')

days30 = Subscription('Мiсячний', 30)
days90 = Subscription('Три по цiнi двух!', 90)
days30_pool = Subscription('Мiсячний з басейном!', 30)

person1 = Client('Крамаренко', 'Iлья', '099-111-11-11')
person2 = Client('Пискун', 'Олександра', '099-222-22-22')
person3 = Client('Шевченко', 'Михайло', '099-333-33-33')

print('----' * 3)
remaster.add_client(person1)
remaster.add_client(person2)
remaster.add_client(person3)
print('----' * 3)

remaster.add_training(strength_training)
remaster.add_training(cardio_training)
print('----' * 3)

remaster.add_subscription(days30)
remaster.add_subscription(days30_pool)
print('----' * 3)

print(remaster)
print('----' * 3)

remaster.remove_client(person3)
remaster.remove_subscription(days30_pool)
remaster.add_subscription(days90)
print('----' * 3)

print(remaster)
print('----' * 3)

strength_training.add_client(person1)
strength_training.add_client(person2)
cardio_training.add_client(person1)
print('----' * 3)

print(strength_training)
print(cardio_training)
print('----' * 3)

print(days30)
print(days90)
print('----' * 3)

person1.add_subscription(days90)
person2.add_subscription(days30_pool)
print('----' * 3)

print(person1)
print(person2)
print('----' * 3)
