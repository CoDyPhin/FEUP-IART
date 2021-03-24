from piece import Center
from piece import Piece

class Board:
    def __init__(self, board):
        self.board = board
        self.pieces = []
        self.centers = []
        self.retrieveCenters()
        self.retrievePieces()
        self.parentBoard = None #   (?) trace path using search algorithms

    def setParentBoard(self, board):
        self.parentBoard = board
        return self

    def retrieveCenters(self):
        for i in range(len(self.board)):
            colsize = len(self.board[0])
            for j in range(colsize):
                if('C' in self.board[i][j][0]):
                    self.centers.append(Center(j,i,self.board[i][j][0][0]))

    def retrievePieces(self):
        for i in range(len(self.board)):
            colsize = len(self.board[0])
            for j in range(colsize):
                destX = []
                destY = []
                if('P' in self.board[i][j][1]):
                    for center in self.centers:
                        if (center.color == self.board[i][j][1][0]):
                            destX.append(center.x)
                            destY.append(center.y)
                    self.pieces.append(Piece(j,i,destX,destY,self.board[i][j][1][0]))

    
    def check_game_over(self):
        for piece in self.pieces:
            if (piece.x,piece.y) not in [(piece.destX[i],piece.destY[i]) for i in range(len(piece.destX))]:
                return False
        return True

    def make_move(self, rowfactor, colfactor):
        rowsize = len(self.board)
        colsize = len(self.board[0])
        something_moved = False
        for piece in self.pieces:
            counter = 1 
            while( ((piece.y + rowfactor*counter) in range(rowsize)) and ((piece.x + colfactor*counter) in range(colsize)) and (self.board[piece.y + rowfactor * counter][piece.x + colfactor * counter][1]=='-')):
                self.board[(piece.y + rowfactor * (counter-1))][piece.x + colfactor*(counter-1)][1] = '-'
                self.board[(piece.y + rowfactor * counter)][piece.x + colfactor * counter][1] = piece.content
                counter+=1
                something_moved = True

            piece.x += (counter - 1)*colfactor
            piece.y += (counter - 1)*rowfactor
        return something_moved


    def move_up(self):
        rowfactor = -1
        colfactor = 0
        self.pieces.sort(key=lambda a: a.y)
        return self.make_move(rowfactor, colfactor)


    def move_down(self):
        rowfactor = 1
        colfactor = 0
        self.pieces.sort(reverse=True, key=lambda a: a.y)
        return self.make_move(rowfactor, colfactor)


    def move_left(self):
        rowfactor = 0
        colfactor = -1
        self.pieces.sort(key=lambda a: a.x)
        return self.make_move(rowfactor, colfactor)


    def move_right(self):
        rowfactor = 0
        colfactor = 1
        self.pieces.sort(reverse=True, key=lambda a: a.x)
        return self.make_move(rowfactor, colfactor)
