from django import forms
from .models import *


class AddAuthorPostForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
