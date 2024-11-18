#leer un archivo linea por linea
"""with open('file.txt','r') as file:
    for lineas in file:
        print(lineas.strip())"""

#leer todas las lineas en una lista
"""with open('file.txt','r') as file:
    lineas = file.readlines()
    print(lineas)"""

#Añadir texto en el archivo
"""with open('file.txt','a') as file:
    file.write("\n\nBy ChatGPT")"""

#Sobre escribir archivo
"""with open('file.txt','w') as file:
    file.write("\n\nBy ChatGPT")"""


