import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (25, 25, 25)
ligray = (50, 50, 50)

scr_w, scr_h = 800, 450
tile_s = scr_h // 10
screeny = pygame.display.set_mode((scr_w, scr_h))

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

world = [
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [ston, ston, ston, watr, watr, watr, ston, ston, ston, ston, ston, gron, gron, gron, gron, gron, gras, gras],
    [ston, gras, gras, watr, watr, watr, gras, gras, ston, ston, ston, ston, gron, gron, gron, gras, gras, watr],
    [ston, gras, gras, watr, watr, watr, gras, gras, gras, ston, ston, gron, gron, gron, gras, gras, watr, watr],
    [gron, gron, ston, ston, ston, ston, ston, gras, gras, gron, gron, gron, gron, gras, gras, watr, watr, watr],
    [gron, gron, gron, gron, gron, gron, gron, gron, gron, gron, gron, gron, gras, gras, watr, watr, watr, watr],
    [ston, gron, gron, gron, gron, gron, gron, gron, gron, gron, gron, gras, gras, watr, watr, watr, watr, watr],
    [ston, gras, ston, ston, ston, ston, ston, gras, ston, ston, ston, ston, gras, gras, watr, watr, watr, watr],
    [ston, gras, gras, watr, watr, watr, gras, ston, ston, lava, lava, ston, ston, gras, gras, watr, watr, watr],
    [ston, gras, gras, watr, watr, watr, ston, ston, lava, lava, lava, lava, ston, ston, gras, gras, watr, watr],
    [ston, ston, ston, watr, watr, watr, ston, lava, lava, lava, lava, lava, lava, ston, gras, gras, gras, watr],
]

world_w = 25
world_h = 25

world = [[None for j in range(world_w)] for i in range(world_h)]

vis_world_w = 10
vis_world_h = 10

x_shift = 0
y_shift = 0


class Button:
    def __init__(self, tile, text):
        font = pygame.font.Font(None, 30)

        self.tile = tile
        self.tile_rect = self.tile.get_rect()

        self.text = font.render(text, True, white)
        self.text_rect: pygame.Rect = self.text.get_rect()

        self.w = self.text_rect.width + tile_s + 50
        self.h = max(tile_s, self.text_rect.height) + 20
        self.rect = pygame.Rect(0, 0, self.w, self.h)

        self.is_hov = False
        self.is_act = False

    def check_collision(self, pos):
        self.is_hov = False
        if self.rect.collidepoint(pos):
            self.is_hov = True
        return self.is_hov

    def render(self, screen):
        if self.is_hov:
            pygame.draw.rect(screen, gray, self.rect)
        if self.is_act:
            pygame.draw.rect(screen, ligray, self.rect)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.tile, self.tile_rect)


gras_btn = Button(gras, 'Gras')
gron_btn = Button(gron, 'Gron')
lava_btn = Button(lava, 'Lava')
ston_btn = Button(ston, 'Ston')
watr_btn = Button(watr, 'Watr')

gras_btn.rect.left = tile_s * 10 + 25
gras_btn.rect.top = tile_s // 2
gras_btn.tile_rect.left = gras_btn.rect.left + 20
gras_btn.tile_rect.centery = gras_btn.rect.centery
gras_btn.text_rect.left = gras_btn.tile_rect.right + 10
gras_btn.text_rect.centery = gras_btn.tile_rect.centery

gron_btn.rect.left = tile_s * 10 + 25
gron_btn.rect.top = gras_btn.rect.bottom + 10
gron_btn.tile_rect.left = gron_btn.rect.left + 20
gron_btn.tile_rect.centery = gron_btn.rect.centery
gron_btn.text_rect.left = gron_btn.tile_rect.right + 10
gron_btn.text_rect.centery = gron_btn.tile_rect.centery

lava_btn.rect.left = tile_s * 10 + 25
lava_btn.rect.top = gron_btn.rect.bottom + 10
lava_btn.tile_rect.left = lava_btn.rect.left + 20
lava_btn.tile_rect.centery = lava_btn.rect.centery
lava_btn.text_rect.left = lava_btn.tile_rect.right + 10
lava_btn.text_rect.centery = lava_btn.tile_rect.centery

ston_btn.rect.left = tile_s * 10 + 25
ston_btn.rect.top = lava_btn.rect.bottom + 10
ston_btn.tile_rect.left = ston_btn.rect.left + 20
ston_btn.tile_rect.centery = ston_btn.rect.centery
ston_btn.text_rect.left = ston_btn.tile_rect.right + 10
ston_btn.text_rect.centery = ston_btn.tile_rect.centery

watr_btn.rect.left = tile_s * 10 + 25
watr_btn.rect.top = ston_btn.rect.bottom + 10
watr_btn.tile_rect.left = watr_btn.rect.left + 20
watr_btn.tile_rect.centery = watr_btn.rect.centery
watr_btn.text_rect.left = watr_btn.tile_rect.right + 10
watr_btn.text_rect.centery = watr_btn.tile_rect.centery

tiles_btns = [gras_btn, gron_btn, lava_btn, ston_btn, watr_btn]
selected_tile = None

tiles_names = {
    gras: 'gras',
    gron: 'gron',
    lava: 'lava',
    ston: 'ston',
    watr: 'watr'
}

name_to_tile = {
    'gras': gras,
    'gron': gron,
    'lava': lava,
    'ston': ston,
    'watr': watr
}


def save_world(world):
    file = open('map.txt', 'w', encoding='utf-8')

    world_record = ' '

    world_record += str(len(world[0]))
    world_record += ' '

    world_record += str(len(world))
    world_record += '\n'

    file.write(world_record)

    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] is None:
                continue

            file.write(f'{i} {j} {tiles_names[world[i][j]]}\n')

            print("saved")

    file.close()


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


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            w = tile_s * vis_world_w
            h = tile_s * vis_world_h
            if x < w and y < h:
                tile_x = x // tile_s + x_shift
                tile_y = y // tile_s + y_shift
                world[tile_y][tile_x] = selected_tile

            any_btn_pressed = False
            for btn in tiles_btns:
                if btn.check_collision(event.pos):
                    any_btn_pressed = True
                    break
            if not any_btn_pressed:
                continue

            for btn in tiles_btns:
                if btn.check_collision(event.pos):
                    btn.is_act = not btn.is_act
                else:
                    btn.is_act = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_shift > 0:
                y_shift -= 1
            if event.key == pygame.K_DOWN and y_shift < world_h - vis_world_h:
                y_shift += 1
            if event.key == pygame.K_LEFT and x_shift > 0:
                x_shift -= 1
            if event.key == pygame.K_RIGHT and x_shift < world_w - vis_world_w:
                x_shift += 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            save_world(world)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            load_world()

    mouse_pos = pygame.mouse.get_pos()

    gras_btn.check_collision(mouse_pos)
    gron_btn.check_collision(mouse_pos)
    lava_btn.check_collision(mouse_pos)
    ston_btn.check_collision(mouse_pos)
    watr_btn.check_collision(mouse_pos)

    selected_tile = None
    for btn in tiles_btns:
        if btn.is_act:
            selected_tile = btn.tile

    screeny.fill(black)

    for i in range(vis_world_h):
        for j in range(vis_world_w):
            x = j * tile_s
            y = i * tile_s

            cell = world[i + y_shift][j + x_shift]
            if cell is not None:
                screeny.blit(cell, (x, y))
            else:
                cell_w = tile_s
                cell_h = tile_s
                pygame.draw.rect(screeny, white, (x, y, cell_w, cell_h), 1)

    gras_btn.render(screeny)
    gron_btn.render(screeny)
    lava_btn.render(screeny)
    ston_btn.render(screeny)
    watr_btn.render(screeny)

    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()
