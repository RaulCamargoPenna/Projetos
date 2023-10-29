from django.shortcuts import render
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class Homepage(TemplateView):
    template_name = 'homegeral.html'
    
class navbar(TemplateView):
    template_name = 'navbar.html'
