import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (25, 25, 25)
ligray = (50, 50, 50)

tile_s = 50

vis_world_w = 16
vis_world_h = 9

scr_w = tile_s * vis_world_w
scr_h = tile_s * vis_world_h
screen = pygame.display.set_mode((scr_w, scr_h))

gras = pygame.image.load('tiles/grass.jpg')
gron = pygame.image.load('tiles/ground.jpg')
ston = pygame.image.load('tiles/stone.jpg')
watr = pygame.image.load('tiles/water.jpg')
lava = pygame.image.load('tiles/lava.jpg')

gras = pygame.transform.scale(gras, (tile_s, tile_s))
gron = pygame.transform.scale(gron, (tile_s, tile_s))
ston = pygame.transform.scale(ston, (tile_s, tile_s))
watr = pygame.transform.scale(watr, (tile_s, tile_s))
lava = pygame.transform.scale(lava, (tile_s, tile_s))

world_h = 25
world_w = 25

world = []
for i in range(world_h):
    row = []
    for j in range(world_w):
        row.append(None)
    world.append(row)

x_shift = 0
y_shift = 0

name_to_tile = {
    'gras': gras,
    'gron': gron,
    'lava': lava,
    'ston': ston,
    'watr': watr
}


def load_world():
    global world, world_h, world_w
    file = open('map.txt', 'r')

    world_info = next(file)
    world_s = world_info.strip().split()
    world_w = int(world_s[0])
    world_h = int(world_s[1])

    world = []
    for i in range(world_h):
        row = []
        for j in range(world_w):
            row.append(None)
        world.append(row)

    for line in file:
        line = line.strip()
        i, j, tile = line.split()

        i = int(i)
        j = int(j)

        tile = name_to_tile[tile]

        world[i][j] = tile

    file.close()


load_world()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and y_shift > 0:
            y_shift -= 1
        if event.key == pygame.K_DOWN and y_shift < world_h - vis_world_h:
            y_shift += 1
        if event.key == pygame.K_LEFT and x_shift > 0:
            x_shift -= 1
        if event.key == pygame.K_RIGHT and x_shift < world_w - vis_world_w:
            x_shift += 1

    screen.fill(black)

    for i in range(vis_world_h):
        for j in range(vis_world_w):
            x = j * tile_s
            y = i * tile_s

            cell = world[i + y_shift][j + x_shift]
            if cell is not None:
                screen.blit(cell, (x, y))
            else:
                cell_w = tile_s
                cell_h = tile_s
                pygame.draw.rect(screen, white, (x, y, cell_w, cell_h), 1)

    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()