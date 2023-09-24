# Валідація даних: Створіть клас Validator з класовим методом для перевірки правильності введених даних.
import re


class Validator:
    @classmethod
    def validate_email(cls, email):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if email_regex.match(email):
            print(f"Почта {email} є валідною.")
        else:
            print(f"Почта {email} не є валідною.")

    @classmethod
    def validate_phone_number(cls, phone_number):
        phone_regex = re.compile(r"^\+?(\d[\d\- ]+)?(\([\d\- ]+\))?[\d\- ]+\d$")

        if phone_regex.match(phone_number):
            print(f"Телефонний номер {phone_number} є валідним.")
        else:
            print(f"Телефонний номер {phone_number} не є валідним.")


Validator.validate_email("test@example.com")
Validator.validate_email("invalid_example.com")
Validator.validate_phone_number("+38(099)-111-11-11")
Validator.validate_phone_number("sadw123213")
