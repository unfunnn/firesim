import random
import time
import pygame
import math

height = 100
width = 100

scale_factor = 8  # fire size * scale factor = window size
intensity = 0.5  # lower numbers = higher fire (preferably 0-1)
temperature = 37  # range 0-len(colour) for the temperature of the fire
# lower temperatures work better with lower intensities
wind = 0  # negative bias is to the right and positive to the left
follow_mouse = False  # turns normal fire off and makes a point of fire follow the mouse

pixel_size = 1  # is only used for scaling, don't change
fire_pixels = []

colour = [
    "070707",
    "1F0707",
    "2F0F07",
    "470F07",
    "571707",
    "671F07",
    "771F07",
    "8F2707",
    "9F2F07",
    "AF3F07",
    "BF4707",
    "C74707",
    "DF4F07",
    "DF5707",
    "DF5707",
    "D75F07",
    "D75F07",
    "D7670F",
    "CF6F0F",
    "CF770F",
    "CF7F0F",
    "CF8717",
    "C78717",
    "C78F17",
    "C7971F",
    "BF9F1F",
    "BF9F1F",
    "BFA727",
    "BFA727",
    "BFAF2F",
    "B7AF2F",
    "B7B72F",
    "B7B737",
    "CFCF6F",
    "DFDF9F",
    "EFEFC7",
    "FFFFFF"
]
colour.reverse()
temperature = abs(temperature - len(colour))


def render():
    for y in range(height):
        for x in range(width):
            colour_index = math.ceil(fire_pixels[x][y])
            try:
                hex_colour = colour[colour_index]
            except:
                hex_colour = colour[len(colour) - 1]
            rbg_colour = tuple(int(hex_colour[i:i + 2], 16) for i in (0, 2, 4))  # Hex code to RBG
            # pygame.draw.circle(display_screen, rbg_colour, (x*scale_factor, y*scale_factor), pixel_size*scale_factor)
            pygame.draw.rect(display_screen, rbg_colour,
                             (x * scale_factor, y * scale_factor, pixel_size * scale_factxor, pixel_size * scale_factor))


def setup():
    for x in range(height):
        col = []
        for y in range(width+1):
            col.append(len(colour) - 1)
        fire_pixels.append(col)


def diffuse():
    for x in range(width):
        for y in range(height):
            random_variation_y = random.randint(0, 1)
            random_variation_x = random.randint(wind - 1, wind + 1)
            try:
                fire_pixels[x][y] = fire_pixels[x + random_variation_x][y + random_variation_y] + random.uniform(
                    intensity - 1, intensity + 1)
            except:
                fire_pixels[x][y] = fire_pixels[x][y + 1] + random.uniform(intensity-1, intensity+1)
            if y == 99 and follow_mouse is False:
                fire_pixels[x][y] = temperature



background_colour = 0, 0, 0
screen = pygame.display.set_mode((width, height))
display_screen = pygame.display.set_mode((width * scale_factor, height * scale_factor))
pygame.display.set_caption('firesim')
running = True
setup()
while running:
    pygame.display.flip()
    diffuse()
    render()
    if follow_mouse:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        fire_pixels[int(mouse_x / scale_factor)][int(mouse_y / (scale_factor))] = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scaled_win = pygame.transform.smoothscale(screen, display_screen.get_size())
    display_screen.blit(scaled_win, (0, 0))
    time.sleep(1 / 60)
