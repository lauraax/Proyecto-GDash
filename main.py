import pygame, sys 
from pygame.locals import *
from settings import *
from Bloques import *
from Jug import *
#Clase del juego general
class Game:
    def __init__(self, ruta_mapa):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Las flipantes carreras del cubo saltarín")
        self.blocks = pygame.sprite.Group()
        self.pla = pygame.sprite.GroupSingle()
        self.mapa = self.read_file(ruta_mapa)
        self.load_map()
    #Función para los eventos del juego
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    #Función para dibujar la rejilla para guiarse en la creacion del mapa
    def draw_grid(self):
        for y in range(34, WIDTH, 34):
            pygame.draw.line(self.screen,RED,(y,0),(y,HEIGHT)) #líneas verticales 

        for x in range(34, HEIGHT, 34):
            pygame.draw.line(self.screen,GREEN, (0,x), (WIDTH,x))#líneas horizontales
    
    #Función para leer el mapa a partir de un txt
    def read_file(self, ruta):
        file = ''
        with open(ruta, 'r') as f: #lee el archivo txt y lo convierte un string
            file = f.read().splitlines() #el splitlines quita los saltos de linea
        return file
    #Funcion para hacer el mapa
    def load_map(self):

        for i,row in enumerate(self.mapa):
            for j,char in enumerate(row):
                if char == 'b':
                    self.blocks.add(Bloque((34*j,34*i),34,34,'imagenes/bloque.jpg'))
                elif char == 'p':
                    self.pla.add(Jugador((34*j,34*i),34,34,'imagenes/cuadrao.jpg'))
    def coli_horizontal(self): #Coliciones con los bloques pero solo horizontalmente
        self.pla.sprite.pos.x += self.pla.sprite.direction.x
        self.pla.sprite.rect.x = self.pla.sprite.pos.x
        for block in self.blocks:
            if block.rect.colliderect(self.pla.sprite.rect):
                self.pla.sprite.rect.right = block.rect.left
                self.pla.sprite.pos.x = self.pla.sprite.rect.x  
    def coli_vertical(self):
        self.pla.sprite.gravitacion()#Gravedad dah
        for block in self.blocks:
            if block.rect.colliderect(self.pla.sprite.rect):
                self.pla.sprite.piso=True  
                if self.pla.sprite.direction.y<0:
                    self.pla.sprite.rect.top = block.rect.bottom
                    self.pla.sprite.pos.y = self.pla.sprite.rect.y 
                    self.pla.sprite.direction.y=0   
                if self.pla.sprite.direction.y>0:
                    self.pla.sprite.rect.bottom = block.rect.top
                    self.pla.sprite.pos.y = self.pla.sprite.rect.y  
                    self.pla.sprite.direction.y=0  
                            
    def update(self):
        self.coli_vertical()
        self.coli_horizontal()
        
        self.pla.update()#Aqui esta todo el movimiento del cubo
    def draw(self,surface):#funcion para dibujar los sprites
        self.blocks.draw(surface)
        self.pla.draw(surface)
        
    #Función para correr el juego
    def running(self):
        while True:
            self.clock.tick(FPS)
            pygame.display.update()
            self.screen.fill('lightblue')
            self.events()
            self.update()
            self.draw(self.screen)
            # self.blocks.draw(self.screen)
            # for block in self.blocks:
                # self.screen.blit(block.image, block.rect)#esto es solo para ver cómo se ve el cuadrito xd
            # self.draw_grid()

game=Game('mapa.txt')

game.running()