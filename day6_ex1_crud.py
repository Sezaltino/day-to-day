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
def add_tasks():
    pass

def update_taks():
    pass

def get_tasks():
    pass

def delete_tasks():
    pass

if __name__ == "__main__":
    pythontarefas = [
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
            if option == "1": pass
            elif option == "2": pass 
            elif option == "3": pass
            elif option == "4": pass
            else: print("\nOption inválida, escolhe entre 1 e 5!\n")
        else:
            print("\nCaracteres não são permitidos, insira um número de 1 a 5!\n")