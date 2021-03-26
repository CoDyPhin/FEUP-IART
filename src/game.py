from board import *
from stats import *
from settings import *
import copy
import random

global gamesettings
gamesettings = Settings(1,1,1,1,1,1)

class Game:
    def __init__(self, settings):
        self.settings = settings
        self.board = None
        self.stats = Stats()
        self.select_board()
        self.dfs_visited = []
        self.iddfs_solution = None
        self.dfs_result = []
        self.nodes_expanded = 0
        
    def select_board(self):
        staticboard = Board([[['o', 'gP'], ['o', '-'], ['o', '-'], ['o', '-'], ['o', '-']], [['gC', '-'], ['x', 'x'], ['o', '-'], ['x', 'x'], ['o', '-']], [['x', 'x'], ['x', 'x'], ['o', '-'], ['o', '-'], ['o', '-']], [['o', '-'], ['o', '-'], ['o', '-'], ['x', 'x'], ['o', '-']], [['bC', '-'], ['o', '-'], ['o', '-'], ['o', 'bP'], ['x', 'x']]])

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

        if self.settings.randompz == 2:
            self.get_possible_board()
            self.board.parentBoard = None
        else:
            if self.settings.puzzledb == 1:
                self.board = staticboard3
            elif self.settings.puzzledb == 2:
                self.board = staticboard2
            elif self.settings.puzzledb == 3:
                self.board = staticboard4

    def cleanstack(self):
        self.dfs_visited = []
        self.dfs_result = []
        self.iddfs_result = []

    def neighbours(self):
        neighbours = [copy.deepcopy(self) for i in range(4)]
        neighbour_boards = [neighbours[0].board.setParentBoard(self.board).move_up(), neighbours[1].board.setParentBoard(self.board).move_down(), neighbours[2].board.setParentBoard(self.board).move_left(), neighbours[3].board.setParentBoard(self.board).move_right()]
        neighbours = [neighbours[i] for i in range(len(neighbour_boards)) if neighbour_boards[i] == True]
        return neighbours

# Search Methods

    def dfs(self, gameState):
        gameStateBoard = gameState.board
        if gameStateBoard.board not in self.dfs_visited: 
            self.dfs_visited.append(gameStateBoard.board)
            neighbours = gameState.neighbours()
            self.stats.operations += len(neighbours)
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
            self.stats.operations+=1
            s = queue.pop(0)
            neighbours = [copy.deepcopy(s).setParentBoard(s) for i in range(4)]
            neighbour_boards = [neighbours[0].move_up(), neighbours[1].move_down(), neighbours[2].move_left(), neighbours[3].move_right()]
            neighbours = [neighbours[i] for i in range(len(neighbours)) if neighbour_boards[i] == True]
            self.stats.operations += len(neighbours)
            for neighbour in neighbours:
                if neighbour not in visited:
                    if neighbour.check_game_over():
                        gameState.stats.moves = len(getPath(neighbour, []))
                        return getPath(neighbour, [])
                    visited.append(neighbour)
                    queue.append(neighbour)


    def iterative_deepening(self, gameState):
        depth = 1
        self.iddfs_result = None
        while True:     #BEWARE OF IMPOSSIBLE PUZZLES
            self.dfs_visited = []
            self.iddfs(gameState, depth)
            if self.iddfs_solution != None:
                result = getPath(self.iddfs_solution.board, [])
                return result
            depth += 2
            #print(depth)


    def iddfs(self, gameState, depth):
        if (depth == 0):
            return None

        gameStateBoard = gameState.board
        self.dfs_visited.append(gameStateBoard.parentBoard)
        if gameStateBoard.board not in self.dfs_visited:
            neighbours = gameState.neighbours()
            self.stats.operations += len(neighbours)
            for neighbour in neighbours:
                if neighbour.board.check_game_over():
                    self.iddfs_solution = neighbour
                    return neighbour
                
                self.iddfs(neighbour, depth-1)


    

    def simple_heuristics(self):
        points = 0
        gameStateBoard = self.board
        for piece in gameStateBoard.pieces:
            listCenters = zip(piece.destX, piece.destY)
            for center in listCenters:
                if center[0] != piece.x: points += 1
                if center[1] != piece.y: points += 1
        
        return points



    def heuristics(self):
        points = 0
        gameStateBoard = self.board
        for piece in gameStateBoard.pieces:
            listCenters = zip(piece.destX, piece.destY)
            for center in listCenters:
                if center[0] == piece.x: points += check_obstaclesX(piece, center[0], gameStateBoard.board)
                if center[1] == piece.y: points += check_obstaclesX(piece, center[1], gameStateBoard.board)
                if center[0] != piece.x: points += 1
                if center[1] != piece.y: points += 1
        
        return points

    # def heuristics(self):
    #     points = 0
    #     gameStateBoard = self.board
    #     points_list = []
    #     for piece in gameStateBoard.pieces:
    #         listCenters = zip(piece.destX, piece.destY)
    #         for center in listCenters:
    #             pointsAux = 0
    #             if center[0] == piece.x: pointsAux += check_obstaclesX(piece, center[0], gameStateBoard.board)
    #             if center[1] == piece.y: pointsAux += check_obstaclesX(piece, center[1], gameStateBoard.board)
    #             if center[0] != piece.x: pointsAux += 1
    #             if center[1] != piece.y: pointsAux += 1
    #             points_list.append(pointsAux)
    #         points += min(points_list)
        
    #     return points



    def greedy_search(self, easy = False):
        self.dfs_visited = []
        start_node = copy.deepcopy(self)
        current_node = copy.deepcopy(self)
        while True:
            self.dfs_visited.append(current_node.board.board)
            
            if current_node.board.check_game_over():
                return getPath(current_node.board, [])
           
            neighbours = [x for x in current_node.neighbours() if x.board.board not in self.dfs_visited]

            if len(neighbours) == 0:
                self.dfs_visited.append(current_node.board.board)
                current_node.board = current_node.board.parentBoard #BACKTRACK
                continue
            
            if not easy:
                current_node = min(neighbours, key = lambda x: x.heuristics())    #Expands the node with max points
            else:
                current_node = min(neighbours, key = lambda x: x.simple_heuristics())
        return None


    def a_star_search(self, easy = True, limit = False):
        self.dfs_visited = []
        current = copy.deepcopy(self)
        frontier = [current]
        cost_so_far = {current: 0}
        self.nodes_expanded = 0
        self.stats.start_timer()

        while frontier:
            self.stats.update_timer()

            if self.stats.ms > 800 and limit:
                print("FOI ALI")
                return []
                

            if not easy: current = min(frontier, key = lambda x: cost_so_far[x] + x.heuristics())
            else: current = min(frontier, key = lambda x: cost_so_far[x] + x.simple_heuristics())
            
            
            self.nodes_expanded += 1

            if current.board.check_game_over():
                return getPath(current.board, [])

            neighbours = [x for x in current.neighbours() if x not in self.dfs_visited]

            for next in neighbours:
                self.dfs_visited.append(next)
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    frontier.append(next)
            
            frontier.remove(current)

        print("Impossible puzzle!")
        return []



    #   GENERATE RANDOM PUZZLES
    
    def generate_random_board(self):
        empty_board = [[['o','-'],        ['o','-'],     ['o','-'],     ['o','-'],      ['o','-']],
        [['o','-'],        ['o','-'],      ['o','-'],    ['o','-'],      ['o','-']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['o','-'],      ['o','-']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['o','-'],     ['o','-']],
        [['o','-'],        ['o','-'],     ['o','-'],     ['o','-'],      ['o','-']]]

        pieces = [['gC','gP'], ['bC','bP'], ['rC','rP'], ['yC','yP'], ['pC','pP']]
        pieces_to_use = [pieces[x] for x in range(random.randint(2, len(pieces)))]

        n_obstacles = random.randint(5,10)

        possible_positions = []

        for i in range(len(empty_board)):
            possible_positions.append((0, i))
            possible_positions.append((i, 0))
            possible_positions.append((len(empty_board) - 1, i))
            possible_positions.append((i, len(empty_board) - 1))

        for i in range(n_obstacles):
            (row, col) = (random.randrange(5), random.randrange(5))
            empty_board[col][row] = ['x', 'x']

        while pieces_to_use:
            elem = pieces_to_use.pop(random.randrange(len(pieces_to_use)))
            (row, col) = (0,0)

            found = False
            while not found:
                (row, col) = possible_positions.pop(random.randrange(len(possible_positions)))
                if empty_board[col][row] != ['x', 'x']:
                    found = True

            empty_board[col][row] = elem
        
        return empty_board

    
    
    def generate_random_puzzle(self):
        board = Board(self.generate_random_board())
        self.board = board
    
        visited = [self.board]

        for i in range(7):
            neighbours = [x for x in self.neighbours() if x.board.board not in visited]
            if len(neighbours) == 0:
                #print("DEAD END")
                return None

            self.board = neighbours[random.randrange(len(neighbours))].board
            visited.append(self.board.board)
        
        print(self.board.board)


    
    def get_possible_board(self):
        found = False
        while not found:
            print("Generating board...")
            self.iddfs_solution = None
            self.generate_random_puzzle()
            #self.board.parentBoard = None
            solution = self.a_star_search(False, True)
            if solution != None and len(solution) < 4 : continue
            elif solution != None:
                found = True
                self.cleanstack()

        print("Encontrei uma board valida")
        #self.board = self.genboard

        

   
def check_obstaclesX(piece, centerX, board):
    iterMin = min(piece.x, centerX)
    iterMax = max(piece.y, centerX)
    for i in range(iterMin, iterMax):
        if board[piece.y][i][0] == "block":  return 2
    return 0

def check_obstaclesY(piece, centerY, board):
    iterMin = min(piece.y, centerY)
    iterMax = max(piece.y, centerY)
    for i in range(iterMin, iterMax):
        if board[i][piece.x][0] == "block": return 2
    return 0

def getPath(board, listBoards):
    if (board.parentBoard == None):
        return listBoards
    listBoards.append(board)
    return getPath(board.parentBoard, listBoards)
    