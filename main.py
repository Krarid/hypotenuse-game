import pygame
import pygame_textinput
import random

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
numero = pygame.font.Font(None, 20)

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer(font_color='white',cursor_color= (255, 255, 255))

pantalla = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
clock = pygame.time.Clock()

triangulo = Triangulo()
triangulo.hipotenusaAleatoria()

posX = PANTALLA_ANCHO
posY = PANTALLA_ALTO

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
                print("Lado A: ", textinput.value)
                triangulo.ingresarLadoA(int(textinput.value))
                triangulo.calcularCateto()

                print(f'Lado B: {triangulo.obtenerLadoB()}')
                print(f'Hipotenusa: {triangulo.obtenerHipotenusa()}', end='\n\n')

                textinput.value = ''

                # Genera una hipotenusa aleatoria para el proximo triangulo
                triangulo.hipotenusaAleatoria()
                
                # Posicion aleatoria para el triangulo
                posX = random.randint(0, 1100)
                posY = random.randint(0, 500)

            
    # Muestra la hipotenusa
    hipotenusa_texto = texto.render(f'Hipotenusa: {triangulo.obtenerHipotenusa()}', True, (255, 255, 255))
    pantalla.blit(hipotenusa_texto, (10, 570))

    # Pide un lado del triangulo rectangulo
    hipotenusa_texto = texto.render('Lado A: ', True, (255, 255, 255))
    pantalla.blit(hipotenusa_texto, (10, 600))

    # Muestra el lado B
    ladoB_texto = texto.render(f'Lado B: {triangulo.obtenerLadoB()}', True, (255, 255, 255))
    pantalla.blit(ladoB_texto, (10, 630))

    # Dibuja el triangulo
    pygame.draw.polygon(pantalla, 'white', 
    [(posX, posY), # 
    (posX, triangulo.ladoA * 10 + posY), 
    (posX + triangulo.ladoB * 10, triangulo.ladoA * 10 + posY)], 0)

    # Dibuja los lados del triangulo generado
    ladoA_numero = numero.render(f'{triangulo.obtenerLadoA()}', True, (255, 0, 0))
    pantalla.blit(ladoA_numero, (posX - 17, triangulo.ladoA * 5 + posY))

    ladoB_numero = numero.render(f'{round(triangulo.obtenerLadoB(),2)}', True, (255, 0, 0))
    pantalla.blit(ladoB_numero, (triangulo.ladoB * 5 + posX - 12, posY + triangulo.ladoA * 10 + 5))

    hipotenusa_numero = numero.render(f'{triangulo.obtenerHipotenusa()}', True, (255, 0, 0))
    pantalla.blit(hipotenusa_numero, (triangulo.ladoB * 5 + posX + 10, posY + triangulo.ladoA * 5))

    # Renderiza la pantalla
    pygame.display.flip()
    clock.tick(FRAME)