def factorial(numero):
    if numero > 0:
        return numero * factorial(numero-1)
    return 1

def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)
    return 1

n1 = 10
print(f"factorial {n1}:",factorial(n1))
print(f"fibonacci {n1}:",fibonacci(n1))