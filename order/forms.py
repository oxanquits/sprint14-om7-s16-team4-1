from django import forms
from .models import *


class AddOrderPostForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
