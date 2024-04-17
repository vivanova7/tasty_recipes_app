from django.core.validators import MinLengthValidator
from django.db import models

from django_basics_retake.profiles.profile_validators import validate_username, validate_name


class Profile(models.Model):
    MIN_NICKNAME_LENGTH = 2
    MAX_NICKNAME_LENGTH = 20

    MAX_FIRST_LAST_NAME_LENGTH = 30

    nickname = models.CharField(
        unique=True,
        max_length=MAX_NICKNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NICKNAME_LENGTH),
            validate_username,
        ),
        null=False,
        blank=False,
        verbose_name='Nickname',
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_LAST_NAME_LENGTH,
        validators=(
            validate_name,
        ),
        null=False,
        blank=False,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_FIRST_LAST_NAME_LENGTH,
        validators=(
            validate_name,
        ),
        null=False,
        blank=False,
        verbose_name='Last Name',
    )

    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
        verbose_name='Chef',
    )

    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='Bio',
    )
