from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=_("Имя пользователя"),
        max_length=150,
        help_text=_("Обязательно. До 150 символов. Только буквы, цифры и @/./+/-/_."),
    )
    password1 = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput,
        help_text=_(
            "<ul>"
            "<li>Ваш пароль не должен быть слишком похож на другую вашу личную информацию.</li>"
            "<li>Ваш пароль должен содержать как минимум 8 символов.</li>"
            "<li>Ваш пароль не должен быть слишком простым.</li>"
            "<li>Ваш пароль не может состоять только из цифр.</li>"
            "</ul>"
        ),
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput,
        help_text=_("Введите тот же пароль ещё раз для подтверждения."),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         print("опасука")
    #         raise forms.ValidationError('Такой логин уже существует!')
    #     return username

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="Логин",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш логин'
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'Введите ваш пароль'
        })
    )