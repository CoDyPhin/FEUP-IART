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
        self.dfs_result = []
        
    def select_board(self):
        staticboard = Board([   [['x', 'x'],        ['o','rP'],     ['o','-'],     ['o','-'],      ['o','-']],
                                [['bC','-'],        ['o','-'],      ['rC','-'],    ['o','-'],      ['x','x']],
                                [['x','x'],         ['o','-'],      ['x','x'],     ['x','x'],      ['o','-']],
                                [['x','x'],         ['o','-'],      ['o','-'],     ['o','bP'],     ['x','x']],
                                [['o','gP'],        ['gC','-'],     ['x','x'],     ['x','x'],      ['x','x']]])

        staticboard2 = Board([  [['x','x'],         ['x','x'],      ['x','x'],     ['x','x'],      ['o','-'],      ['x','x']],
                                [['x', 'x'],        ['o','rP'],     ['o','-'],     ['o','-'],      ['bC','-'],     ['x','x']],
                                [['o','-'],         ['o','-'],      ['rC','-'],    ['o','-'],      ['x','x'],      ['x','x']],
                                [['x','x'],         ['o','-'],      ['x','x'],     ['x','x'],      ['o','-'],      ['x','x']],
                                [['x','x'],         ['o','-'],      ['o','-'],     ['o','bP'],     ['x','x'],      ['x','x']],
                                [['o','gP'],        ['gC','-'],     ['x','x'],     ['x','x'],      ['x','x'],      ['x','x']]])

        staticboard3 = Board([  [['x', 'x'],        ['o','rP'],     ['o','-'],     ['o','-']],
                                [['bC','-'],        ['o','-'],      ['rC','-'],    ['o','bP']],
                                [['x','x'],         ['o','-'],      ['x','x'],     ['x','x']],
                                [['o','gP'],        ['gC','-'],     ['x','x'],     ['x','x']]])

        staticboard4 = Board([   [['o', 'bP'],        ['x','x'],     ['bC','-'],     ['o','-'],      ['o','bP']],
                                [['bC','-'],        ['o','-'],      ['o','-'],      ['o','-'],      ['x','x']],
                                [['o','-'],         ['o','-'],     ['o','-'],     ['o','-'],      ['o','-']],
                                [['x','x'],         ['x','x'],      ['x','x'],     ['o','-'],     ['o','-']],
                                [['o','-'],        ['x','x'],     ['x','x'],     ['o','-'],      ['o','-']]])
        if self.settings.puzzledb == 1:
            self.board = staticboard3
        elif self.settings.puzzledb == 2:
            self.board = staticboard
        elif self.settings.puzzledb == 3:
            self.board = staticboard4

    def cleanstack(self):
        self.dfs_visited = []
        self.dfs_result = []

    def dfs(self, gameState):
        gameStateBoard = gameState.board
        neighbours = [copy.deepcopy(gameState) for i in range(4)]
        neighbour_boards = [neighbours[0].board.setParentBoard(gameStateBoard).move_up(), neighbours[1].board.setParentBoard(gameStateBoard).move_down(), neighbours[2].board.setParentBoard(gameStateBoard).move_left(), neighbours[3].board.setParentBoard(gameStateBoard).move_right()]
        neighbours = [neighbours[i] for i in range(len(neighbour_boards)) if neighbour_boards[i] == True]
        self.stats.memoryused += len(neighbours)
        if gameStateBoard.board not in self.dfs_visited:
            self.dfs_visited.append(gameStateBoard.board)
            for neighbour in neighbours:
                self.stats.operations +=1
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
            self.stats.operations+=1
            s = queue.pop(0)
            neighbours = [copy.deepcopy(s).setParentBoard(s) for i in range(4)]
            neighbour_boards = [neighbours[0].move_up(), neighbours[1].move_down(), neighbours[2].move_left(), neighbours[3].move_right()]
            neighbours = [neighbours[i] for i in range(len(neighbours)) if neighbour_boards[i] == True]
            self.stats.memoryused += len(neighbours)
            for neighbour in neighbours:
                if neighbour not in visited:
                    if neighbour.check_game_over():
                        #print("Solution found in " + str(len(getPath(neighbour, []))) + " moves")
                        gameState.stats.moves = len(getPath(neighbour, []))
                        return getPath(neighbour, [])
                    visited.append(neighbour)
                    queue.append(neighbour)


def getPath(board, listBoards):
    if (board.parentBoard == None):
        return listBoards
    listBoards.append(board)
    return getPath(board.parentBoard, listBoards)