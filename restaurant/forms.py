from django import forms
from django.db import models
from .models import Menu 

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu 
        fields = ['restaurant','date', 'menu_name']