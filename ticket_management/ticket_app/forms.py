from django.contrib.auth.forms import UserCreationForm
from .models import User1
from django import forms
from django.db.models import Q


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
        ("JS Developer", "JS Developer"),
    ]
    user_role = forms.ChoiceField(choices=ROLES_CHOICES)


class AssignPMForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pm"] = forms.ModelChoiceField(
            queryset=User1.objects.filter(role="PM"), empty_label="Select PM"
        )

    def clean_pm_users(self):
        selected_pm = self.cleaned_data["pm"]
        if selected_pm:
            return selected_pm
        else:
            return None


class AssignTLForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tl"] = forms.ModelChoiceField(
            queryset=User1.objects.filter(Q(role="Python-TL") | Q(role="JS-TL")),
            empty_label="Select TL",
        )

    def clean_tl_users(self):
        selected_tl = self.cleaned_data["tl"]
        if selected_tl:
            return selected_tl
        else:
            return None
