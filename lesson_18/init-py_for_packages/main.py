# Використання __init__.py для пакетів:
# Створіть папку my_package і всередині неї два файли: module1.py та module2.py. У __init__.py вказати, які модулі
# повинні бути доступні при імпорті пакету. В module1.py та module2.py створіть функції. У головному файлі програми
# імпортуйте та використовуйте функції з пакету.
from my_package import function_from_module1, function_from_module2

function_from_module1()
function_from_module2()
