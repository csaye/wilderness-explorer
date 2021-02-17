### imports ###

import pygame, sys

### screen ###

grid = 16
screen_x = 32; screen_y = 32

# initialize screen
screen_size = (screen_x * grid, screen_y * grid)
screen = pygame.display.set_mode(screen_size)

# set caption
pygame.display.set_caption('Wilderness Explorer')

