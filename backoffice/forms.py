from django import forms
from www.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
