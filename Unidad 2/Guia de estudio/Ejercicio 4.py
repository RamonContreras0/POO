from datetime import datetime

class Planta:
    def __init__(self, tipo, estado_crecimiento, agua_necesaria, fertilizante_necesario):
        self._tipo = tipo
        self._estado_crecimiento = estado_crecimiento
        self._agua_necesaria = agua_necesaria
        self._fertilizante_necesario = fertilizante_necesario
        self._último_riego = None
        self._último_fertilizado = None
    
    # Getters y setters
    def get_tipo(self):
        return self._tipo
    
    def set_estado_crecimiento(self, estado):
        self._estado_crecimiento = estado

    def regar(self):
        self._último_riego = datetime.now()
        print(f"{self._tipo} ha sido regada.")
    
    def fertilizar(self):
        self._último_fertilizado = datetime.now()
        print(f"{self._tipo} ha sido fertilizada.")

    def __str__(self):
        return f"{self._tipo} ({self._estado_crecimiento}): Agua necesaria {self._agua_necesaria}L, Fertilizante necesario {self._fertilizante_necesario}."
    
class AreaJardin:
    def __init__(self, nombre):
        self.nombre = nombre
        self.plantas = []
    
    def agregar_planta(self, planta):
        self.plantas.append(planta)
    
    def eliminar_planta(self, planta):
        if planta in self.plantas:
            self.plantas.remove(planta)
    
    def __str__(self):
        return f"Área: {self.nombre}, Plantas: {len(self.plantas)}"

def calcular_agua_necesaria(self):
    if self._estado_crecimiento == "semilla":
        return self._agua_necesaria * 0.5
    elif self._estado_crecimiento == "brote":
        return self._agua_necesaria * 0.75
    return self._agua_necesaria

class Recurso:
    def __init__(self, nombre, cantidad_disponible):
        self.nombre = nombre
        self.cantidad_disponible = cantidad_disponible
    
    def usar_recurso(self, cantidad):
        if self.cantidad_disponible >= cantidad:
            self.cantidad_disponible -= cantidad
        else:
            raise ValueError("Cantidad insuficiente.")
    
    def __str__(self):
        return f"{self.nombre}: {self.cantidad_disponible} unidades disponibles."

def crecer(self):
    estados = ["semilla", "brote", "adulta"]
    if self._estado_crecimiento in estados:
        indice_actual = estados.index(self._estado_crecimiento)
        if indice_actual < len(estados) - 1:
            self._estado_crecimiento = estados[indice_actual + 1]
class Jardin:
    def __init__(self):
        self.areas = []
        self.recursos = {}
    
    def agregar_area(self, area):
        self.areas.append(area)
    
    def agregar_recurso(self, recurso):
        self.recursos[recurso.nombre] = recurso
    
    def __str__(self):
        return f"Jardín con {len(self.areas)} áreas y {len(self.recursos)} recursos."
planta1 = Planta("Rosa", "Rosa", "Semilla", 1.5)
planta2 = Planta("Girasol", "Girasol", "Brote", 2.0)
garden_area = AreaJardin("Área de flores")
print(planta1)
print(planta2)


