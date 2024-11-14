class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad}")


persona1 = Persona(nombre="Luis G", edad=30)

persona1.saludar()