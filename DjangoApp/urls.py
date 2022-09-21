from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import app

urlpatterns = [
    path('',app,name='app'),
    #path('upload/',upload,name='upload'),
]
