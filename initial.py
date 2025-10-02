import pygame
import random
pygame.init()
font = pygame.font.SysFont(None, 48)
l1=list(range(1,10))
random.shuffle(l1)
kkk=[[0]*9 for _ in range(9)]
row=10
col=10
kkk[0]=l1
print(kkk)
scr=pygame.display.set_mode((305,305))
run=True
white=(255,255,255)
lc=(0,0,0)
x=2
y=2 
cs = 33
gs = 9
bs = cs * gs
while run:
    scr.fill(white)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // cs
            col = pos[0] // cs
            print("Selected cell:", row, col)
    pygame.draw.rect(scr,(255,0,0),[col*33,row*33,33,33])
            

    


    for i in range(gs + 1):
        lt = 3 if i % 3 == 0 else 1
        
        pygame.draw.line(scr, lc, (i*cs, 0), (i*cs, bs), lt)
       
        pygame.draw.line(scr, lc, (0, i*cs), (bs, i*cs), lt)
    for i in range(9):
        for j in range(9):

            if kkk[i][j]!=0:
                score_text = font.render(str(kkk[i][j]), True, (255, 0, 255))
                scr.blit(score_text, (j*cs+10,i*cs+5))

        # text_rect = font.get_rect(center=(col*cs + cs//2, row*cs + cs//2))
        # scr.blit(text_rect,font)







    pygame.display.update()

pygame.quit()