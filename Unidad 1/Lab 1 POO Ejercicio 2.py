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
import random
import math
pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laboratorio N°2 - Ejercicio 2")

ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (0, 139, 255)
FPS = 60
reloj = pygame.time.Clock()
class Puntos:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.radio = 8 

    def mover(self):
        self.y += self.velocidad
        if self.y > ALTO: 
            self.reiniciar()

    def reiniciar(self):
        self.x = random.randint(0, ANCHO - self.radio)
        self.y = random.randint(-100, -40)

    def dibujar(self):
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radio)

class Triangulo:
    def __init__(self, x, y, velocidad, base, altura):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.base = base
        self.altura = altura

    def dibujar(self):
        puntos = [
            (self.x, self.y),
            (self.x - self.base // 2, self.y + self.altura), 
            (self.x + self.base // 2, self.y + self.altura), 
        ]
        pygame.draw.polygon(pantalla, AZUL, puntos)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.x - self.base // 2 > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x + self.base // 2 < ANCHO:
            self.x += self.velocidad

    def colision(self, punto):
        centro_x = self.x
        centro_y = self.y + self.altura // 2
        distancia = math.sqrt((centro_x - punto.x) ** 2 + (centro_y - punto.y) ** 2)
        return distancia < punto.radio + self.altura // 2

def main():
    puntos_rojos = [Puntos(random.randint(0, ANCHO - 10), random.randint(-100, -40), random.randint(2, 6)) for _ in range(5)]
    nave = Triangulo(ANCHO // 2, ALTO - 60, 8, 40, 30)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        teclas = pygame.key.get_pressed()
        nave.mover(teclas)
        pantalla.fill(NEGRO)

        for punto in puntos_rojos:
            punto.mover()
            punto.dibujar()
            if nave.colision(punto):
                corriendo = False

        nave.dibujar()

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
