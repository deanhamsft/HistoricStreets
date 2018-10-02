import pygame
import os
import map_obj

center_offset = [0,0]
coordinates = [0,0] 
mouse_pos = [0,0]
image_dimensions = [0,0]
held = False

image1 = pygame.image.load('photos/42961479_344104342993622_231747858242469888_n.jpg')

picture_1885_locations = [[image1, -370, -940]]
picture_1917_locations = [0,0]
picture_1954_locations = [0,0]
picture_1964_locations = [0,0]

map_1885 = map_obj.map_obj('1885', 'resources/maps/vernal_1885.jpg',  'Ashley Valley 1885', [-370, -940])
map_1917 = map_obj.map_obj('1917', 'resources/maps/vernal_1917.jpg',  'Ashley Valley 1917', [-370, -940])
map_1954 = map_obj.map_obj('1954', 'resources/maps/vernal_1954.jpg',  'Ashley Valley 1954', [-370, -940])
map_1964 = map_obj.map_obj('1964', 'resources/maps/vernal_1964.jpg',  'Ashley Valley 1964', [-370, -940])

def holding():
    global coordinates, mouse_pos
    temp_work = pygame.mouse.get_pos()
    curr_x = temp_work[0] - mouse_pos[0]
    curr_y = temp_work[1] - mouse_pos[1]

    min_x = 0 - image_dimensions[0] - 1440
    min_y = 0 - image_dimensions[1] - 900

    max_x = 0 - image_dimensions[0] + 1440
    max_y = 0 - image_dimensions[1] + 900

    if  coordinates[0] > min_x and coordinates[0] < 0:
        coordinates[0] += curr_x
    elif curr_x > -1 and coordinates[0] > min_x:
        coordinates[0] -= curr_x
    if coordinates[1] > min_y and coordinates[1] < 0:
        coordinates[1] += curr_y
    elif curr_y > -1 and coordinates[1] > min_y:
        coordinates[1] -= curr_y
    mouse_pos = pygame.mouse.get_pos()
    
def game_event_loop(screen):
    global held, coordinates, mouse_pos
    if held:
        holding()
    screen.fill((0,0,255))
    screen.blit(map_1964.image, coordinates)

    for picture in picture_1885_locations:
        screen.blit(picture[0], (picture[1], picture[2]))
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

    screen = pygame.display.set_mode((1440, 900), 0, 32)
    image_dimensions = map_1885.image.get_rect().size
    center_offset[0] = image_dimensions[0] - (1440 - (map_1885.center[0]))
    center_offset[1] = image_dimensions[1] - (900 - (map_1885.center[1]))
    coordinates = [-center_offset[0], -center_offset[1]]
    
    while 1:
        game_event_loop(screen)
        pygame.display.update()