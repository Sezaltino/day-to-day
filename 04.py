import copy


def apply_discounts(list_product, discount):
    #Function Variables 
    discounted_products = [copy.deepcopy(set_products) for set_products in list_product]
    discounted_products = list({key: round((value - value * discount/100), 2) if key == "preco" else value for key, value in index.items()} for index in discounted_products)

    return discounted_products

if __name__ == "__main__":
    products = [
    {"nome": "Notebook", "preco": 3000.00},
    {"nome": "Mouse", "preco": 50.00},
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Monitor", "preco": 800.00}
    ]
    discount_product = 13.3
    print(apply_discounts(products, discount_product))
