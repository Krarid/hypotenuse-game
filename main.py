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
from Cuadrado import Cuadrado
from Numero import Numero
from configuracion import PANTALLA_ALTO, PANTALLA_ANCHO, FRAME

# Genera una hipotenusa aleatoria
def hipotenusaAleatoria():
    return random.randint(10,20)

# Calcula el catego en base a la hipotenusa y otro cateto
def calcularCateto(hipotenusa, ladoA):
    return pow((hipotenusa ** 2) - (ladoA ** 2), 1/2)

pygame.init()
pygame.font.init()

texto = pygame.font.Font(None, 36)
numeroTexto = pygame.font.Font(None, 20)
titulo = pygame.font.Font(None, 60)

# Funcion para crear numeros en la pantalla
def crearTextoNumerico(numero, posX, posY):
    numeroSurf = numeroTexto.render(f'{numero}', True, (255, 102, 102))
    return Numero(numeroSurf, posX, posY)

# Crea el objeto para el ingreso de texto en Pygame
textinput = pygame_textinput.TextInputVisualizer(font_color='white',cursor_color= (255, 255, 255))

pantalla = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
clock = pygame.time.Clock()

triangulos = pygame.sprite.Group()
numeros = pygame.sprite.Group()
cuadrados = pygame.sprite.Group()

hipotenusa = hipotenusaAleatoria()
ladoA = 0
ladoB = 0

posX = PANTALLA_ANCHO
posY = PANTALLA_ALTO

# Initializing Color
blanco = (255,255,255)
negro = (0,0,0)

mostrar_error = False
colision = False

while True:
    # Color negro del espacio
    pantalla.fill("black") 

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    pantalla.blit(textinput.surface, (158, 650))

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
                # Calcula los lados del triangulo
                try:
                    # Si se ingresa texto entonces manda una excepcion y repite el proceso
                    ladoA = int(textinput.value)

                    # Si se ingresa un lado menor que 0 o mayor o igual que la hipotenusa entonces muestra error y reinicia
                    if(not(ladoA > 0 and ladoA < hipotenusa)):
                        raise ValueError

                    ladoB = calcularCateto(hipotenusa, ladoA)

                    # Imprime los lados e hipotenusa
                    print("Lado A: ", textinput.value)
                    print(f'Lado B: {ladoB}')
                    print(f'Hipotenusa: {hipotenusa}', end='\n\n')

                    # Posicion aleatoria para el triangulo
                    posX = random.randint(0, 1100)
                    posY = random.randint(0, 360) + 80

                    # Crea el triangulo
                    triangulo = Triangulo(ladoB, ladoA, posX, posY)
                    triangulo.ingresarHipotenusa(hipotenusa)

                    # Genera una hipotenusa aleatoria para el proximo triangulo
                    hipotenusa = hipotenusaAleatoria()

                    # Asigna la posicion del triangulo
                    triangulo.ingresarPosicionX(posX)
                    triangulo.ingresarPosicionY(posY)

                    triangulos.add(triangulo)

                    # Detecta si el triangulo dibujado ha colisionado con otros
                    for trianguloActual in triangulos:
                        sprite_collide = pygame.sprite.spritecollide(trianguloActual, triangulos, False)
                        if len(sprite_collide) > 1:
                            for sprite in sprite_collide:
                                colision = True
                    
                    if colision:
                        triangulos.remove(triangulo)
                        triangulo.kill()
                        cuadrados.add(Cuadrado(ladoB, ladoA, posX, posY, (255,0,0)))
                    else:
                        cuadrados.add(Cuadrado(ladoB, ladoA, posX, posY, (0,0,0)))

                    # Lados e hipotenusa del triangulo
                    numero = crearTextoNumerico(triangulo.obtenerLadoA(), posX - 12, triangulo.ladoA * 5 + posY)
                    numeros.add(numero)

                    numero = crearTextoNumerico(round(triangulo.obtenerLadoB(),2), triangulo.ladoB * 5 + posX - 12, posY + triangulo.ladoA * 10 + 12)
                    numeros.add(numero)

                    numero = crearTextoNumerico(triangulo.obtenerHipotenusa(), triangulo.ladoB * 5 + posX + 10, posY + triangulo.ladoA * 5 - 5)
                    numeros.add(numero)

                    mostrar_error = False
                except:
                    mostrar_error = True

                # Si el usuario presiona enter entonces borra el contenido del input
                textinput.value = ''
            
    # Muestra el titulo del juego
    tituloTexto = titulo.render("Juego de la hipotenusa", True, blanco)
    pantalla.blit(tituloTexto, (400, 20))

    # Muestra la hipotenusa
    hipotenusa_texto = texto.render(f'Hipotenusa: {hipotenusa}', True, blanco)
    pantalla.blit(hipotenusa_texto, (10, 620))

    # Pide un lado del triangulo rectangulo
    hipotenusa_texto = texto.render('Lado A: ', True, blanco)
    pantalla.blit(hipotenusa_texto, (10, 650))

    # Muestra error si es necesario
    if mostrar_error:
        error_texto = texto.render(f'Error: el cateto debe ser mayor que 0 y menor que la longitud de la hipotenusa', True, (255, 0, 0))
        pantalla.blit(error_texto, (10, 680))

    # Muestra error de colision si es necesario (debug)
    if colision:
        colision_texto = texto.render(f'Colision', True, (255, 0, 0))
        pantalla.blit(colision_texto, (500, 620))
        colision = False

    # Pantalla de dibujo
    pygame.draw.rect(pantalla, blanco, pygame.Rect(0, 80, PANTALLA_ANCHO, PANTALLA_ALTO - 200))

    # Dibuja todos los triangulos creados hasta el momento
    for entity in triangulos:
        entity.draw(pantalla)

    # Dibuja todos los numeros creados hasta el momento
    for n in numeros:
        pantalla.blit(n.surf, n.rect)

    # Dibuja todos los cuadrados creados hasta el momento
    for c in cuadrados:
        c.draw(pantalla)

    # Renderiza la pantalla
    pygame.display.flip()
    clock.tick(FRAME)