from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'),
    path('view_customer/', views.view_customer, name='view_customer'),
    path('view_scheme/', views.view_scheme, name='view_scheme'),
    path('add_location/', views.add_location, name='add_location'),
    path('view_file/', views.view_file, name='view_file'),
    path('file_transfer/', views.file_transfer, name='file_transfer'),
    path('file_sale/', views.file_sale, name='file_sale'),
    path('view_property/', views.view_property, name='view_property'),
    path('property_type/', views.property_type, name='property_type'),
    path('view_user/', views.view_user, name='view_user'),
]