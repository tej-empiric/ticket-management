from django.contrib.auth.forms import UserCreationForm
from .models import User1
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User1
        fields = ("username", "email", "password1", "password2")


