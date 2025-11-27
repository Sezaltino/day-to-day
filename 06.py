'''
📋 Contexto
A inflação chegou! Você precisa reajustar todos os preços em 5% para o próximo mês.
🎯 Objetivo
Crie uma função reajustar_precos(produtos, percentual) que use map() e lambda para aumentar todos os preços.
📥 Entrada Esperada
pythonprodutos = [
    {"nome": "Arroz", "preco": 20.00},
    {"nome": "Feijão", "preco": 8.00},
    {"nome": "Macarrão", "preco": 5.00}
]
percentual_aumento = 5
📤 Saída Esperada
python[
    {"nome": "Arroz", "preco": 21.00},
    {"nome": "Feijão", "preco": 8.40},
    {"nome": "Macarrão", "preco": 5.25}
]
'''
def adjustment_prices(products, percent):
    return list(map(lambda product: {"nome": product.get("nome",""), "preco" : product.get("preco", 0) * (1 + percent/100)}, products))

if __name__ == "__main__":

    pythonprodutos = [
    {"nome": "Arroz", "preco": 20.00},
    {"nome": "Feijão", "preco": 8.00},
    {"nome": "Macarrão", "preco": 5.00}
    ]
    percents = 5

    print(adjustment_prices(pythonprodutos, percents))