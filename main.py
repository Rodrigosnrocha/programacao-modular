import tarefa, path
import Modulo_reutilizavel_lista as lista

listaTarefas = lista.criar_lista()

tarefa.create_task("Criar esqueleto", listaTarefas)
tarefa.set_duration("Criar esqueleto", 2, listaTarefas)

tarefa.create_task("Criar testes de API", listaTarefas)
tarefa.set_duration("Criar testes de API", 1, listaTarefas)

tarefa.create_task("Implementar func 1", listaTarefas)
tarefa.set_duration("Implementar func 1", 3, listaTarefas)
tarefa.update_prereqs("Implementar func 1", "Criar esqueleto", listaTarefas)
tarefa.update_prereqs("Implementar func 1", "Criar testes de API", listaTarefas)

tarefa.create_task("Implementar func 2", listaTarefas)
tarefa.set_duration("Implementar func 2", 5, listaTarefas)

tarefa.create_task("Implementar func 3", listaTarefas)
tarefa.set_duration("Implementar func 3", 7, listaTarefas)
tarefa.update_prereqs("Implementar func 3", "Implementar func 1", listaTarefas)

path.set_dates(listaTarefas, "01/12", 2023)

caminhoCritico = path.critical_path(listaTarefas)

print(f"Data início {caminhoCritico[0][3][0]} - Data fim {caminhoCritico[-1][3][1]}")
print(f"Caminho crítico: ")
texto = ""
for i in caminhoCritico:
    texto +=f"|{i[0]} - Início {i[3][0]} - Fim {i[3][1]}| "

print(texto)