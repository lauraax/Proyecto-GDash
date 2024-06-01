import pygame, sys 
from pygame.locals import *
from settings import *
from bloques import *
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Las flipantes carreras del cubo saltarín")
        self.block = Bloque((0,0),50,50,'imagenes/bloque.jpg')
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def draw_grid(self):
        
        for y in range(50, WIDTH, 50):
            pygame.draw.line(self.screen,RED,(y,0),(y,HEIGHT))

        for x in range(50, HEIGHT, 50):
            pygame.draw.line(self.screen,GREEN, (0,x), (WIDTH,x))

    def running(self):
        while True:
            self.clock.tick(FPS)
            pygame.display.update()
            self.events()
            self.screen.blit(self.block.image, self.block.rect)
            self.draw_grid()

game=Game()

game.running()