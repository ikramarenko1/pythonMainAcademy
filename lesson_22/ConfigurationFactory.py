# Конфігуратор веб-сервісу: Створіть фабричний метод для створення об'єктів,
# які налаштовують параметри веб-сервісу (наприклад, налаштування безпеки,
# кешування або аутентифікації) згідно з вимогами користувача.
class WebServiceConfiguration:
    def apply(self):
        raise NotImplementedError('Підкласи повинні реалізовувати цей метод')


class SecurityConfiguration(WebServiceConfiguration):
    def apply(self):
        return 'Застосування конфігурації безпеки'


class CachingConfiguration(WebServiceConfiguration):
    def apply(self):
        return 'Застосування конфігурації кешування'


class AuthenticationConfiguration(WebServiceConfiguration):
    def apply(self):
        return 'Застосування конфігурації автентифікації'


class ConfigurationFactory:
    @staticmethod
    def create_configuration(config_type):
        if config_type == 'Security':
            return SecurityConfiguration()
        elif config_type == 'Caching':
            return CachingConfiguration()
        elif config_type == 'Authentication':
            return AuthenticationConfiguration()
        else:
            raise ValueError(f'Тип конфігурації {config_type} не розпізнано')


user_choice = input('Введіть тип конфігурації (Security/Caching/Authentication): ')
configuration = ConfigurationFactory.create_configuration(user_choice)

print(configuration.apply())
