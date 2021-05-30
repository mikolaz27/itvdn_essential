from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    fullname = forms.CharField(label="First name")

    class Meta:
        model = User
        fields = ("last_name", "fullname", "email", "password1")
