from django.core import validators
from django import forms
from .models import Card


class CardRegistration(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['image', 'title', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
