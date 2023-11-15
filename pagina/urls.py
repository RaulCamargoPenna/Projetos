#começando as páginas - url - view - template

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from .views import *
from django.contrib.auth import views
from django.contrib.auth.views import PasswordResetConfirmView
from .tasks import *



app_name = 'pagina'

urlpatterns = [
     path('', Homepage.as_view(), name='homepage'),
     path('navbar', navbar.as_view(), name='navbar'),
     path('teste', teste, name='teste'),
     path('Clery_teste', Clery_teste.as_view(), name='Clery_teste'),
     path('check_task_status/<str:task_id>/', check_task_status, name='check_task_status'),
     
]