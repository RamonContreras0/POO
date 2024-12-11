class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True

    def marcar_vendido(self):
        if self.__disponible:
            self.__disponible = False
        else:
            print(f"El vehículo {self.__marca} {self.__modelo} ya está vendido.")

    def esta_disponible(self):
        return self.__disponible

    def __str__(self):
        estado = "Disponible" if self.__disponible else "No disponible"
        return f"{self.__marca} {self.__modelo} ({self.__año}) - {estado}"


class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
        else:
            print("Solo se pueden agregar instancias de la clase Vehiculo.")

    def mostrar_vehiculos(self):
        print(f"Lista de vehículos en la concesionaria {self.nombre}:")
        for vehiculo in self.vehiculos:
            print(vehiculo)

    def vender_vehiculo(self, marca, modelo):
        for vehiculo in self.vehiculos:
            if vehiculo._Vehiculo__marca == marca and vehiculo._Vehiculo__modelo == modelo:
                if vehiculo.esta_disponible():
                    vehiculo.marcar_vendido()
                    print(f"El vehículo {marca} {modelo} ha sido vendido.")
                else:
                    print(f"El vehículo {marca} {modelo} no está disponible.")
                return
        print(f"El vehículo {marca} {modelo} no se encuentra en la concesionaria.")

# Interacción
concesionaria = Concesionaria("Autos Premium")

# Agregar vehículos
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Honda", "Civic", 2019)
vehiculo3 = Vehiculo("Ford", "Mustang", 2022)

concesionaria.agregar_vehiculo(vehiculo1)
concesionaria.agregar_vehiculo(vehiculo2)
concesionaria.agregar_vehiculo(vehiculo3)

# Mostrar vehículos disponibles
concesionaria.mostrar_vehiculos()

# Vender un vehículo
concesionaria.vender_vehiculo("Honda", "Civic")

# Mostrar vehículos después de la venta
concesionaria.mostrar_vehiculos()
