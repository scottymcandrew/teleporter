from django import forms


class LoginForm(forms.Form):
    """
    Form to authenticate users
    """
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput
