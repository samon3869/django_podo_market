import string
from django.core.exceptions import ValidationError


def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False


def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False


def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False


def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password)
        ):
            raise ValidationError("8자이상, 영문 대소문자, 숫자를 포함해야 함")
    
    def get_help_text(self):
        return ("8자이상, 영문 대소문자, 숫자를 포함해야 함")

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없음")
