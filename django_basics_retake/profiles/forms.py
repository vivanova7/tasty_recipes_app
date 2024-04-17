from django import forms

from django_basics_retake.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("nickname", "first_name", "last_name", "chef")

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("nickname", "first_name", "last_name", "chef", "bio")

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }
