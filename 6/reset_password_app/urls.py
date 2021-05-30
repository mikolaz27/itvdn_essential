from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]