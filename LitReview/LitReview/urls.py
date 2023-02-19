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
import review.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.login_page, name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('flux/', review.views.flux, name='flux'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('follow/', review.views.follow, name='follow'),
    path('create_critique/', review.views.critique_and_photo_upload, name='create_critique'),
    path('critique/<int:crit_id>', review.views.view_crit, name='view_crit'),
]
