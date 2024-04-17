from django.core.exceptions import ValidationError


def time_validator(value):
    if value < 1:
        raise ValidationError("Time cannot be below 1")
