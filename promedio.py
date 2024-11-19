def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.

    Parameters:
    notas (list): lista de notas.

    Returns:
    float: el promedio de las notas.
    """

    promedio = sum(notas) / len(notas)
    return promedio 

#imprimir promedio 
print(calcular_promedio([1, 2, 3, 4, 5])) 

