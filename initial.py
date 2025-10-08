import pygame
import random
import time
pygame.init()

# ------------------ Sudoku Logic ------------------
def is_complete(board):
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                return False
            board[r][c] = 0
            if not is_valid(board, num, (r, c)):
                board[r][c] = num
                return False
            board[r][c] = num
    return True

def is_valid(board, num, pos):
    r, c = pos
    for j in range(9):
        if board[r][j] == num and j != c:
            return False
    for i in range(9):
        if board[i][c] == num and i != r:
            return False
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
    for i in range(0, 9, 3):
        random.shuffle(numbers)
        for r in range(3):
            for c in range(3):
                board[i+r][i+c] = numbers[r*3+c]
    solve(board)
    return board

def make_puzzle(board, holes=10):
    puzzle = [row[:] for row in board]
    count = holes
    while count > 0:
        r = random.randint(0, 8)
        c = random.randint(0, 8)
        if puzzle[r][c] != 0:
            puzzle[r][c] = 0
            count -= 1
    return puzzle

# ------------------ Game Setup ------------------
font = pygame.font.SysFont(None, 48)
font1 = pygame.font.SysFont(None, 20)

scr = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Sudoku with Levels")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 150, 0)
gray = (230, 230, 230)

# ------------------ Level Selection Screen ------------------
def level_selection():
    scr.fill(white)
    title_font = pygame.font.SysFont(None, 40)
    button_font = pygame.font.SysFont(None, 35)

    title = title_font.render("Select Difficulty Level", True, black)
    scr.blit(title, (60, 70))

    easy_btn = pygame.Rect(120, 130, 160, 40)
    med_btn = pygame.Rect(120, 190, 160, 40)
    hard_btn = pygame.Rect(120, 250, 160, 40)

    pygame.draw.rect(scr, gray, easy_btn)
    pygame.draw.rect(scr, gray, med_btn)
    pygame.draw.rect(scr, gray, hard_btn)

    scr.blit(button_font.render("Easy", True, black), (170, 135))
    scr.blit(button_font.render("Medium", True, black), (155, 195))
    scr.blit(button_font.render("Hard", True, black), (170, 255))

    pygame.display.update()

    level = None
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.collidepoint(event.pos):
                    level = 1
                    waiting = False
                elif med_btn.collidepoint(event.pos):
                    level = 2
                    waiting = False
                elif hard_btn.collidepoint(event.pos):
                    level = 3
                    waiting = False
    return level

# ------------------ Start Game ------------------
level = level_selection()

if level == 1:
    holes = 16
elif level == 2:
    holes = 25
else:
    holes = 36

full_board = generate_full_board()
kkk = make_puzzle(full_board, holes=holes)
original = [row[:] for row in kkk]

# ------------------ Main Game Loop ------------------
row, col = 100, 100
cs = 33
gs = 9
bs = cs * gs

scr = pygame.display.set_mode((bs, bs + 40))
run = True

while run:
    scr.fill(white)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // cs
            col = pos[0] // cs
            print("Selected cell:", row, col)

        if i.type == pygame.KEYDOWN:
            if row < 9 and col < 9 and original[row][col] == 0:
                if i.key in [pygame.K_1, pygame.K_2, pygame.K_3,
                             pygame.K_4, pygame.K_5, pygame.K_6,
                             pygame.K_7, pygame.K_8, pygame.K_9]:
                    number = int(pygame.key.name(i.key))
                    if is_valid(kkk, number, (row, col)):
                        kkk[row][col] = number
                    else:
                        pygame.draw.rect(scr, red, [col*33, row*33, 33, 33])
                elif i.key in [pygame.K_BACKSPACE, pygame.K_DELETE, pygame.K_0]:
                    kkk[row][col] = 0

    pygame.draw.rect(scr, red, [col*33, row*33, 33, 33], 3)

    for i in range(gs + 1):
        lt = 3 if i % 3 == 0 else 1
        pygame.draw.line(scr, black, (i*cs, 0), (i*cs, bs), lt)
        pygame.draw.line(scr, black, (0, i*cs), (bs, i*cs), lt)

    gg = {n: 0 for n in range(1, 10)}
    for i in range(9):
        for j in range(9):
            if kkk[i][j] in gg:
                gg[kkk[i][j]] += 1
            color = black if original[i][j] != 0 else blue
            if kkk[i][j] != 0:
                text = font.render(str(kkk[i][j]), True, color)
                text_rect = text.get_rect(center=(j*cs + cs//2, i*cs + cs//2))
                scr.blit(text, text_rect)

    count_text = " ".join([f"{n}:{gg[n]}  " for n in range(1, 10)])
    tx = font1.render(count_text, True, black)
    scr.blit(tx, (10, bs + 10))

    if is_complete(kkk):
        font2 = pygame.font.SysFont(None, 30)
        scr.fill(white)
        txx = font2.render("CONGRATULATIONS!", True, green)
        scr.blit(txx, (45, 120))
        pygame.display.update()
        font2 = pygame.font.SysFont(None, 25)
        txx = font2.render("You solved the puzzle!", True, green)
        scr.blit(txx, (60, 150))
        pygame.display.update()
        print("You solved the puzzle!")

        time.sleep(3)
        break

    pygame.display.update()

pygame.quit()
