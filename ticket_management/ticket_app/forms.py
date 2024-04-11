from django.contrib.auth.forms import UserCreationForm
from .models import User1
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User1
        fields = ("username", "email", "password1", "password2")


class UserRoleForm(forms.Form):
    ROLES_CHOICES = [
        ("PM", "PM"),
        ("Python-TL", "Python-TL"),
        ("JS-TL", "JS-TL"),
        ("Python Developer", "Python Developer"),
        ("JS-Developer", "JS-Developer"),
    ]
    user_role = forms.ChoiceField(choices=ROLES_CHOICES)
