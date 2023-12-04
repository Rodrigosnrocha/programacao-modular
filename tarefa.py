import Modulo_reutilizavel_lista as lista

def create_task(tarefa, lista_tarefas):
    elemento = []
    lista.adicionar_elemento(elemento, tarefa)
    lista.adicionar_elemento(elemento, 0)
    lista.adicionar_elemento(elemento, '')
    lista.adicionar_elemento(elemento, ())
    lista.adicionar_elemento(lista_tarefas, elemento)
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

def set_duration(tarefa, tempo, lista_tarefas):
    #adiciona, para cada tarefa, seu tempo de duração
    i = 0
    for t in lista_tarefas:
        if t[0] == tarefa:
            t[1] = tempo
        i += 1
    return lista_tarefas #retorna lista atualizada com o tempo de duração de cada tarefa


def update_prereqs(tarefa, prereq, lista_tarefas):
    #adiciona, para cada tarefa, seus pré-requisitos
    i = 0
    for t in lista_tarefas:
        if t[0] == tarefa:
            if (type(t[2])==list):
                lista.adicionar_elemento(t[2],prereq)
            else:
                t[2] = []
                lista.adicionar_elemento(t[2], prereq)
        i += 1
    return lista_tarefas #retorna lista atualizada com os pré-requisitos de cada tarefa


#listaTarefas = []
#create_task('dormir', listaTarefas)
#print(listaTarefas)
#listaTarefas = set_duration('dormir',2,listaTarefas)
#print(listaTarefas)
#listaTarefas = update_prereqs('dormir','comer',listaTarefas)
#print(listaTarefas)
#listaTarefas = update_prereqs('dormir', 'estudar', listaTarefas)
#print(listaTarefas)
