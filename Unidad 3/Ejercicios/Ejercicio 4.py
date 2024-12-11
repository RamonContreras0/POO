'''Problema de Duck Typing
Estás desarrollando una aplicación para calcular el área de diferentes figuras geométricas. La aplicación no debe
preocuparse por el tipo exacto de la figura, sino por si esta puede calcular su área. Utilizando Duck Typing, implementa un
sistema donde cada figura geométrica tenga un método calcular_area() que realice el cálculo correspondiente.
El programa debe incluir las siguientes figuras geométricas:
Circulo
Rectángulo
Triángulo
Cuadrado
Trapecio
Pentágono Regular
Objetivo
1.Implementar las clases para las figuras mencionadas, asegurando que cada una tenga el método calcular_area().
Diseñar una función llamada mostrar_area que reciba cualquier figura geométrica y llame al método calcular_area()
para mostrar el área calculada.
'''

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Trapecio:
    def __init__(self, base_menor, base_mayor, altura):
        self.base_menor = base_menor
        self.base_mayor = base_mayor
        self.altura = altura

    def calcular_area(self):
        return ((self.base_menor + self.base_mayor) * self.altura) / 2

class PentagonoRegular:
    def __init__(self, lado, apotema):
        self.lado = lado
        self.apotema = apotema

    def calcular_area(self):
        perimetro = self.lado * 5
        return (perimetro * self.apotema) / 2

def mostrar_area(figura):
    try:
        area = figura.calcular_area()
        print(f"El área de la figura es: {area:.2f}")
    except AttributeError:
        print("El objeto proporcionado no tiene un método calcular_area().")

if __name__ == "__main__":
    figuras = [
        Circulo(5),
        Rectangulo(10, 4),
        Triangulo(6, 3),
        Cuadrado(4),
        Trapecio(3, 5, 4),
        PentagonoRegular(6, 4)
    ]

    for figura in figuras:
        mostrar_area(figura)