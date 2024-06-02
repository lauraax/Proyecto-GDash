import pygame, sys 
from pygame.locals import *
from settings import *
from bloques import *
#Clase del juego general
class Game:
    def __init__(self, ruta_mapa):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Las flipantes carreras del cubo saltarín")
        #self.block = Bloque((0,0),50,50,'imagenes/bloque.jpg')
        self.blocks= pygame.sprite.Group()
        self.mapa = self.read_file(ruta_mapa)
    
    #Función para los eventos del juego
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    #Función para dibujar la rejilla para guiarse en la creacion del mapa
    def draw_grid(self):
        for y in range(50, WIDTH, 50):
            pygame.draw.line(self.screen,RED,(y,0),(y,HEIGHT)) #líneas verticales 

        for x in range(50, HEIGHT, 50):
            pygame.draw.line(self.screen,GREEN, (0,x), (WIDTH,x))#líneas horizontales
    
    #Función para leer el mapa a partir de un txt
    def read_file(self, ruta):
        file = ''
        with open(ruta, 'r') as f: #lee el archivo txt y lo convierte un string
            file = f.read().splitlines() #el splitlines quita los saltos de linea
        return file
    
    def load_map(self):
        for row in self.mapa:
            for char in row:
                if char == '0':
                    self.blocks.add(Bloque((0,0),50,50,'imagenes/bloque.jpg'))
    def draw(self):#funcion para dibujar los sprites
        self.blocks.draw(self.screen)
    #Función para correr el juego
    def running(self):
        while True:
            self.clock.tick(FPS)
            pygame.display.update()
            self.events()
            self.screen.blit(self.block.image, self.block.rect)#esto es solo para ver cómo se ve el cuadrito xd
            self.draw_grid()

game=Game()

game.running()