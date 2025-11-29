'''
Exercício 1 – Filtrar Números Pares
📋 Contexto
Você está desenvolvendo um sistema de análise de dados e precisa filtrar apenas os valores pares de uma lista de números para processamento posterior.
🎯 Objetivo
Crie uma função filtrar_pares(numeros) que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números pares.
📥 Entrada Esperada
pythonnumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 23, 28]
📤 Saída Esperada
python[2, 4, 6, 8, 10, 20, 28]
'''

def filter_pairs(numbers):
    return [value for value in numbers if value%2 == 0] #list comprehension deve ter os []

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 23, 28]
    results = filter_pairs(numbers)
    print(results)