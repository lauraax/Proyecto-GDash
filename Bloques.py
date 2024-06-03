import pygame
from util import *

#clase para los bloques de los mapas
class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, imagen) :
        super().__init__()
        self.image = load_images(imagen, (width, height))
        self.rect = self.image.get_rect(topleft = pos) 