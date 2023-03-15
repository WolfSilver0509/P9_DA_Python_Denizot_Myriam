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


class ReviewForm(ModelForm):
    # la notation par étoiles
    RATINGS = [("1", "*"), ("2", "**"), ("3", "***"), ("4", "****"), ("5", "*****")]

    class Meta:
        model = models.Review
        fields = ["ticket", "rating", "user", "headline", "body"]

    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=RATINGS)

class ReviewCreateForm(ModelForm):
    """ """

    RATINGS = [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]

    class Meta:
        model = models.Review
        fields = ["rating", "headline", "body"]

    rating = forms.ChoiceField(label="Note", widget=forms.RadioSelect, choices=RATINGS)
    headline = forms.CharField(max_length=128, label="Titre")
    body = forms.CharField(max_length=8192, label="Commentaire")