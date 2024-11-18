import json

with open('products.json', 'r') as file:
    products = json.load(file) #convierte el archivo json a un diccionario
    for product in products: #recorre el diccionario
        print(product) #imprime el diccionario
        print(product['name'])
        print(product['price'])
        print(product['quantity'])
        print(product['brand'])
        print(product['category'])
        print(product['entry_date'])