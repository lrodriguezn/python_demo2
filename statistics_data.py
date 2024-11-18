import statistics
import csv

monthy_sales ={}

with open('monthy_sales.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    monthy_sales = {row['month']:int(row['sales']) for row in csv_reader}

    ##for row in csv_reader:
    ##    monthy_sales[row['month']] = row['sales']
    
    sales =list(monthy_sales.values())

    #hallar la media
    media = statistics.mean(sales)
    print(f"La media es: {media}")

    #hallar la mediana
    mediana = statistics.median(sales)
    print(f"La mediana es: {mediana}")

    #hallar la moda
    moda = statistics.mode(sales)
    print(f"La moda es: {moda}")

    #hallar la desviacion estandar
    desviacion = statistics.stdev(sales)
    print(f"La desviacion estandar es: {desviacion}")

    #hallar la varianza
    varianza = statistics.variance(sales)    
    print(f"La varianza es: {varianza}")
    