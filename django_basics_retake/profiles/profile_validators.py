from django.core.exceptions import ValidationError


def validate_username(username):
    if len(username) < 2:
        raise ValidationError("Nickname must be at least 2 chars long!")

def validate_name(name):
    if not name[0].isupper():
        raise ValidationError("Name must start with a capital letter!")