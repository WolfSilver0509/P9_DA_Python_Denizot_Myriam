from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from blog.models import Ticket, Review, UserFollows
from blog.forms import Ticket_Form, Critique_Form, Follow_Form
from django.db import IntegrityError
from itertools import chain
from authentification.models import User


@login_required
def ajout_critique(request):
    ticket_form = Ticket_Form()
    review_form = Critique_Form()
    if request.method == "POST":
        review_form = Critique_Form(request.POST)
        ticket_form = Ticket_Form(request.POST, request.FILES)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(request.user.id)
            review_form.save(request.user.id, ticket=ticket)
        return redirect("feed")

    context = {'ticket_form': ticket_form, 'review_form': review_form}
    return render(request, 'blog/ajout_critique.html', context=context)


@login_required
def supp_post(request, pk):
    userpostTodel = Review.objects.get(id=pk, user_id=request.user.id)
    userpostTodel.delete()
    return redirect("post")


@login_required
def creatreview(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == "POST":
        review_form = Critique_Form(request.POST)
        if review_form.is_valid():
            review_form.save(request.user.id, ticket=ticket)
        return redirect("feed")
    else:
        review_form = Critique_Form()
    context = {'ticket': ticket, 'review_form': review_form}
    return render(request, 'blog/creatreview.html', context=context)

@login_required
def post(request):
    reviews = Review.objects.filter(user_id=request.user.id).order_by('-time_created')
    tickets = Ticket.objects.filter(user_id=request.user.id).order_by('-time_created')

    return render(request, "blog/post.html", context={'reviews': reviews, 'tickets': tickets, 'stars': range(1, 5+1)})


@login_required
def edit_post(request, pk, id_post):
    post_to_modify = Review.objects.get(id=pk, user_id=request.user.id)
    tickets = Ticket.objects.get(id=id_post)
    if request.method == "GET":
        review_form = Critique_Form(instance=post_to_modify)
        return render(
            request=request,
            template_name="blog/edit_post.html",
            context={"review_form": review_form, "tickets": tickets})
    elif request.method == "POST":
        ticket_form = Critique_Form(request.POST, request.FILES, initial={
            "id": post_to_modify.id,
            "rating": post_to_modify.rating,
            "headline": post_to_modify.headline,
            "body": post_to_modify.body})
        if ticket_form.is_valid():
            post_to_modify.rating = ticket_form.cleaned_data.get("rating")
            post_to_modify.headline = ticket_form.cleaned_data.get("headline")
            post_to_modify.body = ticket_form.cleaned_data.get("body")
            post_to_modify.ticket_id = id_post
            post_to_modify.save()
        return redirect("post")
