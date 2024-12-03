class Gato:
    def __init__(self, nombre, edad, color,energia, hambre, ubicación):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.energia = energia
        self.hambre = hambre
        self. ubicación= ubicación

    def jugar(self, energia):
        if energia > 20:
            print ("El gato tiene mucha energia y quiere jugar")
        else:
            print("El gato esta muy cansado para jugar")
    
    def comer(self, hambre):
        if hambre > 75:
            print ("El gato esta hambriento, le diste de comer")
            
        else:
            print("El gato no tiene hambre")

    
class Area:
    def __init__(self, nombrearea, capacidadclientes, cantidadgatosporarea, cantidadgatostotal, capacidadgatos):
        self.nombre = nombrearea
        self.gatos = cantidadgatosporarea
        self.gatostotal = cantidadgatostotal
        self.capacidadclientes = capacidadclientes
        self.capacidadgatos = capacidadgatos

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


gato =(Gato, 1, 3, "naranjo", 100, 0, "Primer piso")
gato2 =(Gato, 2, 6, "negro", 80, 15, "Terraza")
print(gato)
Area1 = (Area, "Primer piso",  4, 4, 12, 6)
print(Area1)
Area2 = (Area, "Segundo piso", 3, 2, 12, 3)
print(Area2)
Area3 = (Area, "Terraza", 3, 3, 12, 3)
print(Area3)
inventario=(Inventario, "café", "comidad de gatos", "juguete")
