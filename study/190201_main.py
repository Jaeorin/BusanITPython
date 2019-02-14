import pygame

WHITE         = (48, 48, 48)
displaywidth  = 470
displayheight = 840
displayobj    = None
clock         = None
imgbackA      = pygame.image.load('image/back.png')
imgbackB      = imgbackA.copy()

def iotsetcaption(caption):
    pygame.display.set_caption(caption)

def iotbackdraw(image, x, y):
    global displayobj
    displayobj.blit(image, (x, y))

def iotgo():
    global displayobj
    global clock

    backAposy = 0
    backBposy = -displayheight

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            pygame.quit()
            break

        backAposy = backAposy + 2
        backBposy = backBposy + 2

        if displayheight <= backAposy:
            backAposy = 0
            backBposy = -displayheight


        displayobj.fill(WHITE)
        iotbackdraw(imgbackA, 0, backAposy)
        iotbackdraw(imgbackB, 0, backBposy)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()

def base():
    global displayobj
    global clock

    pygame.init()
    iotsetcaption("IoT Game")
    displayobj = pygame.display.set_mode((displaywidth, displayheight))
    clock = pygame.time.Clock()

    iotgo()

base()