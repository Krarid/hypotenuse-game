import pygame
import random

class Triangulo(pygame.sprite.Sprite):

    def __init__(self, ladoB, ladoA):
        super(Triangulo, self).__init__()
        self.hipotenusa = 0
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.surf = pygame.Surface((self.ladoB, self.ladoA))
        self.rect = self.surf.get_rect()

    def ingresarLadoA(self, ladoA):
        self.ladoA = ladoA

    def ingresarHipotenusa(self, hipotenusa):
        self.hipotenusa = hipotenusa

    def ingresarPosicionX(self, posX):
        self.posX = posX

    def ingresarPosicionY(self, posY):
        self.posY = posY

    def obtenerHipotenusa(self):
        return self.hipotenusa
    
    def obtenerLadoA(self):
        return self.ladoA
    
    def obtenerLadoB(self):
        return self.ladoB

    def draw(self, pantalla):
        pygame.draw.polygon(pantalla, (0, 0, 255), 
        [(self.posX, self.posY), # 
        (self.posX, self.ladoA * 10 + self.posY), 
        (self.posX + self.ladoB * 10, self.ladoA * 10 + self.posY)], 0)
    
#triangulo = Triangulo()

#triangulo.hipotenusaAleatoria()
#print("Hipotenusa: ", triangulo.obtenerHipotenusa())

#triangulo.solicitarLadoA()
#triangulo.calcularCateto()
#print("Lado B: ", triangulo.obtenerLadoB())