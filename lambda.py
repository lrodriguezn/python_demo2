add = lambda a, b: a + b
mul = lambda a, b: a * b

numbers = range(11)

#obtener cuadrados
lis_cuadrados = list(map(lambda x: x**2, numbers))

print(lis_cuadrados)

#obtener pares
list_pares = list(filter(lambda x: x% 2 == 0, numbers))
print(list_pares)

