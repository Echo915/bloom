from django.forms import PasswordInput, TextInput, EmailInput, CharField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("rank",)
        fields = UserCreationForm.Meta.fields + (("email"),)
        widgets = {
            "password1": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Password",
            }),
            "password2": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the same password as before",
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
        fields = ["username", "email",]
        widgets = {
            # "password": PasswordInput(attrs={
            #     "class": "form-control",
            #     "placeholder": "Enter Password",
            # }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "example@example.com"
            }),
            "username": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Username",
            })
        }
