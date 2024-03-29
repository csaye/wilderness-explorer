### imports ###

import pygame, sys

### globals ###

# screen
grid = 16
screen_x = 32; screen_y = 32

# game
update = 5
water = 30

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 191, 31)
blue = (0, 0, 255)
brown = (127, 63, 63)

### maps ###

def import_map(name):
    map_lines = open('maps/' + name + '.txt').read().splitlines()
    map_board = []
    for y in range(0, screen_y):
        row = []
        for x in range(0, screen_x):
            ch = map_lines[x][y]
            row.append(ch)
        map_board.append(row)
    return map_board

# maps
map00 = import_map('00')

### screen ###

# updates caption
def update_caption():
    caption = 'Water: ' + str(water)
    pygame.display.set_caption(caption)

# initialize screen
screen_size = (screen_x * grid, screen_y * grid)
screen = pygame.display.set_mode(screen_size)
update_caption()

### boards ###

# initialize sub board
sub_board = map00

# initialize board
board = []
for y in range(0, screen_y):
    row = []
    for x in range(0, screen_x):
        row.append('')
    board.append(row)

# draws all boards
def draw():
    # clear screen
    screen.fill(black)
    for y in range(0, screen_y):
        for x in range(0, screen_x):
            # if tile empty, get sub tile
            tile = board[x][y]
            if tile == '':
                # if sub tile empty, continue
                tile = sub_board[x][y]
                if tile == '': continue
            # get color from tile
            if tile == 'g': color = green # grass
            elif tile == 'p': color = brown # player
            elif tile == 'w': color = blue # water
            # draw rect
            rect = ((x * grid, y * grid), (grid, grid))
            pygame.draw.rect(screen, color, rect)
    # update display
    pygame.display.update()

### player ###

# initialize player
player_x = 1; player_y = screen_y - 2
board[player_x][player_y] = 'p'
can_move = True

def move_dir(direction):
    if direction == 'u': move(player_x, player_y - 1)
    elif direction == 'r': move(player_x + 1, player_y)
    elif direction == 'd': move(player_x, player_y + 1)
    elif direction == 'l': move(player_x - 1, player_y)

def move(x, y):
    global player_x, player_y, can_move, water
    # return if cannot move
    if not can_move: return
    # return if out of bounds
    if x < 0: return
    elif x > screen_x - 1: return
    if y < 0: return
    elif y > screen_y - 1: return
    # update board and player coordinates
    board[player_x][player_y] = ''
    player_x = x; player_y = y
    board[player_x][player_y] = 'p'
    # update water
    if sub_board[player_x][player_y] == 'w':
        water = 30
    else:
        water -= 1
    # update can move
    can_move = False

### main ###

clock = pygame.time.Clock()
frame = 0

# before first frame
draw()

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

        # keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move_dir('u')
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_dir('l')
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move_dir('d')
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_dir('r')

    # update
    if frame % update == 0:

        # draw boards
        draw()

        # update caption
        update_caption()

        # reset player
        can_move = True
    
