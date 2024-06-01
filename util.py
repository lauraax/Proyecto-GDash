import pygame

def load_images(imagen, size = None):
    image = pygame.image.load(imagen)
    if size:
        image = pygame.transform.scale(image, size)
    return image