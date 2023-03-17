from django.contrib import admin
from django.urls import path, include
from .views import user_dashboard

urlpatterns = [
    path('', user_dashboard, name='index'),
]