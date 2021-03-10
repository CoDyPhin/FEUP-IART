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
SPRITES_IMG = {'bluePiece': BLUE_PIECE_IMG, 'redPiece': RED_PIECE_IMG, 'greenPiece': GREEN_PIECE_IMG, 'yellowPiece': YELLOW_PIECE_IMG, 'purplePiece': PURPLE_PIECE_IMG, 
'blueCenter': BLUE_INSIDE_IMG, 'redCenter': RED_INSIDE_IMG, 'greenCenter': GREEN_INSIDE_IMG, 'yellowCenter': YELLOW_INSIDE_IMG, 'purpleCenter': PURPLE_INSIDE_IMG}

BLOCK = pygame.transform.scale(BLOCK_IMG, (110, 110))
GRASS = pygame.transform.scale(GRASS_IMG, (110, 110))
SPRITES = {'block': BLOCK, 'grass': GRASS}

for (key,value) in SPRITES_IMG.items():
    SPRITES[key] = pygame.transform.scale(value, (110, 110))

BOARD = [
    [['block', 'block'],        ['grass','redPiece'],       ['grass','empty'],          ['grass','empty'],          ['grass','empty']],
    [['purpleCenter','empty'],  ['grass','empty'],          ['redCenter','empty'],      ['grass','empty'],          ['block','block']],
    [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block'],          ['grass','empty']],
    [['block','block'],         ['grass','empty'],          ['grass','empty'],          ['grass','purplePiece'],    ['block','block']],
    [['grass','greenPiece'],    ['greenCenter','empty'],    ['block','block'],          ['block','block'],          ['block','block']]]

def draw_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(2):
                if(board[i][j][k] != 'empty'):
                    SCREEN.blit(SPRITES[board[i][j][k]], (350+110*(j),100+110*(i)))


def draw_screen(board):
    SCREEN.fill(BACKGRD_COLOR)
    draw_board(board)
    pygame.display.update()

def arrow_movement(board):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        return movement_handler(board, -1, 0)
    elif keys_pressed[pygame.K_DOWN]:
        return movement_handler(board, 1, 0)
    elif keys_pressed[pygame.K_LEFT]:
        return movement_handler(board, 0, -1)
    elif keys_pressed[pygame.K_RIGHT]:
        return movement_handler(board, 0, 1)
    else: return board

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
    return newboard

def main():
    clock = pygame.time.Clock()
    running = True
    board = BOARD
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        newboard = arrow_movement(board)
        draw_screen(newboard)
    pygame.quit()

if __name__ == "__main__":
    main()