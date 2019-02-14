import pygame
import sys
import time
from UserString import MutableString

pygame.init()

WHITE = (48, 48, 48)
manx = 0
many = 0  
pixelx = 60
pixely = 60
tilex = 10
tiley = 8
displayx = pixelx * tilex
displayy = pixely * tiley
iotcount = 0
DISPLAYSURF = None

iotwall = pygame.image.load('iot_wall.png')
iotmanU = pygame.image.load('iot_manU.png')
iotmanD = pygame.image.load('iot_manD.png')
iotmanL = pygame.image.load('iot_manL.png')
iotmanR = pygame.image.load('iot_manR.png')
iotman = pygame.image.load('iot_manL.png')
iotobj1 = pygame.image.load('iot_obj1.png')
iotobj2 = pygame.image.load('iot_obj2.png')
clear = pygame.image.load('iot_clear.png')

iotstage = [
    [
    MutableString("          "),
    MutableString("   ###    "),
    MutableString(" ###2##   "),
    MutableString(" #211 ### "),
    MutableString(" ###@112# "),
    MutableString("   ##2### "),
    MutableString("    ###   "),
    MutableString("          ")],
    [
    MutableString("   ###    "),
    MutableString("   #2#    "),
    MutableString("   # #### "),
    MutableString(" ###1 12# "),
    MutableString(" #2 1@### "),
    MutableString(" ####1#   "),
    MutableString("    #2#   "),
    MutableString("    ###   ")],
    [
    MutableString("##########"),
    MutableString("#2#   122#"),
    MutableString("#21 ###1##"),
    MutableString("#1#      #"),
    MutableString("#    @ #1#"),
    MutableString("##1### 12#"),
    MutableString("#221   #2#"),
    MutableString("##########")]
]

stagenum = 0
iotcaption = "Skokoban [Stage : %d][move : %d]" % (stagenum + 1, iotcount)
pygame.display.set_caption(iotcaption)
iotmap = []

def iotloadmap():
    global iotmap
    
    for istage in range(tiley):
        iotmap.append(iotstage[stagenum][istage][:])

def iotsetcaption(caption):
    pygame.display.set_caption(caption)

def iotdraw():
    global manx
    global many
    global stageend

    DISPLAYSURF.fill(WHITE)
    stageend = True

    for ix in range(tilex):
        for iy in range(tiley):
            if '#' == iotmap [iy][ix]:
                DISPLAYSURF.blit(iotwall, (ix * pixelx, iy * pixely))
            elif '@' == iotmap [iy][ix]:
                manx = ix
                many = iy
                DISPLAYSURF.blit(iotman, (ix * pixelx, iy * pixely))
            elif '1' == iotmap [iy][ix]:
                DISPLAYSURF.blit(iotobj1, (ix * pixelx, iy * pixely))
                if '2' != iotstage[stagenum][iy][ix]:
                    stageend = False
            elif '2' == iotmap [iy][ix]:
                DISPLAYSURF.blit(iotobj2, (ix * pixelx, iy * pixely))

def iotinit():
    global DISPLAYSURF

    iotloadmap()
    iotcaption = "Skokoban"
    pygame.display.set_caption(iotcaption)
    DISPLAYSURF = pygame.display.set_mode((displayx, displayy), 0, 32)

iotinit()

while True:

    iotdraw()

    pygame.display.update()

    if True == stageend:
        DISPLAYSURF.blit(clear, (120, 60))
        pygame.display.update()
        keyinput = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keyinput = True
                    break
            if True == keyinput:
                break
            time.sleep(0.1)
            continue
        stagenum = stagenum + 1
        iotmap = []
        for istage in range(tiley):
            iotmap.append(iotstage[stagenum][istage][:])
        iotcount = 0
        iotsetcaption("Skokoban [Stage : %d][move : %d]" % (stagenum + 1, iotcount))
        continue

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            tempx = manx
            tempy = many
            if event.key == pygame.K_UP:
                iotman = iotmanU
                many = many-1
            elif event.key == pygame.K_DOWN:
                iotman = iotmanD
                many = many+1
            elif event.key == pygame.K_LEFT:
                iotman = iotmanL
                manx = manx-1
            elif event.key == pygame.K_RIGHT:
                iotman = iotmanR
                manx = manx+1
            elif event.key == pygame.K_r:
                iotcount = 0
                iotsetcaption("Skokoban [Stage : %d][move : %d]" % (stagenum + 1, iotcount))
                iotmap = []
                for istage in range(tiley):
                    iotmap.append(iotstage[stagenum][istage][:])
                break
            else:
                continue

            if '#' != iotmap[many][manx]:
                if '1' == iotmap[many][manx]:
                    if ' ' == iotmap[2 * many - tempy][2 * manx - tempx]:
                        iotmap[2 * many - tempy][2 * manx - tempx] = '1'
                    elif '2' == iotmap[2 * many - tempy][2 * manx - tempx]:
                        iotmap[2 * many - tempy][2 * manx - tempx] = '1'
                    else:
                        manx = tempx
                        many = tempy
                        continue
                if '2' == iotstage[stagenum][tempy][tempx]:
                    iotmap[tempy][tempx] = '2'
                else:
                    iotmap[tempy][tempx] = ' '
                iotmap[many][manx] = '@'
                iotcount = iotcount + 1
                iotsetcaption("Skokoban [Stage : %d][move : %d]" % (stagenum + 1, iotcount))
            else:
                manx = tempx
                many = tempy
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()