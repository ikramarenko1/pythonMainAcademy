# Мовний перекладач: Розробіть систему для створення об'єктів, які здійснюють переклад тексту на різні мови.
# Користувач може вибирати потрібну мову для перекладу.
class Translator:
    def translate(self, text):
        raise NotImplementedError('Підкласи повинні реалізовувати цей метод')


class EnglishToUkrainianTranslator(Translator):
    def __init__(self):
        self.dictionary = {'hello': 'привiт', 'world': 'свiт'}

    def translate(self, text):
        return ' '.join(self.dictionary.get(word, word) for word in text.split(' '))


class EnglishToFrenchTranslator(Translator):
    def __init__(self):
        self.dictionary = {'hello': 'bonjour', 'world': 'monde'}

    def translate(self, text):
        return ' '.join(self.dictionary.get(word, word) for word in text.split(' '))


class TranslatorFactory:
    @staticmethod
    def create_translator(language):
        if language == 'Ukrainian':
            return EnglishToUkrainianTranslator()
        elif language == 'French':
            return EnglishToFrenchTranslator()
        else:
            raise ValueError(f'Переклад на {language} не підтримується')


user_choice = input('Введіть цільову мову (Ukrainian/French): ')
translator = TranslatorFactory.create_translator(user_choice)
input_text = 'hello world'

print(translator.translate(input_text))
