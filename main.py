import pygame
import pygame_textinput

# Importa solo las teclas que pueden ser presionadas
from pygame.locals import (
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT
)

from Triangulo import Triangulo
from configuracion import PANTALLA_ALTO, PANTALLA_ANCHO, FRAME

pygame.init()
pygame.font.init()

texto = pygame.font.Font(None, 36)

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer(font_color='white',cursor_color= (255, 255, 255))

pantalla = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
clock = pygame.time.Clock()

triangulo = Triangulo()
triangulo.hipotenusaAleatoria()

while True:
    # Color negro del espacio
    pantalla.fill("black") 

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    pantalla.blit(textinput.surface, (158, 600))

    # Procesa eventos
    for event in events:

        if event.type == QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                raise SystemExit

            if event.key == K_RETURN:
                print("Entrada: ", textinput.value)
                triangulo.ingresarLadoA(int(textinput.value))
                triangulo.calcularCateto()
                
                textinput.value = ''
                triangulo.hipotenusaAleatoria()

            
    # Muestra la hipotenusa
    hipotenusa_texto = texto.render(f'Hipotenusa: {triangulo.obtenerHipotenusa()}', True, (255, 255, 255))
    pantalla.blit(hipotenusa_texto, (10, 570))

    # Pide un lado del triangulo rectangulo
    hipotenusa_texto = texto.render('Lado A: ', True, (255, 255, 255))
    pantalla.blit(hipotenusa_texto, (10, 600))

    # Muestra el lado B
    ladoB_texto = texto.render(f'Lado B: {triangulo.obtenerLadoB()}', True, (255, 255, 255))
    pantalla.blit(ladoB_texto, (10, 630))

    pygame.draw.polygon(pantalla, 'white', [(100, 0), (100, 100), (200, 100)], 0)

    pygame.display.flip()
    clock.tick(FRAME)