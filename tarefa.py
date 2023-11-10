#Lista de tarefas 
#Importar módulo reutilizável de listas
#Cada elemento da lista é uma lista que contém a tarefa, seu tempo de duração e seus
#pré-requisitos, respectivamente

def criar_lista():
    lista = []
    return lista

def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return

def remover_elemento(lista, elemento):
    lista.remove(elemento)
    return

#Funções criar_lista, adicionar_elemento e remover_elemento fazem parte do módulo que será importado
#Criar list_tarefas no programa principal com a função criar_lista do módulo reutilizavel

def create_task(tarefa, list_tarefas):
    adicionar_elemento(list_tarefas, tarefa)
    return 

def remove_task(tarefa, list_tarefas):
    remover_elemento(list_tarefas, tarefa)
    return 

def set_duration(tarefa, tempo, list_tarefas):
    #adiciona, para cada tarefa, seu tempo de duração
    
    return list_tarefas #retorna lista atualizada com o tempo de duração de cada tarefa


def update_prereqs(tarefa, prereq, list_tarefas):
    #adiciona, para cada tarefa, seus pré-requisitos
    
    return list_tarefas #retorna lista atualizada com os pré-requisitos de cada tarefa

