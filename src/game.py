from database import *
from stats import *
from settings import *
import copy
import itertools
import random

#from drawings import *

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
        self.grouped_pieces = self.group_pieces()
        self.permutations = self.get_permutations()
        
    def select_board(self):
        if self.settings.randompz == 2:
            self.get_possible_board()
            self.board.parentBoard = None
        else:
            if self.settings.puzzledb == 1:
                self.board = copy.deepcopy(easy_db[random.randint(0,len(easy_db)-1)])
            elif self.settings.puzzledb == 2:
                self.board = copy.deepcopy(medium_db[random.randint(0,len(medium_db)-1)])
            elif self.settings.puzzledb == 3:
                self.board = copy.deepcopy(hard_db[random.randint(0,len(hard_db)-1)])

    def get_permutations(self):
        permutations_dict = {}
        for pieces in self.grouped_pieces:
            list_centers = list(zip(pieces[0].destX, pieces[0].destY))
            permutations = [list(zip(x,list_centers)) for x in itertools.permutations(pieces,len(list_centers))]
            permutations_dict[tuple(pieces)] = permutations
        return permutations_dict

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


    
    #*Counts pieces that are already above their center
    def simple_heuristics(self):
        points = 0
        gameStateBoard = self.board
        for piece in gameStateBoard.pieces:
            listCenters = zip(piece.destX, piece.destY)
            for center in listCenters:
                if center[0] != piece.x and center[1] != piece.y:
                    points += 1
        
        return points

    
    


    def group_pieces(self): #GROUP PIECES BY COLOR
        piecesDict = {}
        for piece in self.board.pieces:
            if piece.color not in piecesDict.keys():
                piecesDict[piece.color] = [piece]
            else:
                listPieces = piecesDict[piece.color]
                listPieces.append(piece)
                piecesDict[piece.color] = listPieces
        
        return [x for x in piecesDict.values()]




    def admissible_heuristics(self):
        gameStateBoard = self.board
        piece_points = []
        for pieces in self.grouped_pieces:
            points_list = []
            permutations = self.permutations[tuple(pieces)] #  *Finds best combination between pieces and respective centers*
            for permutation in permutations:
                list_aux = []
                for piece, center in permutation:
                    pointsAux = 0
                    if center[0] == piece.x: pointsAux += check_obstaclesX(piece, center[0], gameStateBoard.board)
                    if center[1] == piece.y: pointsAux += check_obstaclesY(piece, center[1], gameStateBoard.board)
                    pointsAux += estimateCenterDifference(piece, center, gameStateBoard.board)
                    list_aux.append(pointsAux)
                points_list.append(max(list_aux))
           
            piece_points.append(min(points_list))

        return max(piece_points) #*evaluates only the worst piece (otherwise it would not be optimistic)


        
    def heuristics(self):
        points = 0
        gameStateBoard = self.board
        for pieces in self.grouped_pieces:
            points_list = []
            permutations = self.permutations[tuple(pieces)] #  *Finds best combination between pieces and respective centers*
            for permutation in permutations:
                pointsAux = 0
                for piece, center in permutation:
                    pointsAux += estimateCenterDifference(piece, center, gameStateBoard.board)
                points_list.append(pointsAux)
            
            points += min(points_list)

        return points #*evaluates only the worst piece (otherwise it would not be optimistic)


        


    def greedy_search(self, generate = False):
        self.dfs_visited = []
        start_node = copy.deepcopy(self)
        current_node = copy.deepcopy(self)
        starttime = datetime.now()
        while True:
            self.dfs_visited.append(current_node.board.board)
            if current_node.board.check_game_over():
                solution = getPath(current_node.board, [])
                return solution
            timer = datetime.now()-starttime
            if(generate and (timer.microseconds // 1000) > 500):
                return None
            neighbours = [x for x in current_node.neighbours() if x.board.board not in self.dfs_visited]
            self.stats.operations+=len(neighbours)

            if len(neighbours) == 0:
                current_node.board = current_node.board.parentBoard #BACKTRACK
                continue

            if self.settings.heuristic == 1:
                current_node = min(neighbours, key = lambda x: x.simple_heuristics())
            elif self.settings.heuristic == 2:
                current_node = min(neighbours, key = lambda x: x.admissible_heuristics())
            elif self.settings.heuristic == 3:
                current_node = min(neighbours, key = lambda x: x.heuristics())
        
        return None


    def a_star_search(self, limit = False):
        self.dfs_visited = []
        current = copy.deepcopy(self)
        frontier = [current]
        cost_so_far = {current: 0}
        self.nodes_expanded = 0
        self.stats.start_timer()

        while frontier:
            self.stats.update_timer()

            if (self.stats.ms > 150) and limit:
                return []
                

            if self.settings.heuristic == 1:
                current = min(frontier, key = lambda x: cost_so_far[x] + x.simple_heuristics())
            elif self.settings.heuristic == 2:
                current = min(frontier, key = lambda x: cost_so_far[x] + x.admissible_heuristics())
            elif self.settings.heuristic == 3:
                current = min(frontier, key = lambda x: cost_so_far[x] + x.heuristics())
            
            self.nodes_expanded += 1

            if current.board.check_game_over():
                return getPath(current.board, [])

            neighbours = [x for x in current.neighbours() if x not in self.dfs_visited]
            self.stats.operations += len(neighbours)

            for next in neighbours:
                self.dfs_visited.append(next)
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    frontier.append(next)
            
            frontier.remove(current)

        print("Impossible puzzle!")
        return []

    def get_hint(self):
        self.dfs_visited = []
        current = copy.deepcopy(self)
        frontier = [current]
        cost_so_far = {current: 0}
        self.nodes_expanded = 0

        while frontier:
            current = min(frontier, key = lambda x: cost_so_far[x] + x.heuristics())
            self.nodes_expanded += 1
            if current.board.check_game_over():
                solution = getPath(current.board, [])
                solution.reverse()
                return solution

            neighbours = [copy.deepcopy(current) for i in range(4)]
            neighbour_boards = [neighbours[0].board.setParentBoard(current.board).setMove("up").move_up(), neighbours[1].board.setParentBoard(current.board).setMove("down").move_down(), neighbours[2].board.setParentBoard(current.board).setMove("left").move_left(), neighbours[3].board.setParentBoard(current.board).setMove("right").move_right()]
            neighbours = [neighbours[i] for i in range(len(neighbour_boards)) if neighbour_boards[i] == True]
            neighbours = [x for x in neighbours if x not in self.dfs_visited]
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
        
        factor = self.settings.puzzledb

        empty_board = [[['o','-'] for i in range(3+factor)] for j in range(3+factor)]

        pieces = [['gC','gP'], ['bC','bP'], ['rC','rP'], ['yC','yP'], ['pC','pP']]
        pieces_to_use = []
        npieces = random.randint(factor, factor+1)
        for i in range(npieces):
            pieces_to_use.append(pieces[random.randint(0,4)])

        if factor == 1:
            n_obstacles = random.randint(4, 10)
        elif factor == 2:
            n_obstacles = random.randint(6, 15)
        elif factor == 3:
            n_obstacles = random.randint(9, 18)

        possible_positions = []

        for i in range(len(empty_board)):
            possible_positions.append((0, i))
            possible_positions.append((i, 0))
            possible_positions.append((len(empty_board) - 1, i))
            possible_positions.append((i, len(empty_board) - 1))

        for i in range(n_obstacles):
            (row, col) = (random.randrange(factor+3), random.randrange(factor+3))
            empty_board[row][col] = ['x', 'x']

        while pieces_to_use:
            elem = pieces_to_use.pop(random.randrange(len(pieces_to_use)))
            (row, col) = (0,0)

            found = False
            while not found:
                (row, col) = possible_positions.pop(random.randrange(len(possible_positions)))
                if empty_board[row][col] != ['x', 'x']:
                    found = True

            empty_board[row][col] = elem
        return empty_board

    
    
    def generate_random_puzzle(self):
        board = Board(self.generate_random_board())
        self.board = board
        self.grouped_pieces = self.group_pieces()
        self.permutations = self.get_permutations()
    
        visited = [self.board]

        for i in range(random.randint(self.settings.puzzledb*5,self.settings.puzzledb*7)):
            neighbours = [x for x in self.neighbours() if x.board.board not in visited]
            if len(neighbours) == 0:
                return None

            self.board = neighbours[random.randrange(len(neighbours))].board
            visited.append(self.board.board)
        self.board.centers = []
        self.board.pieces = []
        self.board.retrieveCenters()
        self.board.retrievePieces()
        if(len(self.board.centers)!=len(self.board.pieces)):
            self.generate_random_puzzle()
        else:
            if self.settings.puzzledb != 1:
                piecesDict = {}
                for piece in self.board.pieces:
                    if piece.color not in piecesDict.keys():
                        piecesDict[piece.color] = [piece]
                    else:
                        listPieces = piecesDict[piece.color]
                        listPieces.append(piece)
                        piecesDict[piece.color] = listPieces
                centersDict = {}
                for center in self.board.centers:
                    if center.color not in centersDict.keys():
                        centersDict[center.color] = [center]
                    else:
                        listCenters = centersDict[center.color]
                        listCenters.append(center)
                        centersDict[center.color] = listCenters
                for key in piecesDict.keys():
                    if len(piecesDict[key]) != len(centersDict[key]):
                        self.generate_random_board()
                        break



    def get_possible_board(self):
        found = False
        while not found:
            self.iddfs_solution = None
            self.generate_random_puzzle()
            self.cleanstack()
            solution = self.greedy_search(generate=True)
            if solution != None and solution != []:
                self.board = solution[-1]
                astar = self.a_star_search(limit=True)
                if astar != [] and len(astar) < 4:
                    continue
                found = True
                self.cleanstack()
        return solution

#*  Estimates distance between piece and center
def estimateCenterDifference(piece, center, board):
    pointsX = 0
    pointsY = 0
    if center[0] != piece.x:
        if center[0] == 0 or center[0] == len(board[0]) - 1:
            pointsX += 1
        
        elif center[0] > 0 and board[piece.y][center[0] - 1][0] == "x" and piece.x > center[0]:
            pointsX += 1

        elif center[0] < len(board[0]) - 1 and board[piece.y][center[0] + 1][0] == "x" and piece.x < center[0]:
            pointsX += 1
        
        else: 
            pointsX += 2

    if center[1] != piece.y:
        if center[1] == 0 or center[1] == len(board[0]) - 1:
            pointsY += 1

        elif center[1] > 0 and board[center[1] - 1][piece.x][0] == "x" and piece.y > center[1]:
            pointsY += 1

        elif center[1] < len(board[0]) - 1 and board[center[1] + 1][piece.x][0] == "x" and piece.y < center[1]:
            pointsY += 1
        
        elif pointsX != 2: 
            pointsY += 2
        
        else: 
            pointsY += 1
      
    return pointsX + pointsY

    
def check_obstaclesX(piece, centerX, board):
    iterMin = min(piece.x, centerX)
    iterMax = max(piece.y, centerX)
    for i in range(iterMin, iterMax):
        if board[piece.y][i][0] == "x":  return 3   #*Applies penalization if there is an obstacle in the way
    return 0

def check_obstaclesY(piece, centerY, board):
    iterMin = min(piece.y, centerY)
    iterMax = max(piece.y, centerY)
    for i in range(iterMin, iterMax):
        if board[i][piece.x][0] == "x": return 3    #*Applies penalization if there is an obstacle in the way
    return 0

def getPath(board, listBoards):
    if (board.parentBoard == None):
        return listBoards
    if (board.check_game_over()):
        return getPath(board.parentBoard, [board])
    else:
        listBoards.append(board)
        return getPath(board.parentBoard, listBoards)
    