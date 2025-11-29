'''
📋 Contexto
Você tem duas listas separadas: uma com nomes de alunos e outra com suas respectivas notas. Precisa combiná-las em uma estrutura mais organizada.
🎯 Objetivo
Crie uma função combinar_dados(nomes, idades) que use zip() para criar uma lista de dicionários.
📥 Entrada Esperada
pythonnomes = ["Alice", "Bruno", "Carla", "Diego"]
idades = [28, 35, 22, 41]
📤 Saída Esperada
python[
    {"nome": "Alice", "idade": 28},
    {"nome": "Bruno", "idade": 35},
    {"nome": "Carla", "idade": 22},
    {"nome": "Diego", "idade": 41}
]
'''

def data_join(names, ages):

    return [
        {
        "nome": name,
        "idade": age
        } 
        for name, age in zip(names, ages)]

if __name__ == "__main__":

    python_names = [
                    "Alice",
                    "Bruno",
                    "Carla",
                    "Diego"
                    ]
    
    python_ages = [
                    28, 
                    35, 
                    22, 
                    41
                    ]

    print(data_join(python_names, python_ages))
