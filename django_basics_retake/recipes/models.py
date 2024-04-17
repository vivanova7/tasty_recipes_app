from django.core.validators import MinLengthValidator
from django.db import models

from django_basics_retake.profiles.models import Profile
from django_basics_retake.recipes.recipe_validators import time_validator


# Create your models here.
class Recipe(models.Model):
    MIN_TITLE_LENGTH = 10
    MAX_TITLE_LENGTH = 100

    MAX_CUISINE_TYPE_LENGTH = 7

    CUISINE_TYPES = [
        ("French", "French"),
        ("Chinese", "Chinese"),
        ("Italian", "Italian"),
        ("Balkan", "Balkan"),
        ("Other", "Other"),
    ]

    title = models.CharField(
        unique=True,
        max_length=MAX_TITLE_LENGTH,
        error_messages={"unique": "We already have a recipe with the same title!"},

        validators=(
            MinLengthValidator(MIN_TITLE_LENGTH),
        ),
    )

    cuisine_type = models.CharField(
        max_length=MAX_CUISINE_TYPE_LENGTH,
        choices=CUISINE_TYPES,
        null=False,
        blank=False,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space.",
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        validators=(
            time_validator,
        ),
        help_text="Provide the cooking time in minutes.",
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )