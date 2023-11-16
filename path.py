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
    
def formatar_data(data):
    # Divide a string em dia, mês
    dia, mes = map(int, data.split('/'))
    dia_formatado = f'0{dia}' if dia < 10 else str(dia)
    mes_formatado = f'0{mes}' if mes < 10 else str(mes)
    
    # Retorne a data formatada no formato dd/mm
    return f'{dia_formatado}/{mes_formatado}'
    
#data_incio é um dia no formato dd//mm que representa o inicio do projeto
def set_dates(lista_tarefas, inicio, ano):
    def calcula_data_termino(dia_inicio, duracao):
        dia_inicio = formatar_data(dia_inicio)
        dia_termino = int(dia_inicio[:2]) + duracao
        mes_termino = int(dia_inicio[3:])
        dia_max = dias_no_mes(ano, mes_termino)
        if dia_termino > dia_max:
            dia_termino = dia_termino % dia_max
            mes_termino += 1
        return f'{dia_termino}/{mes_termino}'

    for tarefa in lista_tarefas:
        duracao = tarefa[1]
        pre_requisito = tarefa[2]

        if pre_requisito == '':
            data_termino = calcula_data_termino(inicio, duracao)
        else:
            if type(pre_requisito) == list:
                datas_pre_req = []
                for el in lista_tarefas:
                    for predecessora in pre_requisito:
                        if el[0] == predecessora:
                            inicio = formatar_data(el[1][1])
                            datas_pre_req.append(inicio)
                maior_mes = int(datas_pre_req[0][3:])
                maior_dia = int(datas_pre_req[0][:2])

                for datas in datas_pre_req:
                    mes = int(datas[3:])
                    dia = int(datas[:2])
                    if mes > maior_mes or (mes == maior_mes and dia > maior_dia):
                        maior_mes = mes
                        maior_dia = dia

                inicio = formatar_data(f'{maior_dia}/{maior_mes}')
                data_termino = calcula_data_termino(inicio, duracao)
            else:
                for el in lista_tarefas:
                    if el[0] == pre_requisito:
                        inicio = el[1][1]
                        data_termino = calcula_data_termino(inicio, duracao)

        tarefa[1] = (inicio, formatar_data(data_termino))

    return lista_tarefas

def critical_path(lista_tarefas):
    return 0
