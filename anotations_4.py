from typing import Optional

def find_empleado(empleados_ids: list[int] , empleado_id: int) -> Optional[int]:
    """
    Finds an employee ID in a list of employee IDs.

    Parameters:
    empleados_ids (list[int]): A list of employee IDs.
    empleado_id (int): The employee ID to search for.

    Returns:
    Optional[int]: The employee ID if found, otherwise None.
    """
    if empleado_id in empleados_ids:
        return empleado_id
    return None


empleados_ids = [1, 2, 3, 4, 5]
empleado_id = 33
encontrado = find_empleado(empleados_ids, empleado_id)
print(encontrado)

