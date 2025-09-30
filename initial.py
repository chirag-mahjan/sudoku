import pygame
import random
pygame.init()
scr=pygame.display.set_mode((305,305))
run=True
lc=(0,0,0)
x=2
y=2 
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    scr.fill((255,255,255))

    pygame.draw.rect(scr,lc, [x+0,y+0,3,300]) #border
    pygame.draw.rect(scr,lc, [x+297,y+0,3,300])#border

    pygame.draw.rect(scr,lc, [x+0,y+0,300,3])#border
    pygame.draw.rect(scr,lc, [x+0,y+297,300,3])#border

    pygame.draw.rect(scr,lc, [x+0,y+100,300,3])#main grid 
    pygame.draw.rect(scr,lc, [x+0,y+200,300,3])#main grid 
    pygame.draw.rect(scr,lc, [x+100,y+0,3,300])#main grid 
    pygame.draw.rect(scr,lc, [x+200,y+0,3,300])#main grid

    pygame.draw.rect(scr,lc, [x+33,y+0,1,300])
    pygame.draw.rect(scr,lc, [x+133,y+0,1,300])
    pygame.draw.rect(scr,lc, [x+233,y+0,1,300])
    pygame.draw.rect(scr,lc, [x+266,y+0,1,300])
    pygame.draw.rect(scr,lc, [x+166,y+0,1,300])
    pygame.draw.rect(scr,lc, [x+66,y+0,1,300])

    pygame.draw.rect(scr,lc, [x+0,y+33,300,1])
    pygame.draw.rect(scr,lc, [x+0,y+133,300,1])
    pygame.draw.rect(scr,lc, [x+0,y+233,300,1])
    pygame.draw.rect(scr,lc, [x+0,y+266,300,1])
    pygame.draw.rect(scr,lc, [x+0,y+166,300,1])
    pygame.draw.rect(scr,lc, [x+0,y+66,300,1])

    






    pygame.display.update()

pygame.quit()