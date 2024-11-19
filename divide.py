def division(a: int, b: int) -> float:
    #valiar los tipos de datos
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los argumentos deben ser enteros")
    
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    
    return a / b


if __name__ == '__main__':
    try:
        print(division(10, 0))
    except (ZeroDivisionError,TypeError) as e:
        print(e)
