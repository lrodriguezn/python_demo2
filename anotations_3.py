class Empleado:

    def __init__(self, nombre: str, edad: int, salario: float) -> None:
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def __str__(self) -> str:
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"
    
    def saludar(self) -> str:
        return f"Mi nombre es {self.nombre} y tengo {self.edad}"

empleado1 = Empleado("Luis", 30, 5000)

print(empleado1.__str__())
print(empleado1.saludar())

        