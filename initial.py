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
kkk = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

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
        if i.type == pygame.KEYDOWN:
            if row < 9 and col < 9:  # valid selection
                if i.key == pygame.K_1:
                    kkk[row][col] = 1
                elif i.key == pygame.K_2:
                    kkk[row][col] = 2
                elif i.key == pygame.K_3:
                    kkk[row][col] = 3
                elif i.key == pygame.K_4:
                    kkk[row][col] = 4
                elif i.key == pygame.K_5:
                    kkk[row][col] = 5
                elif i.key == pygame.K_6:
                    kkk[row][col] = 6
                elif i.key == pygame.K_7:
                    kkk[row][col] = 7
                elif i.key == pygame.K_8:
                    kkk[row][col] = 8
                elif i.key == pygame.K_9:
                    kkk[row][col] = 9

                
                elif i.key == pygame.K_BACKSPACE:
                    kkk[row][col] = 0
    pygame.draw.rect(scr,(255,0,0),[col*33,row*33,33,33],3)

            

    


    for i in range(gs + 1):
        lt = 3 if i % 3 == 0 else 1
        
        pygame.draw.line(scr, lc, (i*cs, 0), (i*cs, bs), lt)
       
        pygame.draw.line(scr, lc, (0, i*cs), (bs, i*cs), lt)
    for i in range(9):
        for j in range(9):

            if kkk[i][j]!=0:
                text = font.render(str(kkk[i][j]), True, (0, 0, 0))
                text_rect = text.get_rect(center=(j*cs + cs//2, i*cs + cs//2))
                scr.blit(text, text_rect)

        # text_rect = font.get_rect(center=(col*cs + cs//2, row*cs + cs//2))
        # scr.blit(text_rect,font)







    pygame.display.update()

pygame.quit()