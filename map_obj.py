import pygame

class map_obj():
    def __init__(self, name, image_path, description, center, lat_long_base, lat_long_extremes):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.description = description
        self.center = center
        self.lat_long_base = lat_long_base
        self.lat_long_extremes = lat_long_extremes
