import pygame, sys, spritesheetmatrix
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
HEIGHT = 400
WIDTH = 300
OFFSET_X = 10
OFFSET_Y = 10
SPRITE_ROWS = 3
SPRITE_COLS = 4

fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
ss = spritesheetmatrix.spritesheetmatrix('images/F_07.png', SPRITE_ROWS, SPRITE_COLS, WHITE)

personX = OFFSET_X
personY = OFFSET_Y
direction = 'right'
imgCount = 0
fpsCount = 1
sprite_width = ss.get_sprite_width()
sprite_height = ss.get_sprite_height()
num_sprites = ss.get_num_sprites()
scale_factor = int(min(WIDTH, HEIGHT) / 4)

while True:
    DISPLAYSURF.fill(WHITE)
    imgCount = imgCount + 1

    if direction == 'right':
        images = ss.get_right_sprites()
        img_len = len(images)
        personX += 5
        if personX > WIDTH - sprite_width - OFFSET_X - 55:
            direction = 'down'
    elif direction == 'down':
        images = ss.get_forward_sprites()
        img_len = len(images)
        personY += 5
        if personY > HEIGHT - sprite_height - OFFSET_Y - 55:
            direction = 'left'
    elif direction == 'left':
        images = ss.get_left_sprites()
        img_len = len(images)
        personX -= 5
        if personX < OFFSET_X:
            direction = 'up'
    elif direction == 'up':
        images = ss.get_backward_sprites()
        img_len = len(images)
        personY -= 5
        if personY < OFFSET_Y:
            direction = 'right'

    imgCount = imgCount % img_len
    personImg = images[imgCount]
    personImg = pygame.transform.scale(personImg, (scale_factor, scale_factor))
    fpsCount = (fpsCount + 1) % FPS

    DISPLAYSURF.blit(personImg, (personX, personY))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()