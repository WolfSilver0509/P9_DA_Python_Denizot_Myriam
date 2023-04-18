from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from blog.models import Ticket, Review, UserFollows
from blog.forms import Ticket_Form, Critique_Form, Follow_Form
from django.db import IntegrityError
from itertools import chain
from authentification.models import User




@login_required
def ajout_tickets(request):
    if request.method == "POST":
        ticket_form = Ticket_Form(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket_form.save(request.user.id)
            return redirect("feed")
    else:
        ticket_form = Ticket_Form()
    return render(request, "blog/ajout_tickets.html", context={"ticket_form": ticket_form})

@login_required
def supp_ticket(request, pk):
    userpostTodel = Ticket.objects.get(id=pk, user_id=request.user.id)
    userpostTodel.delete()
    return redirect("post")


@login_required
def edit_ticket(request, pk):
    post_to_modify = Ticket.objects.get(id=pk)
    tickets = Ticket.objects.filter(user_id=request.user.id, id=pk)
    if request.method == "GET":

        ticket_form = Ticket_Form(instance=post_to_modify)
        return render(
            request=request,
            template_name="blog/edit_ticket.html",
            context={"ticket_form": ticket_form, "tickets": tickets})
    elif request.method == "POST":
        ticket_form = Ticket_Form(request.POST, request.FILES, initial={
            "id": post_to_modify.id,
            "title": post_to_modify.title,
            "description": post_to_modify.description,
            "image": post_to_modify.image})
        if ticket_form.is_valid():
            post_to_modify.title = ticket_form.cleaned_data.get("title")
            post_to_modify.description = ticket_form.cleaned_data.get("description")
            post_to_modify.image = ticket_form.cleaned_data.get("image")
            post_to_modify.save()
        return redirect("post")
