import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') 

# Obtener el directorio actual
cwd = os.getcwd()
print("Directorio actual:", cwd)

# Obtener la lista de archivos y directorios en el directorio actual
files = [f for f in os.listdir(cwd) if f.endswith(".csv")] 
print("Archivos csv en el directorio actual:")
for file in files:
    print(file)

#limpiar_pantalla()