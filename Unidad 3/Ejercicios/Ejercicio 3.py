'''Una empresa está desarrollando un sistema de gestión de pagos para su plataforma
de comercio electrónico. La plataforma admite diferentes métodos de pago, como
tarjetas de crédito, transferencias bancarias y pagos en efectivo. Cada método de
pago tiene un comportamiento diferente. Por ejemplo:
1.Las tarjetas de crédito necesitan ser validadas antes de procesar el pago.
Las transferencias bancarias requieren un código de confirmación antes de
completar la transacción.
2.
Los pagos en efectivo no necesitan validación ni confirmación, solo deben registrar
el monto recibido.
3.
Actualmente, la clase base MetodoDePago() incluye un método procesar_pago() que
asume que todos los métodos de pago deben validarse antes de procesarse. Sin
embargo, este diseño está causando problemas, ya que los pagos en efectivo no
necesitan validación, y algunos métodos de pago están lanzando excepciones
inesperadas.
 
Problema a Resolver
El sistema actual viola el Principio de Sustitución de Liskov (LSP) porque no todos los
métodos de pago respetan el comportamiento esperado de la clase base.
Tu tarea es rediseñar la jerarquía de clases para que los métodos de pago cumplan
con el LSP, asegurando que las subclases puedan ser utilizadas de forma
intercambiable sin romper el programa.'''

from abc import ABC, abstractmethod

class MetodoDePago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoConValidacion(MetodoDePago):
    @abstractmethod
    def validar(self):
        pass
    
    def procesar_pago(self, monto):
        self.validar()
        print(f"Procesando pago de {monto} con validación.")

class PagoConConfirmacion(MetodoDePago):
    @abstractmethod
    def confirmar(self):
        pass
    
    def procesar_pago(self, monto):
        self.confirmar()
        print(f"Procesando pago de {monto} con confirmación.")

class PagoSimple(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Procesando pago simple de {monto}.")

class TarjetaDeCredito(PagoConValidacion):
    def validar(self):
        print("Validando tarjeta de crédito...")

class TransferenciaBancaria(PagoConConfirmacion):
    def confirmar(self):
        print("Confirmando transferencia bancaria...")

class PagoEnEfectivo(PagoSimple):
    pass

def procesar(metodo_pago: MetodoDePago, monto):
    metodo_pago.procesar_pago(monto)

tarjeta = TarjetaDeCredito()
transferencia = TransferenciaBancaria()
efectivo = PagoEnEfectivo()

procesar(tarjeta, 100)
procesar(transferencia, 200)
procesar(efectivo, 50)
