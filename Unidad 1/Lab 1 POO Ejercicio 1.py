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

    def atacar(self, personaje2):
        if personaje2.vida > 0:
            personaje2.vida -= self.ataque
            if personaje2.vida < 0:
                personaje2.vida = 0 

    def esta_vivo(self):
        return self.vida > 0

    def __str__(self):
        return f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}"

personaje1 = Personaje("Pedro", 50, 10)
personaje2 = Personaje("Luis", 45, 8)

while personaje1.esta_vivo() and personaje2.esta_vivo():
    print(f"\n{personaje1.nombre} ataca a {personaje2.nombre}")
    personaje1.atacar(personaje2)
    print(personaje1)
    print(personaje2)

    if not personaje2.esta_vivo():
        print(f"\n{personaje2.nombre} no puede continuar.")
        break

    print(f"\n{personaje2.nombre} ataca a {personaje1.nombre}")
    personaje2.atacar(personaje1)
    print(personaje1)
    print(personaje2)

    if not personaje1.esta_vivo():
        print(f"\n{personaje1.nombre} no puede continuar.")
        break
