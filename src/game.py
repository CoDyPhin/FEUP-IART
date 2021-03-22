from board import Board
from stats import Stats
from settings import Settings
import copy

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
        if self.settings.puzzledb == 1:
            self.board = staticboard
        elif self.settings.puzzledb == 2:
            self.board = staticboard
        elif self.settings.puzzledb == 3:
            self.board = staticboard
        elif self.settings.puzzledb == 4:
            self.board = staticboard

    
    def bfs(self, gameState):
        rootBoard = gameState.board
        visited = [] # List to keep track of visited nodes.
        queue = []     #Initialize a queue
        visited.append(rootBoard)
        queue.append(rootBoard)

        while queue:
            s = queue.pop(0)
            neighbours = [copy.deepcopy(s).setParentBoard(s) for i in range(4)]
            neighbour_boards = [neighbours[0].move_up(), neighbours[1].move_down(), neighbours[2].move_left(), neighbours[3].move_right()]
            neighbours = [neighbours[i] for i in range(len(neighbours)) if neighbour_boards[i] == True]

            for neighbour in neighbours:
                if neighbour not in visited:
                    if neighbour.check_game_over():
                        print("Solution found: " + str(len(getPath(neighbour, []))) + " moves")
                        gameState.stats.moves = len(getPath(neighbour, []))
                        return neighbour
                    visited.append(neighbour)
                    queue.append(neighbour)


def getPath(board, listBoards):
    if (board.parentBoard == None):
        return listBoards
    listBoards.append(board)
    return getPath(board.parentBoard, listBoards)