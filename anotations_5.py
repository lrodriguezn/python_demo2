from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Suma dos n meros y devuelve el resultado.
    
    Puede sumar dos enteros, dos flotantes o un entero y un flotante.
    
    Parameters
    ----------
    x : Union[int, float]
        Primer n mero a sumar.
    y : Union[int, float]
        Segundo n mero a sumar.
    
    Returns
    -------
    Union[int, float]
        La suma de x e y.
    """
    return x + y

result = add(1, 2)
print(result)

result = add(1.0, 2.0)
print(result)

result = add(1, 2.0) 
print(result)




