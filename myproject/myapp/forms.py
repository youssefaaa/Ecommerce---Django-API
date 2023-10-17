# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    # auto_validate = False
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalpha():
            raise forms.ValidationError('Username should only contain letters.')
        return username



    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        # Do not validate the password
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        # Do not validate the password
        return password2
    

    # def clean_password(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match. Please try again.")
    #     if not password1.isdigit():
    #         raise forms.ValidationError('Password should only contain numbers.')
    #     if len(password1) <= 4 or len(password1) >= 8:
    #         raise forms.ValidationError('Password should be between 4 and 8 characters long.')
    #     return password1

    # def clean_password1(self):
    #     password1 = self.cleaned_data.get('password1')
    #     if len(password1) < 4 and len(password1) > 8:
    #         raise forms.ValidationError('Password should be between 4 and 8 characters long.')
    #     return password1

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password1')
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match. Please try again.")
    #     return password2