'''3. Imagina que estás diseñando un sistema para gestionar cuentas bancarias. Para ello, crea
una clase llamada CuentaBancaria que modele el comportamiento básico de una cuenta de
banco. El sistema debe permitir realizar operaciones como depósitos, retiros y consultar el
saldo actual. Además, se debe utilizar el concepto de encapsulamiento para proteger la
información sensible de la cuenta. Asegúrate de encapsular adecuadamente los atributos
que consideres sensibles. Dene métodos para interactuar con estos atributos de manera
controlada.
Consideraciones de Encapsulamiento
● ¿Qué atributos deberían ser privados y por qué?
● ¿Qué métodos utilizarías para acceder o modicar estos atributos de manera
controlada? Por ejemplo, permitiendo consultar el saldo pero no modicarlo
directamente.
'''

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular 
        self.__saldo = saldo_inicial 

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.__saldo:
                self.__saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser positivo.")

    def consultar_saldo(self):
        return f"El saldo actual es: {self.__saldo}"

    def obtener_titular(self):
        return self.__titular

    def cambiar_titular(self, nuevo_titular):
        if nuevo_titular:
            self.__titular = nuevo_titular
            print(f"El titular de la cuenta ha sido actualizado a: {self.__titular}")
        else:
            print("El nombre del titular no puede estar vacío.")

cuenta = CuentaBancaria("Juan Pérez", 500)
print(cuenta.consultar_saldo())  # Saldo inicial
cuenta.depositar(200)           # Depósito
cuenta.retirar(100)             # Retiro
print(cuenta.obtener_titular()) # Consultar titular
cuenta.cambiar_titular("Ana López")
print(cuenta.obtener_titular())