'''La universidad ofrecerá descuentos en la cafetería para estudiantes y
académicos. Los estudiantes tienen un 20% de descuento y los
académicos un 10%. Si una persona no es estudiante ni académico, no
tiene descuento. El sistema debe gestionar a los clientes, calcular el precio
final de su compra después de aplicar el descuento adecuado y registrar
las compras realizadas en la cafetería'''

class Cliente:
    def __init__(self, ocupacion, compra):
        self.ocupacion = ocupacion
        self.compra = compra

    def ocupacion(self, ocupacion):
        if ocupacion == 1:
            print("Se selecciono la opcion Estudiante tiene un "20%" de descuento")
        elif: ocupacion = 2:
            print("Se selecciono la opcion Academico tiene un "10%" de descuento ")
        else:
            print("Se selecciono la opcion Otro")
        
    def __compra(self, compra, ocupacion):
        if ocupacion = 1:
            compra= compra * 0.8
            print(f"El precio de su compra es de " {compra})
        elif: ocupacion = 2:
            compra = compra * 0.9
            print(f"El precio de su compra es de " {compra})
        else:  print(f"El precio de su compra es de " {compra})

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