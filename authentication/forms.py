from django import forms
from .models import *


class AddUserPostForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 'is_active']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'first_name': 'Ім\'я',
            'middle_name': 'По-батьковы',
            'last_name': 'Прізвище',
            'email': '',
            'password': 'пароль',
            'role': 'Тик користувача',
            'is_active': 'Активний користувач'
        }