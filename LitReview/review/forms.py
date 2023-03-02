from django import forms

from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class CritForm(forms.ModelForm):
    edit_crit = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Critique
        fields = ['title', 'content']


class DeleteCritForm(forms.ModelForm):
    delete_crit = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Critique
        fields = []

