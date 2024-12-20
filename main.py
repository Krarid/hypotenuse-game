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
from Numero import Numero
from configuracion import PANTALLA_ALTO, PANTALLA_ANCHO, FRAME

def hipotenusaAleatoria():
    return random.randint(10,20)

def calcularCateto(hipotenusa, ladoA):
    return pow((hipotenusa ** 2) - (ladoA ** 2), 1/2)

pygame.init()
pygame.font.init()

texto = pygame.font.Font(None, 36)
numeroTexto = pygame.font.Font(None, 20)

def crearTextoNumerico(numero, posX, posY):
    numeroSurf = numeroTexto.render(f'{numero}', True, (255, 102, 102))
    return Numero(numeroSurf, posX, posY)

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer(font_color='white',cursor_color= (255, 255, 255))

pantalla = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
clock = pygame.time.Clock()

triangulos = pygame.sprite.Group()
numeros = pygame.sprite.Group()

hipotenusa = hipotenusaAleatoria()
ladoA = 0
ladoB = 0

posX = PANTALLA_ANCHO
posY = PANTALLA_ALTO

while True:
    # Color negro del espacio
    pantalla.fill("black") 

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    pantalla.blit(textinput.surface, (158, 680))

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
                ladoA = int(textinput.value)
                ladoB = calcularCateto(hipotenusa, ladoA)

                print(f'Lado B: {ladoB}')
                print(f'Hipotenusa: {hipotenusa}', end='\n\n')

                triangulo = Triangulo(ladoB, ladoA)
                triangulo.ingresarHipotenusa(hipotenusa)

                # Si el usuario presiona enter entonces borra el contenido del input
                textinput.value = ''

                # Genera una hipotenusa aleatoria para el proximo triangulo
                hipotenusa = hipotenusaAleatoria()
                
                # Posicion aleatoria para el triangulo
                posX = random.randint(0, 1100)
                posY = random.randint(0, 500)

                triangulo.ingresarPosicionX(posX)
                triangulo.ingresarPosicionY(posY)

                triangulos.add(triangulo)

                # Lados e hipotenusa del triangulo
                numero = crearTextoNumerico(triangulo.obtenerLadoA(), posX - 12, triangulo.ladoA * 5 + posY)
                numeros.add(numero)

                numero = crearTextoNumerico(round(triangulo.obtenerLadoB(),2), triangulo.ladoB * 5 + posX - 12, posY + triangulo.ladoA * 10 + 12)
                numeros.add(numero)

                numero = crearTextoNumerico(triangulo.obtenerHipotenusa(), triangulo.ladoB * 5 + posX + 10, posY + triangulo.ladoA * 5)
                numeros.add(numero)
            
    # Muestra la hipotenusa
    hipotenusa_texto = texto.render(f'Hipotenusa: {hipotenusa}', True, (255, 255, 255))
    pantalla.blit(hipotenusa_texto, (10, 650))

    # Pide un lado del triangulo rectangulo
    hipotenusa_texto = texto.render('Lado A: ', True, (255, 255, 255))
    pantalla.blit(hipotenusa_texto, (10, 680))

    # Dibuja todos los triangulos creados hasta el momento
    for entity in triangulos:
        entity.draw(pantalla)

    # Dibuja todos los numeros creados hasta el momento
    for n in numeros:
        pantalla.blit(n.surf, n.rect)

    # Renderiza la pantalla
    pygame.display.flip()
    clock.tick(FRAME)