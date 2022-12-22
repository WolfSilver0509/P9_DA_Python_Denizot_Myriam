from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def flux(request):
    return render(request, 'review/flux.html')

@login_required
def follow(request):
    return render(request, 'review/Follow_page.html')
