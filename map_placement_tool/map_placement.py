import pygame
import os
import importlib.util
spec = importlib.util.spec_from_file_location("map_obj", "C:/Users/deanha/OneDrive/PythonProjects/Kerry_Boren_project/map_obj.py")
map_obj = importlib.util.module_from_spec(spec)
spec.loader.exec_module(map_obj)
import tkinter as tk
from tkinter import filedialog

center_offset = [0,0]
coordinates = [0,0] 
mouse_pos = [0,0]
image_dimensions = [0,0]
held = False

def open_map():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    return map_obj.map_obj('new map', file_path, 'map area and year description', [0,0],[0,0],[0,0])

def holding(current_map):
    global coordinates, mouse_pos
    temp_work = pygame.mouse.get_pos()
    curr_x = temp_work[0] - mouse_pos[0]
    curr_y = temp_work[1] - mouse_pos[1]

    min_x = 0 - current_map.image.get_rect().size[0]
    min_y = 0 - current_map.image.get_rect().size[1]
    print('{} | {}'.format(min_x, min_y))
    if  coordinates[0] > min_x and coordinates[0] < 0:
        coordinates[0] += curr_x
    elif curr_x > -1 and coordinates[0] > min_x:
        coordinates[0] -= curr_x
    if coordinates[1] > min_y and coordinates[1] < 0:
        coordinates[1] += curr_y
    elif curr_y > -1 and coordinates[1] > min_y:
        coordinates[1] -= curr_y
    mouse_pos = pygame.mouse.get_pos()
    
def game_event_loop(screen, current_map):
    global held, coordinates, mouse_pos
    if held:
        holding(current_map)
    screen.fill((0,0,255))
    screen.blit(current_map.image, coordinates)

    pygame.display.flip()

    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str(coordinates), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            held = True 
        elif event.type == pygame.MOUSEBUTTONUP:
            held = False
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    current_map = open_map()
    screen = pygame.display.set_mode((1440, 900), 0, 32)
    image_dimensions = current_map.image.get_rect().size
    center_offset[0] = current_map.center[0]
    center_offset[1] = current_map.center[1]
    coordinates = [-center_offset[0], -center_offset[1]]
    
    while 1:
        game_event_loop(screen, current_map)
        pygame.display.update()