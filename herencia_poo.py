class Vehicle:
    def __init__(self, brand,model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido.")
        else:
            print(f"El vehiculo {self.brand}. No está vendido.")

    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha."
        else:
            return f"El coche {self.brand} no está disponible."
        
    def stop_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} se ha detenido."
        else:
            return f"El coche {self.brand} no está disponible."

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha."
        else:
            return f"La bicicleta {self.brand} no está disponible."
        
    def stop_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} se ha detenido."
        else:
            return f"La bicicleta {self.brand} no está disponible."
          
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha."
        else:
            return f"El camión {self.brand} no está disponible."
        
    def stop_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} se ha detenido."
        else:
            return f"El camión {self.brand} no está disponible."
        
class Customer:
    def __init__(self,name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible.")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
            print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}.")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario.")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido.")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f" - {vehicle.brand} por {vehicle.get_price()}.")


# Crear instancias de coches
car1 = Car("Toyota", "Corolla", "20000")
car2 = Car("Honda","Civic", "22,000")
bike1 = Bike("MTB Optimus Aquila Max 13","Optimus", "12,000")

# Crear instancia de cliente
customer1 = Customer("Carlos")

# Crear instancia de concesionaria y registrar coches y clientes
dealer = Dealership()
dealer.add_vehicles(car1)
dealer.add_vehicles(car2)
dealer.add_vehicles(bike1)
dealer.register_customers(customer1)

#Mostrar coches disponibles
dealer.show_available_vehicle()

# cliente consulta un coche
customer1.inquire_vehicle(car1)
#cliente compra coche 
customer1.buy_vehicle(car1)
# Mostrar coches disponibles nuevamente
dealer.show_available_vehicle()
#cliente intenta comprar un coche ya vendido    
customer1.buy_vehicle(car1)                