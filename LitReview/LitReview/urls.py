"""LitReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentification.views
#import review.views
import blog.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.login_page, name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('creatreview/<int:pk>', blog.views.creatreview, name='creatreview'),
    path('post/', blog.views.post, name='post'),
    path('supp_post/<str:pk>', blog.views.supp_post, name='supp_post'),
    path('edit_post/<int:pk>/post/<int:id_post>', blog.views.edit_post, name='edit_post'),
    path('supp_ticket/<str:pk>', blog.views.supp_ticket, name='supp_ticket'),
    path('edit_ticket/<str:pk>', blog.views.edit_ticket, name='edit_ticket'),
    path('abonnements/', blog.views.abonnements, name='abonnements'),
    path('desabonnement/<str:pk>', blog.views.desabonnement, name='desabonnement'),
    path('ajout_tickets/', blog.views.ajout_tickets, name='ajout_tickets'),
    path('ajout_critique/', blog.views.ajout_critique, name='ajout_critique'),
    path('feed/', blog.views.feed, name='feed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
