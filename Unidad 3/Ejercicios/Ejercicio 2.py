'''Diseñar un sistema para un videojuego de carreras
donde los vehículos tienen características y
comportamientos compartidos, pero también
pueden combinar atributos de diferentes tipos
(como "Terrestres " , "Acuáticos " o "Aéreos"). Utilizar
herencia múltiple para crear vehículos híbridos y
polimorfismo para manejar diferentes tipos de
vehículos de manera uniforme.'''

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

    def descripcion(self):
        return f"Soy un {self.nombre}"

class Terrestre(Vehiculo):
    def acelerar(self):
        return f"{self.nombre}: Acelerando en tierra!"

    def frenar(self):
        return f"{self.nombre}: Frenando en tierra!"

class Acuatico(Vehiculo):
    def acelerar(self):
        return f"{self.nombre}: Acelerando en el agua!"

    def frenar(self):
        return f"{self.nombre}: Frenando en el agua!"

class Aereo(Vehiculo):
    def acelerar(self):
        return f"{self.nombre}: Acelerando en el aire!"

    def frenar(self):
        return f"{self.nombre}: Frenando en el aire!"

class HibridoTerrestreAcuatico(Terrestre, Acuatico):
    def descripcion(self):
        return f"{self.nombre}: Soy un vehículo híbrido terrestre y acuático."

class HibridoAcuaticoAereo(Acuatico, Aereo):
    def descripcion(self):
        return f"{self.nombre}: Soy un vehículo híbrido acuático y aéreo."

def manejar_vehiculo(vehiculo):
    print(vehiculo.descripcion())
    print(vehiculo.acelerar())
    print(vehiculo.frenar())

# Crear instancias
moto = Terrestre("Moto")
lancha = Acuatico("Lancha")
avion = Aereo("Avión")
amfibia = HibridoTerrestreAcuatico("Amfibia")
hidroavion = HibridoAcuaticoAereo("Hidroavión")

vehiculos = [moto, lancha, avion, amfibia, hidroavion]

for vehiculo in vehiculos:
    manejar_vehiculo(vehiculo)
    print("-" * 40)
