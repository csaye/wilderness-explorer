### imports ###

import pygame, sys

### globals ###

# screen
grid = 16
screen_x = 32; screen_y = 32

# game
update = 5

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

### screen ###

# initialize screen
screen_size = (screen_x * grid, screen_y * grid)
screen = pygame.display.set_mode(screen_size)

# set caption
pygame.display.set_caption('Wilderness Explorer')

### board ###

# draw board
def draw_board():
    # clear screen
    screen.fill(black)
    for y in range(0, screen_y):
        for x in range(0, screen_x):
            # get color from tile
            tile = board[x][y]
            if tile == '': continue
            elif tile == 'g': color = green
            # draw rect
            rect = ((x * grid, y * grid), (grid, grid))
            pygame.draw.rect(screen, color, rect)
    # update display
    pygame.display.update()

# initialize board
board = []
for y in range(0, screen_y):
    row = []
    for x in range(0, screen_x):
        row.append('g')
    board.append(row)

### main ###

clock = pygame.time.Clock()
frame = 0

# before first frame
draw_board()

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

    # update
    if frame % update == 0:

        # draw board
        draw_board()
    
