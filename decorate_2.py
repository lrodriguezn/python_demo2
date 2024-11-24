def chech_access(func):
    def wrapper(employee):
        if employee.get('role') == 'admin':
            func(employee)
        else:
            print(f"ACCESO DENEGADO: SOLO LOS ADMINISTRADORES PUEDEN ACCEDER A ESTA FUNCION")
            
    return wrapper

@chech_access
def delete_employee(employee):
    print(f"El empleado {employee.get('name')} ha sido eliminado")

admin = {'name': 'John', 'role': 'admin'}
empleado = {'name': 'Luis', 'role': 'empleado'}

delete_employee(admin)
#delete_employee(empleado)