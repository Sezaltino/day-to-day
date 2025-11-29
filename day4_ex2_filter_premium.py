'''
Dia 5 – Filtrar com filter + Lambda
📋 Contexto
O departamento de vendas precisa de uma lista rápida de produtos premium (acima de R$ 100) para uma campanha especial.
🎯 Objetivo
Crie uma função filtrar_premium(produtos) que use filter() e lambda para retornar apenas produtos com preço acima de 100.
📥 Entrada Esperada
pythonprodutos = [
    {"nome": "Caneta", "preco": 5.00},
    {"nome": "Caderno", "preco": 25.00},
    {"nome": "Mochila", "preco": 150.00},
    {"nome": "Estojo", "preco": 15.00},
    {"nome": "Tablet", "preco": 800.00}
]
📤 Saída Esperada
python[
    {"nome": "Mochila", "preco": 150.00},
    {"nome": "Tablet", "preco": 800.00}
]
'''
def filter_premium(products):
        return list(filter(lambda x: x.get("preco", 0) >= 100, products))

if __name__ == "__main__":
    pythonprodutos = [
        {"nome": "Caneta", "preco": 5.00},
        {"nome": "Caderno", "preco": 25.00},
        {"nome": "Mochila", "preco": 150.00},
        {"nome": "Estojo", "preco": 15.00},
        {"nome": "Tablet", "preco": 800.00}
    ]
    print(filter_premium(pythonprodutos))