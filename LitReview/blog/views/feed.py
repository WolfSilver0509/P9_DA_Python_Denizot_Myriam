from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from blog.models import Ticket, Review, UserFollows
# from blog.forms import Ticket_Form, Critique_Form, Follow_Form
# from django.db import IntegrityError
from itertools import chain
# from authentification.models import User

from django.db.models import Q

# .filter = filter les éléments sur la bdd
# Valeur gauche modele valeur droite user qu'on a
# deux condiiton soit je suis l'auteur soit je suis abbonée à l'auteur du ticket
# Récupérer la liste des personnes auxquels je suis abbonnées
# django filter Q = ou
# django filter _in = dans


def get_users_viewable_reviews(user):
    userfollows = UserFollows.objects.filter(followed_user=user)
    follow = [userfollow.user.id for userfollow in userfollows]
    reviews = Review.objects.filter(Q(user=user) | Q(user__id__in=follow))
    return reviews


def get_users_viewable_tickets(user):
    # Récupération dans une liste des follower qu'on suit
    userfollows = UserFollows.objects.filter(followed_user=user)
    follow = [userfollow.user.id for userfollow in userfollows]
    tickets = Ticket.objects.filter(Q(user=user) | Q(user__id__in=follow))
    # user__id__in On utilise les deux __ pour sortie et chercher l'id ,
    # et on utilise in dans pour verifier si il est dans la liste.
    return tickets


@login_required
def feed(request):
    reviews = get_users_viewable_reviews(request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    tickets = get_users_viewable_tickets(request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    return render(
        request,
        "blog/feed/feed.html",
        context={"posts": posts, "stars": range(1, 5 + 1)},
    )


@login_required
def flux(request):
    reviews_users_followers_list = []

    reviews = Review.objects.filter(user_id=request.user.id)
    tickets = Ticket.objects.filter(user_id=request.user.id)

    list_users_followed = UserFollows.objects.filter(user=request.user)
    list_users_followers = UserFollows.objects.filter(followed_user_id=request.user)

    if list_users_followed is not None:
        for user_followed in list_users_followed:
            reviews_users_followed = Review.objects.filter(
                user_id=user_followed.followed_user.id
            )
            tickets_users_followed = Ticket.objects.filter(
                user_id=user_followed.followed_user.id
            )
            if reviews_users_followed is not None:
                reviews = reviews | reviews_users_followed
            if tickets_users_followed is not None:
                tickets = tickets | tickets_users_followed

    if list_users_followers is not None:
        for user_followers in list_users_followers:
            reviews_users_followers = Review.objects.filter(
                user_id=user_followers.user.id
            )
            if reviews_users_followers is not None:
                for review_user in reviews_users_followers:
                    reviews_users_followers_list.append(review_user.ticket.id)
                for ticket in tickets:
                    if ticket.id in reviews_users_followers_list:
                        review_user = Review.objects.filter(
                            ticket_id=ticket.id, user_id=user_followers.user.id
                        )
                        reviews = reviews | review_user
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    return render(
        request, "blog/flux.html", context={"posts": posts, "stars": range(1, 5 + 1)}
    )
