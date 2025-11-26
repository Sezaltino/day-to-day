'''
Dia 4 – Aplicar Descontos em Produtos
📋 Contexto
É Black Friday! Sua loja decidiu aplicar 10% de desconto em todos os produtos. Você precisa atualizar a lista de preços rapidamente.
🎯 Objetivo
Crie uma função aplicar_desconto(produtos, percentual) que receba uma lista de dicionários de produtos e retorne uma nova lista com os preços atualizados.
📥 Entrada Esperada
pythonprodutos = [
    {"nome": "Notebook", "preco": 3000.00},
    {"nome": "Mouse", "preco": 50.00},
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Monitor", "preco": 800.00}
]
percentual_desconto = 10
📤 Saída Esperada
python[
    {"nome": "Notebook", "preco": 2700.00},
    {"nome": "Mouse", "preco": 45.00},
    {"nome": "Teclado", "preco": 135.00},
    {"nome": "Monitor", "preco": 720.00}
]
'''
def apply_discounts(list_product, discount):
    return list({key: round((value - value * discount/100), 2) if key == "preco" else value for key, value in index.items()} for index in list_product)

if __name__ == "__main__":
    products = [
    {"nome": "Notebook", "preco": 3000.00},
    {"nome": "Mouse", "preco": 50.00},
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Monitor", "preco": 800.00}
    ]
    discount_product = float(input("Digite o percentual de desconto: "))

    while discount_product < 0 or discount_product > 100:
        discount_product = float(input("Digite o percentual de desconto: "))

    print(apply_discounts(products, discount_product))
