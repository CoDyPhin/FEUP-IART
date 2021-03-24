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
        self.dfs_visited = []
        self.iddfs_solution = None
        self.dfs_result = []
        
    def select_board(self):
        staticboard = Board(    [[['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty'],          ['grass','empty']],
                                [['bCenter','empty'],       ['grass','empty'],          ['rCenter','empty'],        ['grass','empty'],          ['block','block']],
                                [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block'],          ['grass','empty']],
                                [['block','block'],         ['grass','empty'],          ['grass','empty'],          ['grass','bPiece'],         ['block','block']],
                                [['grass','gPiece'],        ['gCenter','empty'],        ['block','block'],          ['block','block'],          ['block','block']]])
        staticboard2 = Board(   [[['block','block'],         ['block','block'],          ['block','block'],          ['block','block'],          ['grass','empty'],          ['block','block']],
                                [['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty'],          ['bCenter','empty'],          ['block','block']],
                                [['grass','empty'],       ['grass','empty'],          ['rCenter','empty'],        ['grass','empty'],          ['block','block'],          ['block','block']],
                                [['block','block'],         ['grass','empty'],          ['block','block'],          ['block','block'],          ['grass','empty'],          ['block','block']],
                                [['block','block'],         ['grass','empty'],          ['grass','empty'],          ['grass','bPiece'],         ['block','block'],          ['block','block']],
                                [['grass','gPiece'],        ['gCenter','empty'],        ['block','block'],          ['block','block'],          ['block','block'],          ['block','block']]])
        staticboard3 = Board(   [[['block', 'block'],        ['grass','rPiece'],         ['grass','empty'],          ['grass','empty']],
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

    def cleanstack(self):
        self.dfs_visited = []
        self.dfs_result = []
        self.iddfs_result = []

    def dfs(self, gameState):
        gameStateBoard = gameState.board

        neighbours = [copy.deepcopy(gameState) for i in range(4)]
        neighbour_boards = [neighbours[0].board.setParentBoard(gameStateBoard).move_up(), neighbours[1].board.setParentBoard(gameStateBoard).move_down(), neighbours[2].board.setParentBoard(gameStateBoard).move_left(), neighbours[3].board.setParentBoard(gameStateBoard).move_right()]
        neighbours = [neighbours[i] for i in range(len(neighbour_boards)) if neighbour_boards[i] == True]

        if gameStateBoard.board not in self.dfs_visited:
            self.dfs_visited.append(gameStateBoard.board)
            for neighbour in neighbours:
                if neighbour.board.check_game_over():
                    result = getPath(neighbour.board, [])
                    self.dfs_result = result
                    return result
                
                self.dfs(neighbour)


        
    
    def bfs(self, gameState):
        rootBoard = gameState.board
        visited = []    #   List to keep track of visited nodes.
        queue = []      #   Initialize a queue
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
                        #print("Solution found in " + str(len(getPath(neighbour, []))) + " moves")
                        gameState.stats.moves = len(getPath(neighbour, []))-1
                        return getPath(neighbour, [])
                    visited.append(neighbour)
                    queue.append(neighbour)


    def iterative_deepening(self, gameState):
        depth = 1
        self.iddfs_result = None
        while True:     #BEWARE OF IMPOSSIBLE PUZZLES
            self.iddfs(gameState, depth)
            if self.iddfs_solution != None:
                result = getPath(self.iddfs_solution.board, [])
                return result
            depth *= 2



    def iddfs(self, gameState, depth):
        gameStateBoard = gameState.board

        neighbours = [copy.deepcopy(gameState) for i in range(4)]
        neighbour_boards = [neighbours[0].board.setParentBoard(gameStateBoard).move_up(), neighbours[1].board.setParentBoard(gameStateBoard).move_down(), neighbours[2].board.setParentBoard(gameStateBoard).move_left(), neighbours[3].board.setParentBoard(gameStateBoard).move_right()]
        neighbours = [neighbours[i] for i in range(len(neighbour_boards)) if neighbour_boards[i] == True]

        if (depth == 0):
            return None

        for neighbour in neighbours:
            if neighbour.board.check_game_over():
                self.iddfs_solution = neighbour
                return neighbour
            
            self.iddfs(neighbour, depth-1)

        
        


def getPath(board, listBoards):
    if (board.parentBoard == None):
        return listBoards
    listBoards.append(board)
    return getPath(board.parentBoard, listBoards)