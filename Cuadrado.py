import pygame
import random

class Cuadrado(pygame.sprite.Sprite):

    def __init__(self, ladoB, ladoA, posX, posY, color):
        super(Cuadrado, self).__init__()
        self.hipotenusa = 0
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.posX = posX
        self.posY = posY
        self.color = color
        self.surf = pygame.Surface((self.ladoB * 10, self.ladoA * 10))
        self.rect = self.surf.get_rect(topleft = (posX, posY))

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, self.color, 
                         pygame.Rect(self.posX, self.posY, self.ladoB * 10, self.ladoA * 10), 2)