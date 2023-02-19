from django import forms

from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class CritForm(forms.ModelForm):
    class Meta:
        model = models.Critique
        fields = ['title', 'content']