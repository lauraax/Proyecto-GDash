import pygame
from util import *
vec=pygame.math.Vector2

#clase para los bloques de los mapas
class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, imagen) :
        super().__init__()
        self.image = load_images(imagen, (width, height))
        self.rect = self.image.get_rect(topleft = pos) 
        self.direction = vec(0,0)
        self.gravity = 0.8
        self.pos = vec(pos)
        self.initial_jump = -11
        self.speed = 5
        self.piso =True
    def gravitacion(self):
        self.direction.y += self.gravity
        self.pos.y += self.direction.y
        self.rect.y = self.pos.y
        
    def update(self):
        self.direction.x = self.speed
        keys= pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.piso:
            self.direction.y = self.initial_jump
            self.piso = False
            
