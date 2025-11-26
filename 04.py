import copy


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

    print(products)

    while discount_product < 0 or discount_product > 100:
        discount_product = float(input("Digite o percentual de desconto: "))

    
    print(apply_discounts(products, discount_product))
