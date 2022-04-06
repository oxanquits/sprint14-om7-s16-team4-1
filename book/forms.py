from django import forms
from .models import *

class AddBookPostForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'