'''La universidad ofrecerá descuentos en la cafetería para estudiantes y
académicos. Los estudiantes tienen un 20% de descuento y los
académicos un 10%. Si una persona no es estudiante ni académico, no
tiene descuento. El sistema debe gestionar a los clientes, calcular el precio
final de su compra después de aplicar el descuento adecuado y registrar
las compras realizadas en la cafetería'''

class Cliente:
    __descuentos = {
        "estudiante": 0.20,
        "academico": 0.10,
        "otro": 0.0
    }

    def __init__(self, tipo_cliente, compra):
        if tipo_cliente not in Cliente.__descuentos:
            raise ValueError("Tipo de cliente no válido. Debe ser 'estudiante', 'academico' u 'otro'.")
        self.__tipo_cliente = tipo_cliente 
        self.__compra = max(0, compra) 

    @property
    def tipo_cliente(self):
        return self.__tipo_cliente

    @property
    def compra(self):
        return self.__compra

    @compra.setter
    def compra(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio de la compra no puede ser negativo.")
        self.__compra = nuevo_precio

    @staticmethod
    def calcular_precio_final(precio, descuento):
        return precio * (1 - descuento)

    def obtener_precio_final(self):
        descuento = Cliente.__descuentos[self.__tipo_cliente]
        return Cliente.calcular_precio_final(self.__compra, descuento)

    def registrar_compra(self):
        precio_final = self.obtener_precio_final()
        print(f"Cliente tipo: {self.__tipo_cliente.capitalize()}\nCompra original: ${self.__compra:.2f}\nDescuento aplicado: {Cliente.__descuentos[self.__tipo_cliente] * 100}%\nPrecio final: ${precio_final:.2f}")

if __name__ == "__main__":
    try:
        cliente1 = Cliente("estudiante", 100)
        cliente1.registrar_compra()

        cliente2 = Cliente("academico", 150)
        cliente2.registrar_compra()

        cliente3 = Cliente("otro", 200)
        cliente3.registrar_compra()

        cliente1.compra = 120
        cliente1.registrar_compra()
    except ValueError as e:
        print(e)

#Encapsulación y Atributos Privados
          
#1A: El atributo privado deberia ser el del precio o compra, para evitar que la gente ocupe el descuento sin tenerlo 
#y el publico deberia ser el de ocupacion para que la gente sepa las opciones.

#2A: Se podria crear un diccionario o lista si se quiere organizar datos como el valor individual de diferentes productos como cafe,galletas,etc.
#sin embargo se puede ignorar esta opcion y simplemete agregar el descuento al valor final independiente de los productos
            
#2B: Seria util ya que permitiria una situacion mas inmersiva y personalizada donde se pueda escojer distintas opciones de productos con distintos precios
#en lugar de simplemete escribir un numero equibalente al precio, ademas de ver la diferencia individual del descuento en cada producto

#Variables de Clase
            
#1A: Personalmete prefiero aplicar al descuento al final de la compra, donde la persona coloca el valor total de la compra y se agrega el descuento dependiendo de ser necesario
 
#1B
            
#Accesores y Mutadores
        
#1A: De ser necesario un setter seria de utilidad para la modificacion de datos para modificar el producto que se quiere comprar o se podria poner la opcion de cancelar la compra  y volver a empezar

#1B: El cliente deberia saber la existencia de un descuento sin embargo este descuento solo se aplica al final de la compra, no veo la necesidad de un getter sin embargo se podria utilizar para obtener el valor de un producto individual y sin el descuento     

#Métodos Estáticos

#1A Un metodo estatico seria util para evitar la modificacion de precios, o el valor del descuento