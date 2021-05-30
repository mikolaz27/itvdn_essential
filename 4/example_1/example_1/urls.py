"""example_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from itvdn_shop.views import Index, Report, LoginExample, \
    ListExample, DetailViewExample, DateDetailViewExample, \
    WeekArchiveViewExample, DeleteExample, CreateViewExample, UpdateExample

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('report/', Report.as_view(), name='report'),
    path('login/', LoginExample.as_view(), name='login'),
    path('accounts/profile/', ListExample.as_view(), name='all_user'),
    path('detail/<pk>/', DetailViewExample.as_view(), name='detail'),
    path('detail-date/<year>/<month>/<day>/<pk>',
         DateDetailViewExample.as_view(), name='detail_date'),
    path('week-archive/<week>/', WeekArchiveViewExample.as_view(), name='week_archive'),
    path('create/', CreateViewExample.as_view(), name='create'),
    path('delete/<pk>/', DeleteExample.as_view(), name='delete'),
    path('update/<pk>/', UpdateExample.as_view(), name='update')
]
