import pygame
import sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Newgame')

WHITE = (0, 0, 0)
catImg = pygame.image.load('cat.png')
catx = 100
caty = 100
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(catImg, (catx, caty))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                caty = caty - 10
                if 0 > caty:
                    caty = 0
            if event.key == K_DOWN:
                caty = caty + 10
                if 224 < caty:
                    caty = 224
            if event.key == K_LEFT:
                catx = catx - 10
                if 0 > catx:
                    catx = 0
            if event.key == K_RIGHT:
                catx = catx + 10
                if 261 < catx:
                    catx = 261
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
