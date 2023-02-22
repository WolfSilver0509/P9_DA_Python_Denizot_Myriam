from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from . import forms
from .import models


@login_required
def flux(request):
    photos = models.Photo.objects.all()
    crits = models.Critique.objects.all()
    context = {
        'photos': photos,
        'crits': crits,
    }
    return render(request, 'review/flux.html', context)

@login_required
def follow(request):
    return render(request, 'review/Follow_page.html')

@login_required
def critique_and_photo_upload(request):
    crit_Form = forms.CritForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        crit_Form = forms.CritForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([crit_Form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            crit = crit_Form.save(commit=False)
            crit.author = request.user
            crit.photo = photo
            crit.save()
            return redirect('flux')
        else:
            print(crit_Form.errors)
            print(photo_form.errors)
    context = {
        'crit_Form': crit_Form,
        'photo_form': photo_form,
    }
    return render(request, 'review/create_critique_post.html', context=context)


@login_required
def view_crit(request, crit_id):
    crit = get_object_or_404(models.Critique, id=crit_id)
    return render(request, 'review/view_crit.html', {'crit': crit})

@login_required
def edit_crit(request, crit_id):
    crit = get_object_or_404(models.Critique, id=crit_id)
    edit_crit_form = forms.CritForm(instance=crit)
    delete_crit_form = forms.DeleteCritForm(instance=crit)
    if request.method == 'POST':
        edit_form = forms.CritForm(request.POST, instance=crit)
        delete_form = forms.DeleteCritForm(request.POST, instance=crit)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('flux')
        if delete_form.is_valid():
            crit.delete()
            return redirect('flux')
    else:
        edit_form = forms.CritForm(instance=crit)
        delete_form = forms.DeleteCritForm(instance=crit)
    context = {
            'edit_form': edit_form,
            'delete_form': delete_form,
        }
    return render(request, 'review/edit_crit.html', context)