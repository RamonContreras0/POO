'''Crea la clase Coche que contenga las siguientes propiedades:
marca (string): La marca del coche.
gasolina (float): La cantidad de gasolina disponible en el coche.
La clase tendrá un método llamado conducir() que recibirá como argumento el número de kilómetros a
recorrer y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. Por cada 10
kilómetros recorridos, se restará 1 litro de gasolina al valor de la propiedad gasolina. Si la gasolina no es
suficiente para recorrer la distancia solicitada, el coche conducirá solo hasta donde alcance la gasolina y
mostrará un mensaje indicando que se ha quedado sin gasolina.
Además, la clase contendrá otro método llamado cargar_gasolina() que recibirá como argumento los
litros de gasolina que se desean agregar al coche, sumando estos litros al valor de la propiedad gasolina.'''

class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0

    def conducir(self, kilometros):
        combustible_necesario = kilometros / 10
        
        if self.gasolina >= combustible_necesario:
            self.kilometros_recorridos += kilometros
            self.gasolina -= combustible_necesario
            print(f"Has recorrido {kilometros} kilómetros. Gasolina restante: {self.gasolina:.2f} litros.")
        else:
            distancia_posible = self.gasolina * 10
            self.kilometros_recorridos += distancia_posible
            self.gasolina = 0
            print(f"Te has quedado sin gasolina tras recorrer {distancia_posible:.2f} kilómetros.")

    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Has añadido {litros} litros de gasolina. Gasolina total: {self.gasolina:.2f} litros.")


mi_coche = Coche("Toyota", 5)
mi_coche.conducir(40)
mi_coche.cargar_gasolina(3)
mi_coche.conducir(100)
