from celery import shared_task
from django_celery_results.models import TaskResult
from time import sleep
from notifications.signals import notify
from django.contrib.auth.models import User


def notificar(user, verb):
    result = notify.send(user, recipient=user, verb=verb)
    

@shared_task(bind=True)
def teste_func(self):
    task_result = TaskResult(task_id=self.request.id, task_name="atualizacao_estoque_fulfillment")
    task_result.save()

    ## Lógica de processamento da função!

    for i in range(5):
        sleep(1)
        print(i)

    # Atualiza o status da tarefa:
    result = {'itens_atualizados' : 233} 

    task_result = TaskResult.objects.get(task_id=self.request.id)
    task_result.status = 'SUCCESS'
    task_result.result = result
    task_result.save()
    return result
    