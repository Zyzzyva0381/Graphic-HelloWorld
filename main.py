# -*- coding:utf-8 -*-

# Normal start stuff,don't change
import pygame, sys, time
from pygame.locals import *
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

# setting up the window
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Hello,World!')

# setting up the numbers
#        red gre blu
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (225,0,0)
GREEN = (0,175,0)
BLUE = (0,225,225)

# define functions
def terminate():
    pygame.quit()
    sys.exit()

magicImg = pygame.image.load('magic.png')
magicx = 50
magicy = 0
magicDirection = 90 # 90 -> right, -90 -> left, 0 -> up, 180 -> down

fontObj = pygame.font.Font('Lucida.ttf',32)
textSurfaceObj = fontObj.render("Hello,World!",True,GREEN,BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

soundObj = pygame.mixer.Sound('bgmusic.wav')
soundObj.play()

# load images
#noneImg = pygame.image.load('none.png')
#nonex = 200
#noney = 0
#noneDirection = '90' # 90 -> right, -90 -> left, 0 -> up, 180 -> down

# main game loop
while True:
    mouseClicked = False
    DISPLAYSURF.fill(BLUE)

    # scripts for images
    if magicDirection == 90:
        magicx += 5
        if magicx >=200:
            magicDirection = -90
    if magicDirection == -90:
        magicx -= 5
        if magicx <=50:
            magicDirection = 90
    
    # blit things
    #DISPLAYSURF.blit(noneImg,(nonex,noney))
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    DISPLAYSURF.blit(magicImg,(magicx,magicy))

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == MOUSEMOTION:
            mousex,mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex,mousey = event.pos
            mouseClicked = True


    # draw screen and tick FPS
    pygame.display.update()
    fpsClock.tick(FPS)
