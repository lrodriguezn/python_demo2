class Libro:
    def __init__(self, titulo, autor ):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro {self.titulo} te ha sido asignado")
        else:
            print(f"Libro {self.titulo} no esta disponible")
    
    def devolver_libro(self):
        self.disponible = True
        print(f"Libro {self.titulo} nuevamente disponible")

class Usuario:
    def __init__(self, nombre, id):
        self.nombre =  nombre
        self.id = id
        self.lista_libros_prestados = []
    
    def prestar_libro(self, libro:Libro):
        if libro.disponible:
            libro.prestar_libro()
            self.lista_libros_prestados.append(libro)
        else:
            print(f"Libro {libro.titulo} ya esta prestado")
    
    def devolver_libro(self, libro:Libro):
        if  libro in self.lista_libros_prestados:
            libro.devolver_libro()
            self.lista_libros_prestados.remove(libro)
        else:
            print(f"Libro {libro.titulo}, no esta en tu bibloteca")
    
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def agregar_libro(self, libro:Libro):
        if libro not in self.libros:
            self.libros.append(libro)
            print(f"Libro {libro.titulo} agregado a la bibloteca")
        else:
            print("libro ya esta creado en la bibloteca")

    def eliminar_libro(self, libro:Libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro {libro.titulo} eliminado de la bibloteca")
        else:
            print("Libro no existe en la la bibloteca")
        
    def agregar_usuario(self, usuario:Usuario):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
            print(f"Usuario {usuario.nombre} agregado a la bibloteca")
        else:
            print("Usuario ya esta creado en la bibloteca")

    def eliminar_usuario(self, usuario:Usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuario {usuario.nombre} eliminado de la bibloteca")
        else:
            print("Usuario no existe en la la bibloteca")

    def mostrar_libros_biblioteca(self):
        print("libros disponibles")
        for libro in self.libros:
            if libro.disponible:
                print(f"Libro(Titulo:{libro.titulo}, Autor:{libro.autor} )")

    def mostrar_usuarios_biblioteca(self):
        for usuario in self.usuarios:
            print(f"Usuario(Nombre:{usuario.nombre}, Id:{usuario.id} )")

libro1 = Libro("Libro 1", "autor1")
libro2 = Libro("Libro 2", "autor2")

usuario1 = Usuario("usuario 1", "id1")

biblioteca = Biblioteca()

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_usuario(usuario1)

usuario1.prestar_libro(libro2)
biblioteca.mostrar_libros_biblioteca()

    
    
    



        
        