'''
📋 Contexto
Você está construindo um gerenciador simples de tarefas. Precisa de funções básicas para criar, ler, atualizar e deletar tarefas de uma lista.
🎯 Objetivo
Crie um mini-sistema com 4 funções:

adicionar_tarefa(tarefas, nova_tarefa): adiciona uma tarefa à lista
listar_tarefas(tarefas): exibe todas as tarefas
atualizar_tarefa(tarefas, id, novos_dados): atualiza uma tarefa específica
remover_tarefa(tarefas, id): remove uma tarefa

📥 Estrutura Esperada
pythontarefas = [
    {"id": 1, "descricao": "Estudar Python", "concluida": False},
    {"id": 2, "descricao": "Fazer compras", "concluida": True}
]
📤 Exemplos de Uso
python# Adicionar
adicionar_tarefa(tarefas, {"id": 3, "descricao": "Limpar casa", "concluida": False})

# Atualizar
atualizar_tarefa(tarefas, 1, {"concluida": True})

# Remover
remover_tarefa(tarefas, 2)

# Listar
listar_tarefas(tarefas)
'''
def add_tasks(tasks, new_task):
    pass

def update_taks(tasks, id_task, new_data):
    pass

def get_tasks(tasks, id_or_name_task = None):
    if id_or_name_task is not None:
        if id_or_name_task.isdigit():
            select_task = [task for task in tasks if task.get("id") == id_or_name_task] 
            print(select_task)
def delete_tasks(tasks, id_task):
    pass

if __name__ == "__main__":
    pythontasks = [
    {"id": 1, "descricao": "Estudar Python", "concluida": False},
    {"id": 2, "descricao": "Fazer compras", "concluida": True}
    ]

    leave = True

    while leave:
        print("""
        1 - Adicionar tarefa
        2 - Atualizar tarefa
        3 - Listar tarefas
        4 - Remover tarefa
        5 - Sair
        """)

        option = input("Selecione a option desejada: ")

        leave = False if option == "5" else True

        if option.isdigit():
            if option == "1":
                insert = input("Insira a tarefa: ")
                add_tasks(pythontasks, insert)
            elif option == "2": 
                print("\nTarefas: ")
                for tasks in pythontasks:
                    for key, value in tasks.items():
                        print(str(key) + ": " + str(value)) 
                    print("\n")
                update = input("Insira o nome ou o id da tarefa que quer alterar: ")
                
                print("Task Selecionada:\n")
                print(get_tasks(pythontasks, update))

                print(""""
                O que deseja alterar:
                1 - Nome
                2 - Status
                """)
                option = input("Selecione a option desejada: ")

                if option.isdigit():
                    if option == 1: update_data = {"descricao": input("Insira o novo nome")}
                    elif option == 2: update_data = {"concluida": True}
                    else: print("Option inválida, selecione 1 ou 2")
                else:
                    print("Caracteres não são permitidos, insira um número")

                update_taks(pythontasks, update if update.isdigit() else get_tasks(tasks, update), update_taks)

            elif option == "3": pass
            elif option == "4": pass
            else: print("\nOption inválida, escolhe entre 1 e 5!\n")
        else:
            print("\nCaracteres não são permitidos, insira um número de 1 a 5!\n")