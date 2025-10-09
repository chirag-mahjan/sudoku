import pygame
import random
pygame.init()
hole=10

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

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty

    for num in range(1, 10):
        if is_valid(board, num, (r, c)):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0
    return False

def generate_full_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    numbers = list(range(1, 10))
    for i in range(0, 9, 3):  # fill diagonal 3x3 boxes first (helps solver)
        random.shuffle(numbers)
        for r in range(3):
            for c in range(3):
                board[i+r][i+c] = numbers[r*3+c]
    solve(board)
    return board

def make_puzzle(board, holes=10):
    puzzle = [row[:] for row in board]  # copy
    count = holes
    while count > 0:
        r = random.randint(0, 8)
        c = random.randint(0, 8)
        if puzzle[r][c] != 0:
            puzzle[r][c] = 0
            count -= 1
    return puzzle


font = pygame.font.SysFont(None, 48)
font1=pygame.font.SysFont(None,25)
l1=list(range(1,10))
random.shuffle(l1)
full_board = generate_full_board()
kkk = make_puzzle(full_board, hole)  
original = [row[:] for row in kkk]
row=100
col=100


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
    
    count_text = " ".join([f"{n}:{gg[n]}  " for n in range(1,10)])
    tx = font1.render(count_text, True, (0,0,0))
    scr.blit(tx, (10, bs+10))


    
    if is_complete(kkk):
        scr.fill(white)
        txx = font.render("You solved the puzzle!", True, (0, 128, 0))
        scr.blit(txx, (50, 180))

        print("You solved the puzzle!")

    pygame.display.update()

pygame.quit()