from django.shortcuts import render, redirect, get_object_or_404

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
    return render(
        request, "blog/ajout_tickets.html", context={"ticket_form": ticket_form}
    )


@login_required
def supp_ticket(request, pk):
    # ticket_to_supp = Ticket.objects.get(id=pk)
    ticket_to_supp = get_object_or_404(Ticket, pk=pk)
    if ticket_to_supp.user != request.user:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à supprimer ce Ticket.")
    userpostTodel = Ticket.objects.get(id=pk, user_id=request.user.id)
    userpostTodel.delete()
    return redirect("post")


@login_required
def edit_ticket(request, pk):
    # ticket_to_modify = Ticket.objects.get(id=pk)
    ticket_to_modify = get_object_or_404(Ticket, pk=pk)
    if ticket_to_modify.user != request.user:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à modifier ce ticket.")
    if request.method == "GET":
        ticket_form = Ticket_Form(instance=ticket_to_modify)
        return render(
            request=request,
            template_name="blog/edit_ticket.html",
            context={"ticket_form": ticket_form, "ticket": ticket_to_modify},
        )
    elif request.method == "POST":
        ticket_form = Ticket_Form(
            request.POST, request.FILES, instance=ticket_to_modify
        )
        if ticket_form.is_valid():
            ticket_form.save()
        return redirect("post")
