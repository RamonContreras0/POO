from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        divisor_comun = gcd(self.numerador, self.denominador)
        self.numerador //= divisor_comun
        self.denominador //= divisor_comun
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

    def __str__(self):

        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):

        nuevo_numerador = self.numerador * otra.denominador + otra.numerador * self.denominador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, otra):

        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, otra):
        return (self.numerador == otra.numerador and
                self.denominador == otra.denominador)

f1 = Fraccion(1, 2)
f2 = Fraccion(2, 4)
f3 = Fraccion(3, 4)

print(f"Fracción 1: {f1}")  # Salida: 1/2
print(f"Fracción 2: {f2}")  # Salida: 1/2
print(f"Fracción 3: {f3}")  # Salida: 3/4

suma = f1 + f3
print(f"Suma: {suma}")  # Salida: 5/4

producto = f1 * f3
print(f"Producto: {producto}")  # Salida: 3/8

print(f"¿f1 es igual a f2? {f1 == f2}")  # Salida: True
print(f"¿f1 es igual a f3? {f1 == f3}")  # Salida: False
