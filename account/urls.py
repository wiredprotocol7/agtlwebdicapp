from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('search', views.search, name='search'),
]
