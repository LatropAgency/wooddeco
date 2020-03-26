from django import forms
from django.core.exceptions import ValidationError


class AuthForm(forms.Form):
    login = forms.CharField(max_length=64, label="Email/username")
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, label='Пароль')


class RegForm(forms.Form):
    email = forms.CharField(max_length=64, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, label='Пароль')


class EditForm(forms.Form):
    first_name = forms.CharField(max_length=64, label = "Имя")
    last_name = forms.CharField(max_length=64, label = "Фамилия")
    username = forms.CharField(max_length=64, label='username')
    email = forms.CharField(max_length=64, label = "Email")
    old_password = forms.CharField(widget=forms.PasswordInput, min_length=6, label='Текущий пароль')
    new_password = forms.CharField(widget=forms.PasswordInput, min_length=6, label='Новый пароль')
    rep_new_password = forms.CharField(widget=forms.PasswordInput, min_length=6, label='Повторите пароль')

    def clean_rep_new_password(self):
        data = self.cleaned_data
        if data['rep_new_password'] == data['new_password']:
            if data['old_password'] != data['new_password']:
                return data['new_password']
            else:
                raise ValidationError("Нельзя изменить пароль на текущий")
        else:
            raise ValidationError("Пароли не совпадают")