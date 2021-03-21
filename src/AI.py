from board import Board  

import pygame
import os


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





BOARD = [
    [['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty'],          ['grass','empty']],
    [['bCenter','empty'],       ['grass','empty'],          ['rCenter','empty'],        ['grass','empty'],          ['block','block']],
    [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block'],          ['grass','empty']],
    [['block','block'],         ['grass','empty'],          ['grass','empty'],          ['grass','bPiece'],         ['block','block']],
    [['grass','gPiece'],        ['gCenter','empty'],        ['block','block'],          ['block','block'],          ['block','block']]]




board = Board(BOARD)



def handle_movement(board, previouskey):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and previouskey!='up':      
        board.move_up() 
        return 'up'
    
    elif keys_pressed[pygame.K_DOWN] and previouskey!='down':
        board.move_down()
        return 'down'
    
    elif keys_pressed[pygame.K_LEFT] and previouskey!='left':
        board.move_left()
        return 'left'
    
    elif keys_pressed[pygame.K_RIGHT] and previouskey!='right':
        board.move_right()
        return 'right'
    
    else: return previouskey

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



def main():
    clock = pygame.time.Clock()
    previouskey = "None"
    running = True
    while running:
        previouskey = handle_movement(board, previouskey)
        draw_screen(board.board)

        running = not board.check_game_over()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()