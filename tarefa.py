#Lista de tarefas 
#Importar módulo reutilizável de listas
#Cada elemento da lista é uma lista que contém a tarefa, seu tempo de duração e seus
#pré-requisitos, respectivamente

# Tarefa: Nome | Duracao | Requisitos | Start Date | End Date
import Modulo_reutilizavel_lista as lista

#Criar list_tarefas no programa principal com a função criar_lista do módulo reutilizavel

def create_task(tarefa, list_tarefas):
    lista.adicionar_elemento(list_tarefas, tarefa)
    return 

def remove_task(tarefa, list_tarefas):
    lista.remover_elemento(list_tarefas, tarefa)
    return 

def set_duration(tarefa, tempo, list_tarefas):
    #adiciona, para cada tarefa, seu tempo de duração
    i = 0
    for t in list_tarefas:
        if t[0] == tarefa:
            t[1] = tempo
        i += 1
    return list_tarefas #retorna lista atualizada com o tempo de duração de cada tarefa


def update_prereqs(tarefa, prereq, list_tarefas):
    #adiciona, para cada tarefa, seus pré-requisitos
    i = 0
    for t in list_tarefas:
        if t[0] == tarefa:
            t[2] = prereq
        i += 1
    return list_tarefas #retorna lista atualizada com os pré-requisitos de cada tarefa

