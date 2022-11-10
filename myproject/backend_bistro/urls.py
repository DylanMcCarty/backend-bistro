from django.urls import path, include 
from django.contrib import admin
from .models import MenuItems
from . import views

urlpatterns = [
    path('menu/', views.getMenu),
]