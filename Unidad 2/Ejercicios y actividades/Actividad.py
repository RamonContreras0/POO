'''Contexto
Una cafetería necesita un sistema para gestionar sus pedidos, calcular costos y administrar
descuentos para clientes frecuentes. El sistema debe ser flexible y permitir cambios en los
precios de los productos, administrar descuentos de manera controlada y mantener la
integridad de los datos.
Objetivo
Implementar una clase Cafeteria que cumpla con los requisitos de la cafetería utilizando los
conceptos de encapsulación, accesores, mutadores, invariantes de clase, interfaz,
especificación de clase, asertos, variables de clase y métodos estáticos.
'''

class Cafeteria:
    tasa_descuento = 0.10

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__menu = {}
        self.__pedidos = []  

    def agregar_producto_menu(self, producto, precio):
        if producto in self.__menu:
            raise ValueError(f"El producto '{producto}' ya está en el menú.")
        assert precio > 0, "El precio debe ser mayor a cero."
        self.__menu[producto] = precio

    def agregar_pedido(self, producto):
        assert producto in self.__menu, f"El producto '{producto}' no está en el menú."
        self.__pedidos.append(producto)

    def calcular_total(self, frecuente=False):
        total = sum(self.__menu[producto] for producto in self.__pedidos)
        if frecuente:
            total = self.calcular_precio_con_descuento(total, self.tasa_descuento)
        return total

    @staticmethod
    def calcular_precio_con_descuento(monto, descuento):
        assert 0 <= descuento <= 1, "El descuento debe estar entre 0 y 1."
        assert monto >= 0, "El monto debe ser mayor o igual a cero."
        return monto * (1 - descuento)

    @property
    def menu(self):
        return self.__menu.copy()

    @property
    def pedidos(self):
        return self.__pedidos.copy()

    @classmethod
    def set_tasa_descuento(cls, nueva_tasa):
        assert 0 <= nueva_tasa <= 1, "La tasa de descuento debe estar entre 0 y 1."
        cls.tasa_descuento = nueva_tasa

mi_cafeteria = Cafeteria("Café Central")

mi_cafeteria.agregar_producto_menu("Café", 2.5)
mi_cafeteria.agregar_producto_menu("Té", 1.8)

mi_cafeteria.agregar_pedido("Café")
mi_cafeteria.agregar_pedido("Té")

print("Total:", mi_cafeteria.calcular_total())
print("Total con descuento:", mi_cafeteria.calcular_total(frecuente=True))
Cafeteria.set_tasa_descuento(0.15)
print("Total con nuevo descuento:", mi_cafeteria.calcular_total(frecuente=True))
