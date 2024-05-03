from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from user.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '"Enter Password'}))


class CustomRegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    first_name = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    age = forms.IntegerField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Возраст'}))
    gender = forms.ChoiceField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Пол'}), choices=User.type_gender)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '"Введите пароль'}))

