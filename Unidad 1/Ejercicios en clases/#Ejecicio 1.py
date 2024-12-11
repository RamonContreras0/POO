#Ejecicio 1
'''Tomando el código que hemos estado trabajando en la última clase, se solicita agregar nuevas
Propiedades a la clase Persona:
altura (float): Representa la altura de la persona en metros.
peso (float): Representa el peso de la persona en kilogramos.
Modificar el constructor __init__ para aceptar estos nuevos parámetros y asignarlos a las propiedades correspondientes.
Agregar un nuevo método para calcular el IMC
El método calcular_imc() debe calcular el Índice de Masa Corporal (IMC) de la persona utilizando la
fórmula (peso/altura^2)
El método debe devolver el valor del IMC y mostrar un mensaje indicando si la persona está en un
rango de peso normal, bajo peso, sobrepeso, u obesidad basado en el valor calculado.
Agregar un método llamado promedio_asignatura() a la clase Persona().
Este método debe recibir tres notas (valores de tipo float) como parámetros.
El método debe calcular el promedio de estas tres notas.
Si el promedio es igual o superior a 4.0, el método debe imprimir un mensaje indicando que la
persona aprobó la asignatura; de lo contrario, debe indicar que la persona no aprobó.'''

class Persona():

    #Constructor de Clase
    def __init__(self,nombre, apellido, edad, altura, peso, nota1, nota2, nota3):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    #Atributos de una clase (Caracteristicas compartidas por todos los objetos de la clase)
    #nombre = "Cristina"
    #apellido = "Torres"
    #edad = 23

    #Metodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} esta hablando")
    
    def caminar(self):
        print(f"{self.nombre} esta caminando")

    def calcular_imc(self):
        print(f"Su IMC es {self.peso/self.altura**2}")
        if (self.peso/self.altura**2) < 18.5:
            print("Segun el IMC esta bajo el peso normal")
        elif (self.peso/self.altura**2) >= 18.5 and (self.peso/self.altura**2) < 25:
            print("Segun el IMC esta dentro del rango normal de peso")
        elif (self.peso/self.altura**2) >= 25 and (self.peso/self.altura**2) < 35:
            print("Segun el IMC esta dentro del rango de sobrepeso")
        else: print(" Segun el IMC esta dentro de un rango de obesidad")

    def promedio_asignatura(self):
        print(f"El promedio es {(self.nota1 + self.nota2 + self.nota3)/3}")
        if ((self.nota1 + self.nota2 + self.nota3)/3) > 4:
            print("Has aprobado la asignatura")
        else: print("Has reprobado la asignatura")

#Creación de objetos de la clase persona
persona1 = Persona("Cristina", "Torres", 23, 1.65, 55, 5.5, 6, 5)

#Acceso a los atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellidos: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")
print(f"Altura: {persona1.altura}m")
print(f"Peso: {persona1.peso}k")
print(f"Nota1: {persona1.nota1}")
print(f"Nota2: {persona1.nota2}")
print(f"Nota3: {persona1.nota3}")

#Llamando a los metodos de la clase
persona1.hablar()
persona1.calcular_imc()
persona1.promedio_asignatura()
