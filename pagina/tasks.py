from celery import shared_task
from django_celery_results.models import TaskResult
from time import sleep


@shared_task(bind=True)
def teste_func(self):
    
    task_result = TaskResult(task_id=self.request.id, task_name="atualizacao_estoque_fulfillment")
    task_result.save()

    ## Lógica de processamento da função!

    for i in range(5):
        sleep(2)
        print(i)

    # Atualiza o status da tarefa:
    result = { 'itens_atualizados' : 233} 

    task_result = TaskResult.objects.get(task_id=self.request.id)
    task_result.status = 'SUCCESS'
    task_result.result = result
    task_result.save()
    return result
    