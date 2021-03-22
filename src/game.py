from board import Board
from stats import Stats
from settings import Settings

class Game:
    def __init__(self, settings):
        self.settings = settings
        self.board = None
        self.stats = Stats()
        self.select_board()
        
    def select_board(self):
        staticboard = Board([[['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty'],          ['grass','empty']],
                                [['bCenter','empty'],       ['grass','empty'],          ['rCenter','empty'],        ['grass','empty'],          ['block','block']],
                                [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block'],          ['grass','empty']],
                                [['block','block'],         ['grass','empty'],          ['grass','empty'],          ['grass','bPiece'],         ['block','block']],
                                [['grass','gPiece'],        ['gCenter','empty'],        ['block','block'],          ['block','block'],          ['block','block']]])
        staticboard2 = Board([[['block','block'],         ['block','block'],          ['block','block'],          ['block','block'],          ['grass','empty'],          ['block','block']],
                                [['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty'],          ['bCenter','empty'],          ['block','block']],
                                [['grass','empty'],       ['grass','empty'],          ['rCenter','empty'],        ['grass','empty'],          ['block','block'],          ['block','block']],
                                [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block'],          ['grass','empty'],          ['block','block']],
                                [['block','block'],         ['grass','empty'],          ['grass','empty'],          ['grass','bPiece'],         ['block','block'],          ['block','block']],
                                [['grass','gPiece'],        ['gCenter','empty'],        ['block','block'],          ['block','block'],          ['block','block'],          ['block','block']]])
        staticboard3 = Board([[['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty']],
                                [['bCenter','empty'],       ['grass','empty'],          ['rCenter','empty'],        ['grass','bPiece']],
                                [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block']],
                                [['grass','gPiece'],        ['gCenter','empty'],        ['block','block'],          ['block','block']]])
        if self.settings.puzzledb == 1:
            self.board = staticboard3
        elif self.settings.puzzledb == 2:
            self.board = staticboard
        elif self.settings.puzzledb == 3:
            self.board = staticboard2
        elif self.settings.puzzledb == 4:
            self.board = staticboard
