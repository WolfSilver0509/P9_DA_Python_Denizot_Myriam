from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from blog.models import Ticket, Review, UserFollows
from blog.forms import Ticket_Form, Critique_Form, Follow_Form
from django.db import IntegrityError
from itertools import chain
from authentification.models import User

@login_required
def abonnements(request):
    error = ""
    form = Follow_Form()
    userfllows = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user_id=request.user)
    context = {
        'userfllows': userfllows,
        "followers": followers,
        "form": form,
        "error": error
    }
    if request.method == "POST":
        user_form = Follow_Form(request.POST)
        if user_form.is_valid():
            find_user = user_form.cleaned_data.get("username")
            if find_user == request.user.username:
                error = f"{find_user} Vous ne pouvez pas vous suivre vous-même "
                context.update({"error": error})
                return render(request, 'blog/abonnements.html', context=context)
            else:
                try:
                    found_user = User.objects.get(username=find_user)
                except User.DoesNotExist:
                    error = f"{find_user} n'existe pas ! "
                    context.update({"error": error})
                    return render(request, 'blog/abonnements.html', context=context)
                try:
                    instance = UserFollows(user=request.user, followed_user=found_user)
                    instance.save()
                    followers = UserFollows.objects.filter(followed_user_id=request.user)
                    context.update({"followers": followers})
                    return redirect("abonnements")

                except IntegrityError:
                    error = f"Vous avez déjà suivi {find_user}"
                    context.update({"error": error})
                    return render(request, 'blog/abonnements.html', context=context)
    return render(request, 'blog/abonnements.html', context=context)


@login_required
def desabonnement(request, pk):
    userTodel = User.objects.get(username=pk)
    userFollowstoDel = UserFollows.objects.get(followed_user_id=userTodel.id, user_id=request.user.id)
    userFollowstoDel.delete()
    return redirect("abonnements")