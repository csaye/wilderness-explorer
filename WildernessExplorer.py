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

### main ###

clock = pygame.time.Clock()
frame = 0

# game loop
while True:

    # tick
    clock.tick(60)
    frame += 1

    # events
    for event in pygame.event.get():

        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
