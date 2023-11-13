import tarefa

tasklist = tarefa.criar_lista()
try:
    print(len(tasklist) == 0)
except:
    print("Lista nao foi criada corretamente")

tarefa.create_task("Testar API",tasklist)
tarefa.set_duration("Testar API",5,tasklist)
print(tasklist)

tarefa.create_task("Testar Delete",tasklist)
tarefa.update_prereqs("Testar Delete",["Testar API"],tasklist)
print(tasklist)

tarefa.remove_task("Testar Delete",tasklist)
print(tasklist)



