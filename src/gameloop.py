import tracemalloc
from drawings import *

# Game Loops

def game_loop():
    if gamesettings.randompz == 2:
        draw_loading()
    GameState = Game(gamesettings)
    if GameState.settings.mode == 1:
        puzzle_finished = player_loop(GameState)
    elif GameState.settings.mode == 2:
        puzzle_finished = ai_loop(GameState)
    if puzzle_finished:
        while True:
            draw_stats_screen(GameState)
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_ESCAPE] or keys[pygame.K_SPACE]): break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

def ai_loop(GameState):
    draw_calculating_screen(GameState)
    GameState.cleanstack()
    GameState.stats.start_timer()
    pathlist = []
    if GameState.settings.search == 1:
        if GameState.settings.memtrack == 2:
            tracemalloc.start()
        
        pathlist = GameState.get_possible_board()#GameState.bfs(GameState)
        draw_board(GameState.board.board)
        pygame.time.wait(2500)
        if GameState.settings.memtrack == 2:
            GameState.stats.memoryused = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

    elif GameState.settings.search == 2:
        if GameState.settings.memtrack == 2:
            tracemalloc.start()
        GameState.dfs(GameState)
        if GameState.settings.memtrack == 2:
            GameState.stats.memoryused = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
        pathlist = GameState.dfs_result
        #GameState.stats.moves = len(pathlist) - 1
        GameState.cleanstack()

    elif GameState.settings.search == 3:
        if GameState.settings.memtrack == 2:
            tracemalloc.start()
        pathlist = GameState.iterative_deepening(GameState)
        if GameState.settings.memtrack == 2:
            GameState.stats.memoryused = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
        #GameState.stats.moves = len(pathlist) - 1
        GameState.cleanstack()

    elif GameState.settings.search == 4:
        if GameState.settings.memtrack == 2:
            tracemalloc.start()
        pathlist = GameState.greedy_search()

        if GameState.settings.memtrack == 2:
            GameState.stats.memoryused = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            
        #GameState.stats.moves = len(pathlist)
        GameState.cleanstack()

    elif GameState.settings.search == 5:
        if GameState.settings.memtrack == 2:
            tracemalloc.start()

        pathlist = GameState.a_star_search()

        if GameState.settings.memtrack == 2:
            GameState.stats.memoryused = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
        
        #GameState.stats.moves = len(pathlist)
        GameState.cleanstack()
    
    #print(pathlist)
    if(pathlist != [] and pathlist != None and pathlist[-1].parentBoard == None):
        pathlist.remove(pathlist[-1])
    
    GameState.stats.moves = len(pathlist)
    if(len(pathlist) != 0):
        GameState.board = pathlist[0]
        GameState.stats.update_timer()
        draw_replay(pathlist, GameState.stats.timestring)
    else: print("Solution not found!")
    return GameState.board.check_game_over()

def player_loop(GameState):
    previouskey = "None"
    hint = "None"
    running = True
    notfound = True
    solution = []
    GameState.stats.start_timer()
    while running:
        gameover = GameState.board.check_game_over()
        GameState.stats.update_timer()
        if gameover: break
        if(pygame.key.get_pressed()[pygame.K_h]):
            for i in range(len(solution)):
                if GameState.board.board == solution[i].board:
                    hint = solution[i+1].move
                    notfound = False
            if(notfound):
                draw_screen(GameState, "Calculating...")
                solution = GameState.get_hint()
                GameState.cleanstack()
                if solution == []:
                    hint = "Impossible"
                else:
                    hint = solution[0].move
            notfound = True
        draw_screen(GameState, hint)
        previouskey2 = handle_movement(GameState, previouskey)
        if(previouskey2 != previouskey): hint = "None"
        previouskey = previouskey2
        if(pygame.key.get_pressed()[pygame.K_ESCAPE]): running = False # missing pause menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    return gameover


# Player Movement

def handle_movement(gamestate, previouskey):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and previouskey!='up':
        if gamestate.board.move_up(): gamestate.stats.moves += 1
        # gamestate.getStackedCenters()
        gamestate.heuristics()
        return 'up'
    
    elif keys_pressed[pygame.K_DOWN] and previouskey!='down':
        if gamestate.board.move_down(): gamestate.stats.moves += 1
        # gamestate.getStackedCenters()
        gamestate.heuristics()
        return 'down'
    
    elif keys_pressed[pygame.K_LEFT] and previouskey!='left':
        if gamestate.board.move_left(): gamestate.stats.moves += 1
        #gamestate.getStackedCenters()
        gamestate.heuristics()
        return 'left'
    
    elif keys_pressed[pygame.K_RIGHT] and previouskey!='right':
        if gamestate.board.move_right(): gamestate.stats.moves += 1
        # gamestate.getStackedCenters()
        gamestate.heuristics()
        return 'right'
    
    else: return previouskey
