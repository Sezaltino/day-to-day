''''
📋 Contexto
Você tem uma lista de clientes e precisa ordená-los por idade (do mais jovem ao mais velho). Se houver empate na idade, ordene alfabeticamente pelo nome.
🎯 Objetivo
Crie uma função ordenar_clientes(clientes) que ordene usando múltiplos critérios.
📥 Entrada Esperada
pythonclientes = [
    {"nome": "Carlos", "idade": 30},
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Diana", "idade": 30},
    {"nome": "Eduardo", "idade": 22}
]
📤 Saída Esperada
python[
    {"nome": "Eduardo", "idade": 22},
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Diana", "idade": 30}
]
'''
def order_clients(clients):

    return sorted(clients, key = lambda x: (x["idade"],  x["nome"]))

if __name__ == "__main__":
    pythonclients = [
    {"nome": "Carlos", "idade": 30},
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Diana", "idade": 30},
    {"nome": "Eduardo", "idade": 22}
    ]
    
    print(order_clients(pythonclients))