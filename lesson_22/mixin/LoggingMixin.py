# Логування дій об'єктів для аналізу:
# Створіть мікс, який буде логувати дії об'єктів для подальшого аналізу та відстеження роботи програми.
# Це може бути корисним при відлагодженні та профілюванні додатків.
import logging

logging.basicConfig(level=logging.INFO)


class LoggingMixin:
    def log_action(self, action, message):
        logger = logging.getLogger(self.__class__.__name__)
        logger.info(f"{action}: {message}")


class MyClass(LoggingMixin):
    def __init__(self, name):
        self.name = name

    def do_something(self):
        self.log_action("DO_SOMETHING", f"{self.name} щось виконує")

    def do_something_else(self, param):
        self.log_action("DO_SOMETHING_ELSE", f"{self.name} щось виконує з {param}")


obj = MyClass("MyObject")
obj.do_something()
obj.do_something_else("parameter money 999")
