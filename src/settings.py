class Settings:
    def __init__(self, mode, search, memtrack, heuristic, puzzledb, randompz):
        self.mode = mode
        self.search = search
        self.heuristic = heuristic
        self.puzzledb = puzzledb
        self.randompz = randompz
        self.memtrack = memtrack
        self.modestr = ""
        self.searchstr = ""
        self.heuristicstr = ""
        self.puzzledbstr = ""
        self.randomstr = ""
        self.memtrackstr = ""
        self.updatestrs()

    def updatestrs(self):
        modedic = {1: 'Player vs Puzzle', 2: 'AI vs Puzzle'}
        searchdic = {1: 'Breadth-First Search', 2: 'Depth-First Search', 3: 'Iterative Deepening', 4:"Greedy Search", 5: "A* Algorithm"}
        heuristicdic = {1: 'Simple Algorithm', 2: 'Complex Algorithm', 3: 'Fast Algorithm'}
        puzzledbdic = {1: 'Easy', 2: 'Medium', 3: 'Hard', 4: 'Random Generation'}
        randomdic = {1: 'Off', 2: 'On'}
        self.modestr = modedic[self.mode]
        self.searchstr = searchdic[self.search]
        self.heuristicstr = heuristicdic[self.heuristic]
        self.puzzledbstr = puzzledbdic[self.puzzledb]
        self.randomstr = randomdic[self.randompz]
        self.memtrackstr = randomdic[self.memtrack]
