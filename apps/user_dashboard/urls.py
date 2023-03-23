from django.contrib import admin
from django.urls import path, include
from .views import user_dashboard, gallery, contact, properties_details, properties, blog_archive, blog_single

urlpatterns = [
    path('', user_dashboard, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('properties_details/', properties_details, name='properties_details'),
    path('properties/', properties, name='properties'),
    path('blog_archive/', blog_archive, name='blog_archive'),
    path('blog_single/', blog_single, name='blog_single'),
]