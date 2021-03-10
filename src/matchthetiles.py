import pygame
import os

# pygame initialization
pygame.init()

# Game Settings
BACKGRD_COLOR = (176,224,230)
FPS = 60
WIDTH, HEIGHT = 1280, 720
BOARDSIZE = {"small":4, "medium":5, "big":6}

# Window setup
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Match the Tiles")

# Sprite loading
BLOCK_IMG = pygame.image.load(os.path.join('assets', 'block.png'))
GRASS_IMG = pygame.image.load(os.path.join('assets', 'grass.png'))
BLUE_PIECE_IMG = pygame.image.load(os.path.join('assets', 'bluepiece.png'))
RED_PIECE_IMG = pygame.image.load(os.path.join('assets', 'redpiece.png'))
GREEN_PIECE_IMG = pygame.image.load(os.path.join('assets', 'greenpiece.png'))
YELLOW_PIECE_IMG = pygame.image.load(os.path.join('assets', 'yellowpiece.png'))
PURPLE_PIECE_IMG = pygame.image.load(os.path.join('assets', 'purplepiece.png'))
BLUE_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'blueinside.png'))
RED_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'redinside.png'))
GREEN_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'greeninside.png'))
YELLOW_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'yellowinside.png'))
PURPLE_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'purpleinside.png'))

# Sprite organizing
SPRITES_IMG = {'bPiece': BLUE_PIECE_IMG, 'rPiece': RED_PIECE_IMG, 'gPiece': GREEN_PIECE_IMG, 'yPiece': YELLOW_PIECE_IMG, 'pPiece': PURPLE_PIECE_IMG, 
'bCenter': BLUE_INSIDE_IMG, 'rCenter': RED_INSIDE_IMG, 'gCenter': GREEN_INSIDE_IMG, 'yCenter': YELLOW_INSIDE_IMG, 'pCenter': PURPLE_INSIDE_IMG}

BLOCK = pygame.transform.scale(BLOCK_IMG, (110, 110))
GRASS = pygame.transform.scale(GRASS_IMG, (110, 110))
SPRITES = {'block': BLOCK, 'grass': GRASS}

for (key,value) in SPRITES_IMG.items():
    SPRITES[key] = pygame.transform.scale(value, (110, 110))

# Puzzle Board
BOARD = [
    [['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty'],          ['grass','empty']],
    [['bCenter','empty'],       ['grass','empty'],          ['rCenter','empty'],        ['grass','empty'],          ['block','block']],
    [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block'],          ['grass','empty']],
    [['block','block'],         ['grass','empty'],          ['grass','empty'],          ['grass','bPiece'],         ['block','block']],
    [['grass','gPiece'],        ['gCenter','empty'],        ['block','block'],          ['block','block'],          ['block','block']]]


# Draw Board on Screen

def draw_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(2):
                if(board[i][j][k] != 'empty'):
                    SCREEN.blit(SPRITES[board[i][j][k]], (350+110*(j),100+110*(i)))


# Screen drawing and updating

def draw_screen(board):
    SCREEN.fill(BACKGRD_COLOR)
    draw_board(board)
    pygame.display.update()


# Key assessment

def arrow_movement(board, previouskey):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and previouskey!='up':
        print('up')
        return (movement_handler(board, -1, 0),'up')
    elif keys_pressed[pygame.K_DOWN] and previouskey!='down':
        print('down')
        return (movement_handler(board, 1, 0),'down')
    elif keys_pressed[pygame.K_LEFT] and previouskey!='left':
        print('left')
        return (movement_handler(board, 0, -1),'left')
    elif keys_pressed[pygame.K_RIGHT] and previouskey!='right':
        print('right')
        return (movement_handler(board, 0, 1),'right')
    else: return (board,previouskey)


# Board generation according to the key pressed/movement factor

def movement_handler(board, rowfactor, colfactor):
    newboard = board
    rowsize = len(board)
    for i in range(rowsize):
        colsize = len(board[i])
        for j in range(colsize):
            if(board[i][j][1].find('Piece')!=-1):
                piece = board[i][j][1]
                counter = 1
                while( ((i+rowfactor*counter) in range(rowsize)) and ((j+colfactor*counter) in range(colsize)) and (newboard[i+rowfactor*counter][j+colfactor*counter][1]=='empty')):
                    newboard[(i+rowfactor*(counter-1))][j+colfactor*(counter-1)][1]='empty'
                    newboard[(i+rowfactor*counter)][j+colfactor*counter][1]=piece
                    counter+=1
    return newboard


def flatten_board(board):
    flat_list = []
    for sublist in board:
        for subsubl in sublist:
            for item in subsubl:
                flat_list.append(item)
    return flat_list


def count_on_board(string, flatlist):
    if(string=='pieces'):
        return sum('Piece' in s for s in flatlist)
    if(string=='centers'):
        return sum('Center' in s for s in flatlist)
    returnval = flatlist.count(string)
    if(string=='block'):
        returnval/=2
    return returnval


def check_game_over(board, npieces):
    for row in board:
        for square in row:
            if(square[0].find('Center')!=-1 and square[1].find('Piece')!=-1 and square[0][0]==square[1][0]):
                npieces-=1
    return npieces==0
    

def main():
    clock = pygame.time.Clock()
    running = True
    flatboard = flatten_board(BOARD)
    board = BOARD
    ncenters = count_on_board('centers', flatboard)
    previouskey = 'none'
    while running:
        clock.tick(FPS)


        returnval = arrow_movement(board, previouskey)
        newboard = returnval[0]
        previouskey = returnval[1]
        draw_screen(newboard)
        running = not check_game_over(newboard,ncenters)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()