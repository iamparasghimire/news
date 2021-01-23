from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<str:sno>', views.blogpost, name='blogpost'), 
]