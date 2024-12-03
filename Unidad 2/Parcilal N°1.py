class Gato:
    def __init__(self, nombre, edad, color, ubicación):
        self.__nombre = nombre
        self.__edad = edad
        self.__color = color
        self.__energia = 100
        self.__hambre = 0

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return (f"Nombre: {self.__nombre}, Edad: {self.__edad}, Colo: {self.__color}"
                f"Energía: {self.__energia}, Hambre: {self.__hambre}")

    def jugar(self):
        if self.__energia > 20:
            print ("El gato tiene mucha energia y quiere jugar")
            self.__energia -= 20
            self.__hambre += 30
        else:
            print("El gato esta muy cansado para jugar")
    
    def comer(self, hambre):
        if hambre > 50:
            print ("El gato esta hambriento, le diste de comer")
            self.__hambre -= 40
            self.__energia += 20
        else:
            print("El gato no tiene hambre")

    
class Area:
    def __init__(self, nombre, capacidad, cantidadgatos):
        self.nombre = nombre
        self.gatos = cantidadgatos
        self.capacidadclientes = capacidad

    def añadirgato(self, capacidadgatos, cantidadgatosporarea):
        if cantidadgatosporarea < capacidadgatos:
            print("Es posible añadir mas gatos")
        else: 
            print("El area ya tiene el maximo de gatos posible")


class Inventario:
    def __init__(self, productos, alimentogatos, juguetegatos):
        self.productos = productos
        self.alimento = alimentogatos
        self.juguetes = juguetegatos


gato =(Gato, 1, 3, "naranjo")
gato2 =(Gato, 2, 6, "negro")
print(gato)
Area1 = (Area, "Primer piso",  4, 4, 12, 6)
print(Area1)
Area2 = (Area, "Segundo piso", 3, 2, 12, 3)
print(Area2)
Area3 = (Area, "Terraza", 3, 3, 12, 3)
print(Area3)
inventario=(Inventario, "café", "comidad de gatos", "juguete")
