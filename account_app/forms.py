from django import forms
from django.contrib.auth.forms import (
                                        AuthenticationForm,
                                        PasswordResetForm,
                                        SetPasswordForm
                                        )

from account_app.models import UserAccount


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label='Enter your username', min_length=5, max_length=20,
        help_text='Required')
    email = forms.EmailField(max_length=50, help_text='Requires', 
        error_messages={'Required': 'Sorry You will need an E-mail.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Reapeat Your Password',
        widget=forms.PasswordInput)
    
    class Meta:

        model = UserAccount
        fields = ('user_name', 'email')

    def clean_username(self):

        user_name = self.cleaned_data['username'].lower()

        r = UserAccount.objects.filter(user_name=user_name)
        if r.exists():
            raise forms.ValidationError("Username already exists")

        return user_name

    def clean_password(self):

        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password do not match.')

        return cd['password2']

    def clean_email(self):

        email = self.clean_email['email']

        if UserAccount.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please user another Email, that is already taken!'
            )

        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))