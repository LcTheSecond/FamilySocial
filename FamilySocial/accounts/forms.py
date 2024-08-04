# -------------------------------------------------
# Django imports
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# In-App Imports
from .models import CustomUser


# Other App Imports


# Code:
class CreateUserForm(UserCreationForm):
    """#TODO Make a Doc String"""

    class Meta:
        """#TODO Make a Doc String"""

        model = CustomUser
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    """#TODO Make a Doc String"""

    username = forms.CharField(
        widget=TextInput(attrs={"placeholder": "Usuário"}), label=""
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={"placeholder": "Senha"}), label=""
    )