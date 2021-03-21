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




class Center:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.content = color + "Center"

class Piece:
    def __init__(self, x, y, destX, destY, color):
        self.x = x
        self.y = y
        self.destX = destX
        self.destY = destY
        self.color = color
        self.content = color + "Piece"




class Board:
    def __init__(self, board):
        self.board = board
        self.pieces = []
        self.centers = []
        self.retrieveCenters()
        self.retrievePieces()

    def retrieveCenters(self):
        for i in range(len(self.board)):
            colsize = len(self.board[0])
            for j in range(colsize):
                if(self.board[i][j][0].find('Center') != -1):
                    self.centers.append(Center(j,i,self.board[i][j][0][0]))

    def retrievePieces(self):
        for i in range(len(self.board)):
            colsize = len(self.board[0])
            for j in range(colsize):
                if(self.board[i][j][1].find('Piece') != -1):
                    for center in self.centers:
                        if (center.color == self.board[i][j][1][0]):
                            self.pieces.append(Piece(j,i,center.x,center.y,center.color))

    
    def check_game_over(self):
        for piece in self.pieces:
            if piece.x != piece.destX or piece.y != piece.destY:
                return False
        return True


    def move_up(self):
        rowfactor = -1
        colfactor = 0
        rowsize = len(self.board)
        colsize = len(self.board[0])

        for piece in self.pieces:
            counter = 1
            
            while( ((piece.y + rowfactor*counter) in range(rowsize)) and ((piece.x + colfactor*counter) in range(colsize)) and (self.board[piece.y + rowfactor * counter][piece.x + colfactor * counter][1]=='empty')):
                self.board[(piece.y + rowfactor * (counter-1))][piece.x + colfactor*(counter-1)][1] = 'empty'
                self.board[(piece.y + rowfactor * counter)][piece.x + colfactor * counter][1] = piece.content
                counter+=1

            piece.x += (counter - 1)*colfactor
            piece.y += (counter - 1)*rowfactor


    def move_down(self):
        rowfactor = 1
        colfactor = 0
        rowsize = len(self.board)
        colsize = len(self.board[0])

        for piece in self.pieces:
            counter = 1
            
            while( ((piece.y + rowfactor*counter) in range(rowsize)) and ((piece.x + colfactor*counter) in range(colsize)) and (self.board[piece.y + rowfactor * counter][piece.x + colfactor * counter][1]=='empty')):
                self.board[(piece.y + rowfactor * (counter-1))][piece.x + colfactor*(counter-1)][1] = 'empty'
                self.board[(piece.y + rowfactor * counter)][piece.x + colfactor * counter][1] = piece.content
                counter+=1

            piece.x += (counter - 1)*colfactor
            piece.y += (counter - 1)*rowfactor


    def move_left(self):
        rowfactor = 0
        colfactor = -1
        rowsize = len(self.board)
        colsize = len(self.board[0])

        for piece in self.pieces:
            counter = 1
            
            while( ((piece.y + rowfactor*counter) in range(rowsize)) and ((piece.x + colfactor*counter) in range(colsize)) and (self.board[piece.y + rowfactor * counter][piece.x + colfactor * counter][1]=='empty')):
                self.board[(piece.y + rowfactor * (counter-1))][piece.x + colfactor*(counter-1)][1] = 'empty'
                self.board[(piece.y + rowfactor * counter)][piece.x + colfactor * counter][1] = piece.content
                counter+=1

            piece.x += (counter - 1)*colfactor
            piece.y += (counter - 1)*rowfactor


    def move_right(self):
        rowfactor = 0
        colfactor = 1
        rowsize = len(self.board)
        colsize = len(self.board[0])

        for piece in self.pieces:
            counter = 1
            
            while( ((piece.y + rowfactor*counter) in range(rowsize)) and ((piece.x + colfactor*counter) in range(colsize)) and (self.board[piece.y + rowfactor * counter][piece.x + colfactor * counter][1]=='empty')):
                self.board[(piece.y + rowfactor * (counter-1))][piece.x + colfactor*(counter-1)][1] = 'empty'
                self.board[(piece.y + rowfactor * counter)][piece.x + colfactor * counter][1] = piece.content
                counter+=1

            piece.x += (counter - 1)*colfactor
            piece.y += (counter - 1)*rowfactor
        

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