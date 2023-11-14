import calendar

#acha o sucessor de uma tarefa especifica passada como parâmetro
def find_successor(lista_tarefas, tarefa):
    list_sucessores = []
    for el in lista_tarefas:
        if type(el[2])==str:
            if el[2]==tarefa:
                list_sucessores.append(el[0])
        elif type(el[2])==list:
            for pred in el[2]:
                if pred == tarefa:
                    list_sucessores.append(el[0])
    if len(list_sucessores)==0:   # se a tarefa nao tiver nenhum sucessor, retorna -1
        return -1
    elif len(list_sucessores)==1:  # se a tarefa tiver apenas um sucessor, retorna o proprio elemento, e não uma lista
        for elem in list_sucessores:
            return elem
    else:
        return list_sucessores


def dias_no_mes(ano, mes):
    _, num_dias = calendar.monthrange(ano, mes)
    return num_dias

#lista_inicio é uma lista onde cada elemento é uma string contendo a data de inicio no formato dd/mm
def set_dates(lista_tarefas, lista_inicio, ano):
    i = 0                                          #Contador da lista_inicio
    for tarefa in lista_tarefas:
        duracao = tarefa[1]                         #Duracao da tarefa
        dia_max = dias_no_mes(ano, int(lista_inicio[i][3:]))

        dia_termino = duracao + int(lista_inicio[i][:2])
        mes_termino = int(lista_inicio[i][3:])
        if dia_termino > dia_max:                   #Verifica se o dia de termino execedeu o numero maximo de dias naquele mes
            dia_termino = dia_termino % dia_max
            mes_termino += 1   
        tarefa[1] = (lista_inicio[i], f'{dia_termino}/{mes_termino}') #Substitui a duracao por uma tupla contendo a data de inicio e termino
        i += 1
    return lista_tarefas

def critical_path(lista_tarefas):
    return 0
