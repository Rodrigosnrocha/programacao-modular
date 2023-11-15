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
#lista_inicio é uma lista onde cada elemento é uma string contendo a data de inicio no formato dd/mm

def set_dates(lista_tarefas, data_inicio, ano):    
    data_inicio = formatar_data(data_inicio)    
                               
    for tarefa in lista_tarefas:
        duracao = tarefa[1]  
        pre_requisito = tarefa[2]
        
        if pre_requisito == '':              #Verifica se a tarefa nao tem pre-requisito
            dia_inicio = data_inicio
            dia_termino = duracao + int(data_inicio[:2])
            mes_termino = int(data_inicio[3:])
            dia_max = dias_no_mes(ano, mes_termino)
     
        else:                                 
            if type(pre_requisito) == list:     #Verifica se o pre-requisito e uma lista
                datas_preReq = []
                for el in lista_tarefas:
                    for predecessora in pre_requisito:
                        if el[0] == predecessora:
                           dia_inicio = formatar_data(el[1][1])
                           datas_preReq.append(dia_inicio)
                maior_mes = int(datas_preReq[0][3:])
                maior_dia = int(datas_preReq[0][:2])
                
                for datas in datas_preReq:
                    mes = int(datas[3:])
                    dia = int(datas[:2])
                    if mes > maior_mes:
                        maior_mes = mes
                        maior_dia = dia
                    elif mes == maior_mes:
                        if dia > maior_dia:
                            maior_dia = dia                          
                dia_inicio = formatar_data(f'{maior_dia}/{maior_mes}')
                dia_termino = duracao + maior_dia
                mes_termino = maior_mes
                dia_max = dias_no_mes(ano, mes_termino)
                            
            else:
                for el in lista_tarefas:
                    if el[0] == pre_requisito:
                       dia_inicio = formatar_data(el[1][1])
                       dia_termino = duracao + int(dia_inicio[:2])
                       mes_termino = int(dia_inicio[3:])
                       dia_max = dias_no_mes(ano, mes_termino)
                      
        
        
        if dia_termino > dia_max:                   #Verifica se o dia de termino execedeu o numero maximo de dias naquele mes
           dia_termino = dia_termino % dia_max
           mes_termino += 1   
        
        tarefa[1] = (dia_inicio, formatar_data(f'{dia_termino}/{mes_termino}'))  #Substitui a duracao por uma tupla contendo a data de inicio e termino
    return lista_tarefas

def critical_path(lista_tarefas):
    return 0
