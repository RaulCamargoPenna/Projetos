from .notifications import get_unread_notifications, count_unread_notifications_unser 
from django.http import HttpResponse
import ast


def listar_notificacao(request):
    unread_notifications = get_unread_notifications(user=request.user) 
    notificacoes = list(unread_notifications)

    lista_de_noticicacoes = []
    for notificacao in notificacoes:
        id_notificacao = notificacao.id
        recipient = notificacao.recipient
        mensagem = notificacao.verb
        mensagem_dicionario = ast.literal_eval(mensagem)
        if mensagem_dicionario != None:
            status = ''
            if 'status' in mensagem_dicionario:
                status = mensagem_dicionario['status']
            
            resultado = ''
            if 'resultado' in mensagem_dicionario:
                resultado = mensagem_dicionario['result']

            tarefa = ''
            if 'tarefa' in mensagem_dicionario:
                tarefa = mensagem_dicionario['tarefa']
        else: 
            status = ''
            resultado = ''
            tarefa = ''
        
        info_notificacao = {
            'id_notificacao': id_notificacao,
            'tarefa': tarefa,
            'resultado': resultado,
            'status': status
            }
        lista_de_noticicacoes.append(info_notificacao)
    
    qnt_notificacoes = count_unread_notifications_unser(user=request.user)
    context =  {
        'unread_notifications': lista_de_noticicacoes,
        'qnt_notificacoes': qnt_notificacoes
        }
    
    return context



