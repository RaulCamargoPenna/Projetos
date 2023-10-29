#começando as páginas - url - view - template

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from .views import *
from django.contrib.auth import views
from django.contrib.auth.views import PasswordResetConfirmView



app_name = 'pagina'

urlpatterns = [
     path('', Homepage.as_view(), name='homepage'),
     path('navbar', navbar.as_view(), name='navbar')
]