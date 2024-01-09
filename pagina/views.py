from django.shortcuts import render
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponse
from .tasks import teste_func, notificar
from django.http import JsonResponse
from celery.result import AsyncResult
from django.views.decorators.csrf import csrf_exempt
from django_celery_results.models import TaskResult
from django.db.models import Sum, Value, F
import json
from .notifications import get_unread_notifications
from notifications.models import Notification
from django.views.decorators.http import require_http_methods


class Homepage(TemplateView):
    template_name = 'homegeral.html'
    
class navbar(TemplateView):
    template_name = 'navbar.html'


class Clery_teste(TemplateView):
    template_name = 'celery_teste.html'


# @csrf_exempt
class Notificacoes_dos_usuarios(View):

    def post(self, request):
        
        task_result = teste_func.delay()
        return JsonResponse({'task_id': task_result.id})

    def get(self, request, task_id=None):
        task_result = TaskResult.objects.filter(task_id=task_id).values('task_id').annotate(status = F('status'))
        print(task_result)
        if task_result.exists():
            task_result = {item['task_id']: item['status'] for item in task_result}
            print(task_result)
            response_data = {'status': task_result[task_id]}
            task = TaskResult.objects.get(task_id = task_id)
            
            if response_data['status'] == "SUCCESS":
                result = task.result
                nome_tarefa = task.task_name
                result = eval(result.replace("'",'"'))
                response_data['result'] = result['itens_atualizados']
                response_data['tarefa'] = nome_tarefa
                notificar(request.user, response_data)
            
            return JsonResponse(response_data)
        
        return JsonResponse({'error': 'Task ID não fornecido'})


def marcar_notificacao_lida(request, notification_id):
    notificacao = Notification.objects.get(id=notification_id)

    if notificacao.recipient == request.user:
        notificacao.mark_as_read()

        return JsonResponse({'message': 'Notificação marcada como lida com sucesso.'})
    else:

        return JsonResponse({'error': 'Você não tem permissão para marcar esta notificação como lida.'}, status=403)
