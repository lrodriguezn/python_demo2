from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado
    CANCELLED = 4 #Cancelado


def check_order_statuss(status: OrderStatus):
    if status == OrderStatus.PENDING:
        print("El pedido esta pendiente")
    elif status == OrderStatus.SHIPPED:
        print("El pedido esta enviado")
    elif status == OrderStatus.DELIVERED:
        print("El pedido esta entregado")
    elif status == OrderStatus.CANCELLED:
        print("El pedido esta cancelado")

check_order_statuss(OrderStatus.PENDING)