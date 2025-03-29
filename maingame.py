import pygame
from enum import Enum

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

tile_s = 25

vis_world_w = 25
vis_world_h = 25

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


class Direction(Enum):
    Up = 0
    Down = 180
    Left = 90
    Right = 270


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


class Tank:
    def __init__(self, tile, x, y):
        self.tile = pygame.image.load(f'tiles/{tile}')
        self.w = tile_s
        self.h = tile_s
        self.s = (self.w, self.h)

        self.tile = pygame.transform.scale(self.tile, self.s)
        self.rect = self.tile.get_rect()
        self.x = tile_s * x + tile_s // 2
        self.y = tile_s * y + tile_s // 2

        self.dir = Direction.Right
        self.speed = 2
        self.on_move = False

    def render(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        tile = pygame.transform.rotate(
            self.tile,
            self.dir.value
        )
        screen.blit(tile, self.rect)

    def move(self):
        if not self.on_move:
            return
        if self.dir == Direction.Up:
            self.y -= self.speed
        if self.dir == Direction.Down:
            self.y += self.speed
        if self.dir == Direction.Left:
            self.x -= self.speed
        if self.dir == Direction.Right:
            self.x += self.speed


arrows = [
    pygame.K_UP, pygame.K_DOWN,
    pygame.K_LEFT, pygame.K_RIGHT
]


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


tank = Tank('tank.png', 3, 3)
mank = Tank('mank.png', 21, 21)

load_world()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(black)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            tank.dir = Direction.Up
        if event.key == pygame.K_DOWN:
            tank.dir = Direction.Down
        if event.key == pygame.K_LEFT:
            tank.dir = Direction.Left
        if event.key == pygame.K_RIGHT:
            tank.dir = Direction.Right

    if event.type == pygame.KEYDOWN and event.key in arrows:
        tank.on_move = True

    if event.type == pygame.KEYUP and event.key in arrows:
        tank.on_move = False

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

    tank.move()
    tank.render(screen)

    mank.move()
    mank.render(screen)

    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()