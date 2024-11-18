import csv

file_path = 'products.csv'
updated_file_path = 'updated_products.csv'

with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['total_value']
    with open(updated_file_path, mode='w', newline='') as updated_file:
        writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        writer.writeheader() #Escribe el encabezado
        for row in reader:
            row['total_value'] = int(row['quantity']) * float(row['price'])
            writer.writerow(row) #Escribe las filas