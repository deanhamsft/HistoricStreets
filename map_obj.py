import pygame

class map_obj():
    def __init__(self, name, image_path, description, center):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.description = description
        self.center = center
