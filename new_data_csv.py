import csv

new_product = {
    'name' : "Cargador inalambrico",
    'price' : 230,
    'quantity' : 20,
    'brand' : 'ChangerMaster',
    'category' :'Accessories',
    'entry_date' : '2024-11-15'
}

with open('products.csv','a') as file:
    file.write('\n')
    csv_write = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_write.writerow(new_product)
