import pygame

#función para subir imagenes y ajustar el tamaño 
def load_images(imagen, size = None):
    image = pygame.image.load(imagen)
    if size:
        image = pygame.transform.scale(image, size)
    return image

file = ''
with open('mapa.txt', 'r') as f: #lee el archivo txt y lo convierte un string
    file = f.read().splitlines() #el splitlines quita los saltos de linea
print(file)