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

    


    def dfs(self, gameState):
        gameStateBoard = gameState.board

        neighbours = [copy.deepcopy(gameState) for i in range(4)]
        neighbour_boards = [neighbours[0].board.setParentBoard(gameStateBoard).move_up(), neighbours[1].board.setParentBoard(gameStateBoard).move_down(), neighbours[2].board.setParentBoard(gameStateBoard).move_left(), neighbours[3].board.setParentBoard(gameStateBoard).move_right()]
        neighbours = [neighbours[i] for i in range(len(neighbour_boards)) if neighbour_boards[i] == True]

        if gameStateBoard.board not in self.dfs_visited:
            self.dfs_visited.append(gameStateBoard.board)
            for neighbour in neighbours:
                if neighbour.board.check_game_over():
                    print("Solution found in " + str(len(getPath(neighbour.board, []))) + " moves")
                    gameState.stats.moves = len(getPath(neighbour.board, []))
                    return neighbour
                
                self.dfs(neighbour)
    
    
    # def dfs(self, gameState):   #iterative
    #     where_to_go_next = []
    #     self.dfs_visited = []
    #     where_to_go_next.append(gameState)

    #     while where_to_go_next:
    #         current_node = where_to_go_next.pop(-1)
    #         self.dfs_visited.append(current_node.board)
            
    #         if current_node.check_game_over():
    #             print("Found solution in " + str(len(getPath(current_node, [])))+ " moves")
    #             return current_node

    #         neighbours = [copy.deepcopy(current_node).setParentBoard(current_node) for i in range(4)]
    #         neighbour_boards = [neighbours[0].move_up(), neighbours[1].move_down(), neighbours[2].move_left(), neighbours[3].move_right()]
    #         neighbours = [neighbours[i] for i in range(len(neighbours)) if neighbour_boards[i]]
            
    #         for neighbour in neighbours:

    #             if neighbour.board not in self.dfs_visited:
    #                 where_to_go_next.append(neighbour)
                



        
    
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


def getPath(board, listBoards):
    if (board.parentBoard == None):
        return listBoards
    listBoards.append(board)
    return getPath(board.parentBoard, listBoards)