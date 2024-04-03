from django.forms import PasswordInput, TextInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("rank",)
        fields = ["username", "email", "rank", "password"]
        widgets = {
            "password": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Password",
            }),
            "email": EmailInput(attrs={
                "required": "true",
                "class": "form-control",
                "placeholder": "example@example.com",
            }), 
            "username": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Username",
            })
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ["username", "email", "rank", "password"]
        widgets = {
            "password": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Password",
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "example@example.com"
            }),
            "username": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Username",
            })
        }