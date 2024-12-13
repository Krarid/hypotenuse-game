import pygame

# Importa solo las teclas que pueden ser presionadas
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
from Triangulo import Triangulo
from configuracion import PANTALLA_ALTO, PANTALLA_ANCHO, FRAME

pantalla = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
clock = pygame.time.Clock()

while True:

    # Procesa eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                raise SystemExit
            
    pygame.draw.polygon(pantalla, 'white', [(100, 100), (200, 100), (100, 0)], 0)

    pygame.display.flip()
    clock.tick(FRAME)