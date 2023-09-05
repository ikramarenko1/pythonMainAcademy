# Аліаси та груповий імпорт:
# Створіть два модулі (наприклад, module1.py і module2.py), кожний з яких містить по одній функції.
# У головному файлі main.py зробіть груповий імпорт функцій з обох модулів з аліасами.
# Використовуйте аліаси для зручного звертання до функцій.
from module1 import function_from_module1 as say_hello1
from module2 import function_from_module2 as say_hello2

say_hello1()
say_hello2()
