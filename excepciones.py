## Funcion que muestra arbol de Excepciones de python
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)

"""
while True: 
    try:
        divisor = int(input("ingresa un numero:"))
        resul = print(100/divisor)
    except ZeroDivisionError as e:
        print("divisor no puede ser cero")
        print(e)
    except ValueError as e:
        print("Error de tipo de dato")
        print(e)
"""