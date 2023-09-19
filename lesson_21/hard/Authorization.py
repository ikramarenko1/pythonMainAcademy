# Авторизація: Розробіть систему авторизації з використанням класу User.
# Зберігайте інформацію про користувачів (логіни та паролі) в приватних змінних. Реалізуйте методи для
# перевірки пароля та створення нових облікових записів.
class User:
    def __init__(self):
        self.__logins = []
        self.__passwords = []

    def register(self, login, password):
        if login in self.__logins:
            print('ВIДМОВА: Користувач з таким логiном вже існує.')
        else:
            self.__logins.append(login)
            self.__passwords.append(password)
            print(f'УСПIХ: Користувача {login} внесено до бази.')

            return True

        return False

    def authenticate(self, login, password):
        if login in self.__logins:
            login_index = self.__logins.index(login)

            if password == self.__passwords[login_index]:
                print(f'УСПIХ: Вітаємо в системі, {login}!')
                return True
            else:
                print('ВIДМОВА: Пароль не вiрний!')

        else:
            print('ВIДМОВА: Користувача з таким логiном не знайдено.')

        return False


auth_sys = User()

auth_sys.register('admin', 'qwerty12345')
auth_sys.register('test', 'test123')

auth_sys.authenticate('admin', 'qwerty12345')
auth_sys.authenticate('user', 'test123')
