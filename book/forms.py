from django import forms
from .models import *

class AddBookPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['authors'].label_from_instance = lambda obj : f'{obj.surname} {obj.name} {obj.patronymic}'


    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Назва книги',
            'description': 'Опис',
            'count': 'Кількість',
            'authors': 'Автор'
        }


