import pygame
import random
pygame.init()

def is_complete(board):
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                return False
            # temporarily clear cell to validate
            board[r][c] = 0
            if not is_valid(board, num, (r, c)):
                board[r][c] = num
                return False
            board[r][c] = num
    return True



def is_valid(board, num, pos):
    r, c = pos

    # Row check
    for j in range(9):
        if board[r][j] == num and j != c:
            return False

    # Col check
    for i in range(9):
        if board[i][c] == num and i != r:
            return False

    # Box check
    box_x, box_y = c // 3, r // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True




font = pygame.font.SysFont(None, 48)
font1=pygame.font.SysFont(None,25)
l1=list(range(1,10))
random.shuffle(l1)
kkk=[[0]*9 for _ in range(9)]
row=100
col=100
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
original = [row[:] for row in kkk]
print(kkk)

scr=pygame.display.set_mode((400,400))
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
            if row < 9 and col < 9 and original[row][col]==0:  # valid selection
                if i.key in [pygame.K_1, pygame.K_2, pygame.K_3,pygame.K_4, pygame.K_5, pygame.K_6,pygame.K_7, pygame.K_8, pygame.K_9]:
                    number = int(pygame.key.name(i.key)) 
                     # convert key to int
                    if is_valid(kkk, number,(row,col)):
                        kkk[row][col] = number
                    else:
                        # if not is_valid(kkk, number, (row, col)):
                        pygame.draw.rect(scr, (255, 0, 0), [col*33, row*33, 33, 33])
                elif i.key == pygame.K_BACKSPACE or i.key == pygame.K_DELETE or i.key==pygame.K_0:
                    kkk[row][col] = 0



    pygame.draw.rect(scr,(255,0,0),[col*33,row*33,33,33],3)

            

    


    for i in range(gs + 1):
        lt = 3 if i % 3 == 0 else 1
        
        pygame.draw.line(scr, lc, (i*cs, 0), (i*cs, bs), lt)
       
        pygame.draw.line(scr, lc, (0, i*cs), (bs, i*cs), lt)
    gg={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in range(9):
        for j in range(9):
            if kkk[i][j] in gg:
                gg[kkk[i][j]]+=1

            if original[i][j] != 0:
                color = (0, 0, 0)  
            else:
                color = (0, 0, 255)  
            


            if kkk[i][j]!=0:
                text = font.render(str(kkk[i][j]), True, color)
                text_rect = text.get_rect(center=(j*cs + cs//2, i*cs + cs//2))
                scr.blit(text, text_rect)
    
    tx=font1.render(str(gg),True,(0,0,0))
    scr.blit(tx,(0,350))

    
    if is_complete(kkk):
        print("You solved the puzzle!")
        run = False

        # text_rect = font.get_rect(center=(col*cs + cs//2, row*cs + cs//2))
        # scr.blit(text_rect,font)

    pygame.display.update()

pygame.quit()