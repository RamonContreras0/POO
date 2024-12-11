'''Objetivo
En esta actividad, aplicarás los conceptos de herencia en Python para extender una jerarquía de clases que
representa animales. Trabajarás con subclases, métodos, atributos específicos y la función super() para inicializar la
superclase.
Parte 1: Completar la Superclase Animal
1.Agregar Atributo peso, además de otros atributos que estimes generales de un animal.
2.Crear un método que permita imprimir el sonido de cada animal.
Parte 2: Mejorar las Subclases Perro y Gato
1.Crear un método en cada subclase que imprima los datos completos del animal
Parte 3: Crear Nuevas Subclases Pájaro y Pez
Parte 4: Crear Instancias y Probar el Código
'''
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def hacer_sonido(self):
        return "Sonido genérico de animal"

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso}kg"

class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau guau"

    def imprimir_datos(self):
        return f"{super().__str__()}, Raza: {self.raza}"

class Gato(Animal):
    def __init__(self, nombre, edad, peso, color_pelaje):
        super().__init__(nombre, edad, peso)
        self.color_pelaje = color_pelaje

    def hacer_sonido(self):
        return "Miau"

    def imprimir_datos(self):
        return f"{super().__str__()}, Color de pelaje: {self.color_pelaje}"

class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, plumas):
        super().__init__(nombre, edad, peso)
        self.plumas = plumas

    def hacer_sonido(self):
        return "Pío pío"

    def imprimir_datos(self):
        return f"{super().__str__()}, color de plumas: {self.plumas}"

class Pez(Animal):
    def __init__(self, nombre, edad, peso, tipo_agua):
        super().__init__(nombre, edad, peso)
        self.tipo_agua = tipo_agua

    def hacer_sonido(self):
        return "Blub blub"

    def imprimir_datos(self):
        return f"{super().__str__()}, Tipo de agua: {self.tipo_agua}"

if __name__ == "__main__":
    perro = Perro("Dogi", 5, 20, "Labrador")
    gato = Gato("Michi", 3, 4, "Negro")
    pajaro = Pajaro("Pini", 1, 0.2, "Azules")
    pez = Pez("Nemo", 2, 0.5, "Agua salada")

    animales = [perro, gato, pajaro, pez]

    for animal in animales:
        print(animal.imprimir_datos())
        print(f"Sonido: {animal.hacer_sonido()}\n")
