'''1. Implementar un sistema básico para gestionar personajes de un
videojuego utilizando programación orientada a objetos.
Cada personaje tendrá un nombre, nivel de vida y puntos de ataque. La
idea es que los personajes puedan interactuar entre ellos, permitiendo
que un personaje ataque a otro, lo que disminuirá su vida. Además,
deberás verificar si un personaje está vivo o no.'''

'''Requerimientos:
1. Clase Personaje:
○ Atributos: el nombre del personaje, el nivel de vida del personaje y los
puntos de ataque del personaje.
○ Métodos: un método que permita que el personaje ataque a otro,
disminuyendo la vida del otro personaje según los puntos de ataque del
atacante. Un segundo método, que verifique si el personaje sigue vivo. Debe
devolver True si el nivel de vida es mayor a 0, y False si no. Por último
implementar un método mágico que permita devolver un string que muestre
el estado del personaje (nombre, vida, y ataque).
Instrucciones:
1. Implementar la clase Personaje con los atributos y métodos descritos
anteriormente.
2. Crear al menos dos personajes. Cada personaje debe tener un nombre, vida inicial y
puntos de ataque.
3. Simula un combate entre los personajes haciendo que uno ataque al otro. Después
de cada ataque, se debe mostrar el estado de ambos personajes.
4. Repetir los ataques hasta que uno de los personajes quede sin vida. Utiliza un
método para verificar si el personaje sigue en pie.'''

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

class Personaje2:
    def __init__(self, nombre2, vida2, ataque2):
        self.nombre = nombre2
        self.vida = vida2
        self.ataque = ataque2

def daño(self, vidarestante):
    self.vidarestante = self.vida - self.ataque2
    vida = True
    while vida:
        if vidarestante > 0 :
            print(f"{self.nombre} resivio un ataque de {self.ataque2} de daño, le queda {self.vidarestante} de vida")
        else : vida = False
        print(f"{self.nombre} resivio un ataque de {self.ataque2} de daño, no le queda vida para continuar")

    self.vidarestante = self.vida2 - self.ataque
    vida2 = True
    while vida:
        if vidarestante > 0 :
            print(f"{self.nombre2} resivio un ataque de {self.ataque} de daño, le queda {self.vidarestante} de vida")
        else : vida = False
        print(f"{self.nombre2} resivio un ataque de {self.ataque} de daño, no le queda vida para continuar")
    

personaje1=[Personaje ("Pedro", 50, 3)]
personaje2=[Personaje2 ("Luis", 45, 4)]


