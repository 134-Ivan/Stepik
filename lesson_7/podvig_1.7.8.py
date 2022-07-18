from string import ascii_lowercase, digits
import re


class CardCheck:
    # CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    card_template = re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}')
    name_template = re.compile(r'^[A-Z]*\s[A-Z]*$')

    @classmethod
    def check_card_number(cls, number):
        return True if cls.card_template.match(number) else False

    @classmethod
    def check_name(cls, name):
        return True if cls.name_template.match(name) else False


is_number = CardCheck.check_card_number("134-5678-9012-0000")
print(is_number)

is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_name)
