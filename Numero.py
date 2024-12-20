import pygame

class Numero(pygame.sprite.Sprite):

    def __init__(self, surf, posX, posY):
        super(Numero, self).__init__()
        self.posX = posX
        self.posY = posY
        self.surf = surf
        self.rect = self.surf.get_rect(center = (posX, posY))