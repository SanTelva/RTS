# -*- coding: utf-8 -*-

import random, sys, pygame
from pygame.locals import *
WINDOWWIDTH=1280
WINDOWHEIGHT=640
BGCOLOR = (0, 255, 255)
FORESTCOLOR = (20, 200, 20)
GRASSCOLOR = (15, 230, 10)
GRASSHEIGHT = 310
Aqua=(  0, 255, 255)
Black=(  0,   0,   0)
Blue=(  0,  0, 255)
Fuchsia=(255,   0, 255)
Gray=(128, 128, 128)
Green=(  0, 128,   0)
Lime=(  0, 255,   0)
Maroon=(128,  0,   0)
Navyblue=(  0,  0, 128)
Olive=(128, 128,   0)
Purple=(128,  0, 128)
Red=(255,   0,   0)
Silver=(192, 192, 192)
Teal=(  0, 128, 128)
White=(255, 255, 255)
Yellow=(255, 255,   0)
def main():
    global DISPLAYSURF
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mousex = 0
    mousey = 0
    pygame.display.set_caption('Игра')
    DISPLAYSURF.fill(BGCOLOR)
    creation()
    while True:
        mouseClicked = False        
        for event in pygame.event.get(): # event handling loop  
            if event.type == QUIT:
                pygame.quit()
                sys.exit()                
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                wall(mousex, mousey)
        
        pygame.display.update()

def wall(x,y):
    wallImg = pygame.image.load('Wall.png')
    DISPLAYSURF.blit(wallImg, (x-60, y-60))    
def creation():
    global DISPLAYSURF
    pygame.draw.rect(DISPLAYSURF, GRASSCOLOR, (0, GRASSHEIGHT, WINDOWWIDTH, WINDOWHEIGHT),0)
    pygame.draw.line(DISPLAYSURF, FORESTCOLOR, (0,GRASSHEIGHT), (WINDOWWIDTH, GRASSHEIGHT), 20)
if __name__ == '__main__':
        main()