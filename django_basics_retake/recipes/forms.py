from django import forms

from django_basics_retake.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']

        widgets = {
            'ingredients': forms.Textarea(attrs={
                'placeholder': 'ingredient1, ingredient2, ...',
            }),

            'instructions': forms.Textarea(attrs={
                'placeholder': 'Enter detailed instructions here...',
            }),

            'image_url': forms.URLInput(attrs={
                'placeholder': 'Optional image URL here...',
            }),
        }