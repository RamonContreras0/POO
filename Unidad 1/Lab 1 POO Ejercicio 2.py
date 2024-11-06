'''2. A continuación, se proporciona el código base puntos rojos que ya caen y
se reinician automáticamente en la ventana del juego. El ejercicio consiste
en implementar la clase Triangulo, que representará la nave, y el
mecanismo de detección de colisiones.
Crear una nave (representada por un triángulo azul) que se mueva solamente
horizontalmente y esquive los puntos rojos que caen desde la parte superior de la pantalla.
Además, deberás implementar la funcionalidad de colisión: si un punto rojo toca el triángulo,
el juego se debe cerrar.
Instrucciones:
1. Implementar la clase Triangulo, que simulará la nave espacial. Esta debe moverse
de izquierda a derecha con las teclas de flecha (izquierda y derecha).
2. La nave será un triángulo de color azul que se dibujará en la parte inferior de la
pantalla.
3. Implementar un método que detecte la colisión entre la nave y los puntos rojos.
4. Cuando se detecte una colisión, el juego debe terminar.
5. Usar las dimensiones del triángulo y el radio de los puntos rojos para calcular si hay
una colisión. Se sugiere usar la distancia entre los centros de ambas figuras para
esta detección.'''

import pygame
pygame.init

AZUL = (0, 139, 255)

class Triangulo:
    def __init__(self, x, y , velocidad, altura, base):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.altura= altura
        self.base= base

    def dibujar(self):
        pygame.draw.lines(AZUL, (self.x, self.y))
    
    def movimiento(self, derecha, izquierda):
        self.derecha = derecha
        self.derecha += self.velocidad
        self.izquierda = izquierda
        self.izquierda += self.velocidad
        derecha = pygame.K_RIGHT
        izquierda = pygame.K_LEFT

triangulo=[Triangulo(50 , 30, 6, 20, 30)]

