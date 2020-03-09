from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    """
    Form to authenticate users
    """
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput


class UserRegistrationForm(forms.ModelForm):
    """
    Form to register new users
    """
    # We use widgets to make the fields appear on the form
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat', widget=forms.PasswordInput)

    class Meta:
        model = User
        # Using the user model we inherit validation, for example enforcing usernames are unique
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        """
        Test if both password fields match
        """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('These passwords don\'t match!')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """
    Allow users to edit their basic details
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """
    Allow users to edit their profile information, saved in our custom Profile model
    """
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
