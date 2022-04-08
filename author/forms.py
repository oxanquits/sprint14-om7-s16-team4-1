from django import forms
from .models import *


class AddAuthorPostForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'name': 'Прізвище',
            'surname': 'Ім\'я',
            'patronymic': 'По-батькові',

        }
