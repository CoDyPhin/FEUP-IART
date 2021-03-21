from piece import Center
from piece import Piece

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