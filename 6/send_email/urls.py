from django.contrib import admin
from django.urls import path, include

from .views import usersignup, activate_account, subscription
from django.contrib.auth import views as auth

urlpatterns = [
    path('logout/', auth.LogoutView.as_view(template_name='index.html'),
         name='logout'),
    path(r'signup/', usersignup, name='register_user'),
    path(
        r'activate/<uidb64>/<token>/',
        activate_account, name='activate'),
    path("subscription/", subscription, name="subscription"),
]
