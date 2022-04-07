from django import forms
from .models import *


class AddUserPostForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
