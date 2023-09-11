# Менеджер проекту: Створіть клас, який дозволить створювати та керувати проектами,
# включаючи додавання завдань, присвоєння завдань користувачам і визначення стану проекту.
from enum import Enum


class Status(Enum):
    NEW = '🆕 Нове.'
    ON_HOLD = '⏳ На очiкуваннi.'
    IN_PROGRESS = '🧑‍💻 В роботі.'
    COMPLETED = '✅ Завершено!'


class User:
    def __init__(self, name, user_type):
        self.name = name
        self.user_type = user_type
        self.projects = []

    def __str__(self):
        return f'ℹ️ Iнформацiя про користувача:\n' \
               f'   Ім`я: {self.name}\n' \
               f'   Тип користувача: {self.user_type}\n' \
               f'   Проекти: ' + ', '.join([f'{project.name}: {project.status.value}'
                                            for project in self.projects])


class Task:
    def __init__(self, name):
        self.name = name
        self.user = None
        self.status = Status.NEW

    def __str__(self):
        return f'ℹ️ Iнформацiя про таск:\n' \
               f'   Назва: {self.name}\n' \
               f'   Вiдповiдальний: {self.user.name}\n' \
               f'   Статус: {self.status.value}'

    def set_user(self, user):
        if isinstance(user, User):
            self.user = user
            user.projects.append(self)

            print(f'{self.name.upper()}: ✅ Користувача {user.name} назначено вiдповiдальним.')
        else:
            print(f'{self.name.upper()}: ❌ Неможливо встановити {user} вiдповiдальним.')

    def set_status(self, status):
        if isinstance(status, Status):
            self.status = status
            print(f'{self.name.upper()}: ✅ Встановлено статус {status}.')
        else:
            print(f'{self.name.upper()}: ❌ Неможливо встановити статус {status}.')

    def get_status(self):
        print(f'{self.name.upper()}: ℹ️ Статус {self.status.value}')


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.status = Status.ON_HOLD

    def __str__(self):
        return f'ℹ️ Iнформацiя про проект:\n' \
               f'   Назва: {self.name}\n' \
               f'   Завдання: {", ".join([task.name for task in self.tasks])}\n' \
               f'   Статус: {self.status.value}'

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
            print(f'{self.name.upper()}: ✅ Додано таск {task.name} до проекту.')
        else:
            print(f'{self.name.upper()}: ❌ Неможливо додати {task} до проекту.')

    def remove_task(self, task):
        if isinstance(task, Task):
            if task in self.tasks:
                self.tasks.append(task)
                print(f'{self.name.upper()}: ✅ Видалено таск {task.name} з проекту.')
            else:
                print(f'{self.name.upper()}: ❌ Неможливо видалити {task.name} з проекту, так як його немає.')
        else:
            print(f'{self.name.upper()}: ❌ Неможливо додати {task} до проекту.')

    def set_status(self, status):
        if isinstance(status, Status):
            self.status = status
            print(f'{self.name.upper()}: ✅ Встановлено статус {status.value}.')
        else:
            print(f'{self.name.upper()}: ❌ Неможливо встановити статус {status}.')

    def get_all_tasks(self):
        return ", ".join([f'{task.name}: {task.status}' for task in self.tasks])


# ==== MAIN ====
ilya = User('Ilya', 'tech')
maxim = User('Maxim', 'tech')
sasha = User('Sasha', 'copywriter')
albert = User('Albert', 'designer')

make_ui = Task('Make UX/UI')
make_module = Task('Make Finance Module')
make_module2 = Task('Make Finance Module 2')
make_adv_post = Task('Make Advertising Post')

project = Project('New Project')

make_ui.set_user(albert)
make_module.set_user(ilya)
make_module2.set_user(maxim)
make_adv_post.set_user(sasha)
print('----' * 3)

project.add_task(make_ui)
project.add_task(make_module)
project.add_task(make_module2)
project.add_task(make_adv_post)
print('----' * 3)

print(project)
print('----' * 3)

make_ui.set_status(Status.COMPLETED)
make_module.set_status(Status.COMPLETED)
print('----' * 3)

print(ilya)
print(sasha)
