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
