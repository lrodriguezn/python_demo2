import json

new_product = {
    'name' : "Cargador inalambrico",
    'price' : 230,
    'quantity' : 20,
    'brand' : 'ChangerMaster',
    'category' :'Accessories',
    'entry_date' : '2024-11-15'
}

with open('products.json','r') as file:
    products = json.load(file) #convierte el archivo json a un diccionario
    products.append(new_product) #agrega el nuevo producto al diccionario   

with open('products.json','w') as file: 
    json.dump(products, file, indent=4) #convierte el diccionario a un archivo json
    

