from django.contrib import admin
from django.urls import path, include
from .views import login, logout
urlpatterns = [
    path('',login,name='login'),
    # path('register',views.register,name='register'),
    path('logout',logout,name='logout'),
]