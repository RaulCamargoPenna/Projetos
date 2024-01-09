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
     path("Notificacoes_dos_usuarios/", Notificacoes_dos_usuarios.as_view(), name='Notificacoes_dos_usuarios'),
     path("Notificacoes_dos_usuarios/<str:task_id>/", Notificacoes_dos_usuarios.as_view(), name='status_notificacoes'),
     # path('teste', teste, name='teste'),
     # path('check_task_status/<str:task_id>/', check_task_status, name='check_task_status'),
     path('Clery_teste', Clery_teste.as_view(), name='Clery_teste'),
     path('marcar_notificacao_lida/<str:notification_id>/', marcar_notificacao_lida, name='marcar_notificacao_lida'),
]