from django.contrib import admin
from django.urls import path

from jinja_app import views

urlpatterns = [
    path('jinja2/', views.jinja_test),
    path('django/', views.django_test),
]






