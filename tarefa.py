#Lista de tarefas 
#Importar módulo reutilizável de listas
#Cada elemento da lista é uma lista que contém a tarefa, seu tempo de duração e seus
#pré-requisitos, respectivamente

# Tarefa: Nome | Duracao | Requisitos | Start Date | End Date
import Modulo_reutilizavel_lista as lista


def criar_lista():
    lista = []
    return lista

def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return

def remove_task(tarefa, lista_tarefas):
    lista_copia = lista_tarefas.copy()  # Crie uma cópia da lista
    
    for el in lista_copia:
        if type(el[2]) == list and tarefa[0] in el[2]:
             lista.remover_elemento(el[2], tarefa[0])
        elif el[2] == tarefa[0]:
            el[2] = ''
    
    lista.remover_elemento(lista_copia, tarefa)
     # Remova a tarefa da cópia
    return lista_copia

#Funções criar_lista, adicionar_elemento e remover_elemento fazem parte do módulo que será importado
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

