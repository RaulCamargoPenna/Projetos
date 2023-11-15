from django.shortcuts import render
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from .tasks import teste_func
from django.http import JsonResponse
from celery.result import AsyncResult
from django.views.decorators.csrf import csrf_exempt
from django_celery_results.models import TaskResult
from django.db.models import Sum, Value, F
import json


class Homepage(TemplateView):
    template_name = 'homegeral.html'
    
class navbar(TemplateView):
    template_name = 'navbar.html'


class Clery_teste(TemplateView):
    template_name = 'celery_teste.html'

@csrf_exempt
def teste(request):
    task_result = teste_func.delay()
    return JsonResponse({'task_id': task_result.id})


def check_task_status(request, task_id):
   
    task_result = TaskResult.objects.filter(task_id=task_id).values('task_id').annotate(status = F('status'))
    task_result = {item['task_id']: item['status'] for item in task_result}
    response_data = {'status': task_result[task_id]}
    task = TaskResult.objects.get(task_id = task_id)
    if response_data['status'] == "SUCCESS":
        result = task.result
        result = eval(result.replace("'",'"'))
        print(result)
        response_data['result'] = result['itens_atualizados']
    
    return JsonResponse(response_data)