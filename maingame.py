import pygame
from enum import Enum

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

tile_s = 50
tank_s = tile_s * 2

vis_world_w = 16
vis_world_h = 9

scr_w = tile_s * vis_world_w
scr_h = tile_s * vis_world_h
screen = pygame.display.set_mode((scr_w, scr_h))

gras = pygame.image.load('tiles/grass.jpg')
ston = pygame.image.load('tiles/stone.jpg')
watr = pygame.image.load('tiles/water.jpg')

gras = pygame.transform.scale(gras, (tile_s, tile_s))
ston = pygame.transform.scale(ston, (tile_s, tile_s))
watr = pygame.transform.scale(watr, (tile_s, tile_s))

default_tile = gras


class Direction(Enum):
    Up = 90
    Down = 270
    Left = 180
    Right = 0


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
    'ston': ston,
    'watr': watr
}


class Tank:
    def __init__(self, tile, x, y):
        self.tile = pygame.image.load(f'tiles/{tile}')
        self.w = tank_s
        self.h = tank_s
        self.s = (self.w, self.h)

        self.tile = pygame.transform.scale(self.tile, self.s)
        self.rect = self.tile.get_rect()
        self.x = tile_s * x + tile_s // 2
        self.y = tile_s * y + tile_s // 2

        self.dir = Direction.Right
        self.speed = tile_s / 12
        self.on_move = False

    def update_rect(self):
        pass

    def render(self, screen):
        self.update_rect()
        tile = pygame.transform.rotate(
            self.tile,
            self.dir.value
        )
        screen.blit(tile, self.rect)

    def change_dir(self, direction: Direction):
        self.dir = dir

class PlayerTank(Tank):

    def update_rect(self):
        self.rect.centerx = round(self.x)
        self.rect.centery = round(self.y)

    def move(self):
        global world
        global x_shift, y_shift

        weight_horld = world_h * tile_s
        width_world = world_w * tile_s
        if not self.on_move:
            return

        if self.dir == Direction.Up:
            if self.y <= scr_h / 2 and y_shift - self.speed >= 0:
                y_shift -= self.speed
            else:
                self.y -= self.speed

        if self.dir == Direction.Down:
            if self.y >= scr_h / 2 and \
                y_shift + self.speed <= weight_horld - scr_h:

                y_shift += self.speed
            else:
                self.y += self.speed

        if self.dir == Direction.Left:
            if self.x <= scr_w / 2 and x_shift - self.speed >= 0:
                x_shift -= self.speed
            else:
                self.x -= self.speed

        if self.dir == Direction.Right:
            if self.x >= scr_w / 2 and \
                x_shift + self.speed <= width_world - scr_w:

                x_shift += self.speed
            else:
                self.x += self.speed

class EnemyMank(Tank):

    def update_rect(self):
        self.rect.centerx = round(self.x - x_shift)
        self.rect.centery = round(self.y - y_shift)

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


tank = PlayerTank('tank.png', 3, 3)
mank = EnemyMank('mank.png', 21, 21)

load_world()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(black)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            tank.change_dir(Direction.Up)
        if event.key == pygame.K_DOWN:
            tank.change_dir(Direction.Down)
        if event.key == pygame.K_LEFT:
            tank.change_dir(Direction.Left)
        if event.key == pygame.K_RIGHT:
            tank.change_dir(Direction.Right)

    if event.type == pygame.KEYDOWN and event.key in arrows:
        tank.on_move = True

    if event.type == pygame.KEYUP and event.key in arrows:
        tank.on_move = False

    for i in range(world_h):
        for j in range(world_w):
            x = round(j * tile_s - x_shift)
            y = round(i * tile_s - y_shift)

            screen.blit(default_tile, (x, y))

            cell = world[i][j]
            if cell is not None:
                screen.blit(cell, (x, y))

    tank.move()
    tank.render(screen)

    mank.move()
    mank.render(screen)

    pygame.time.delay(25)
    pygame.display.update()

pygame.quit()