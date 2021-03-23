import os
import pygame
import pygame_menu as menu
from settings import Settings
from game import Game
from AI import *

pygame.init()

# Game Settings
BACKGRD_COLOR = (176,224,230)
WIDTH, HEIGHT = 1280, 720
BOARDSIZE = {"small":4, "medium":5, "big":6}

# Window setup
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Match the Tiles")

# Sprite loading
BLOCK_IMG = pygame.image.load(os.path.join('assets', 'block.png'))
GRASS_IMG = pygame.image.load(os.path.join('assets', 'grass.png'))
BLUE_PIECE_IMG = pygame.image.load(os.path.join('assets', 'bluepiece.png'))
RED_PIECE_IMG = pygame.image.load(os.path.join('assets', 'redpiece.png'))
GREEN_PIECE_IMG = pygame.image.load(os.path.join('assets', 'greenpiece.png'))
YELLOW_PIECE_IMG = pygame.image.load(os.path.join('assets', 'yellowpiece.png'))
PURPLE_PIECE_IMG = pygame.image.load(os.path.join('assets', 'purplepiece.png'))
BLUE_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'blueinside.png'))
RED_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'redinside.png'))
GREEN_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'greeninside.png'))
YELLOW_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'yellowinside.png'))
PURPLE_INSIDE_IMG = pygame.image.load(os.path.join('assets', 'purpleinside.png'))

# Sprite organizing
SPRITES_IMG = {'bPiece': BLUE_PIECE_IMG, 'rPiece': RED_PIECE_IMG, 'gPiece': GREEN_PIECE_IMG, 'yPiece': YELLOW_PIECE_IMG, 'pPiece': PURPLE_PIECE_IMG, 
'bCenter': BLUE_INSIDE_IMG, 'rCenter': RED_INSIDE_IMG, 'gCenter': GREEN_INSIDE_IMG, 'yCenter': YELLOW_INSIDE_IMG, 'pCenter': PURPLE_INSIDE_IMG}

BLOCK = pygame.transform.scale(BLOCK_IMG, (110, 110))
GRASS = pygame.transform.scale(GRASS_IMG, (110, 110))
SPRITES = {'block': BLOCK, 'grass': GRASS}

for (key,value) in SPRITES_IMG.items():
    SPRITES[key] = pygame.transform.scale(value, (110, 110))

def draw_board(board):
    multfactor = 7-len(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(2):
                if(board[i][j][k] != 'empty'):
                    SCREEN.blit(SPRITES[board[i][j][k]], (250+multfactor*50+110*(j),45*multfactor+110*(i)))


def draw_stats(stats, receivedhint):
    font = pygame.font.SysFont('Times New Roman', 25)
    timer = font.render("Timer: " + stats.timestring, True, (0,0,139), BACKGRD_COLOR)
    timerRect = timer.get_rect()
    timerRect.topleft = (5, 50)
    SCREEN.blit(timer, timerRect)
    moves = font.render("Moves: " + str(stats.moves), True, (0,0,139), BACKGRD_COLOR)
    movesRect = moves.get_rect()
    movesRect.topleft = (5, 100)
    SCREEN.blit(moves, movesRect)
    hint = font.render("Press H to get a hint", True, (0,0,139), (192,192,192))
    hintRect = hint.get_rect()
    hintRect.topleft = (5, 200)
    SCREEN.blit(hint, hintRect)
    if(receivedhint != "None"):
        rec_hint = font.render("Try moving " + receivedhint + "!", True, (0,0,139), (192,192,192))
        rec_hintRect = rec_hint.get_rect()
        rec_hintRect.topleft = (5,250)
        SCREEN.blit(rec_hint, rec_hintRect)

def draw_replay_stats(timeused, moves):
    titlefont = pygame.font.SysFont('Times New Roman', 35)
    normalfont = pygame.font.SysFont('Times New Roman', 25)
    replay = titlefont.render("Move Replay", True, (0,0,139), BACKGRD_COLOR)
    replay_rect = replay.get_rect()
    replay_rect.center = (WIDTH//2,20)
    timetitle = titlefont.render("Time used:", True, (0,0,139), BACKGRD_COLOR)
    timer = normalfont.render(timeused, True, (0,0,139), BACKGRD_COLOR)
    timetitle_rect = timetitle.get_rect()
    timer_rect = timer.get_rect()
    timetitle_rect.topleft = (5,50)
    timer_rect.topleft = (10, 100)
    movetext = normalfont.render("Moves: " + str(moves), True, (0,0,139), BACKGRD_COLOR)
    movetext_rect = movetext.get_rect()
    movetext_rect.topleft = (10,150)
    SCREEN.blit(replay, replay_rect)
    SCREEN.blit(timetitle, timetitle_rect)
    SCREEN.blit(timer, timer_rect)
    SCREEN.blit(movetext, movetext_rect)

# Screen drawing and updating

def draw_screen(gamestate, hint):
    SCREEN.fill(BACKGRD_COLOR)
    draw_board(gamestate.board.board)
    draw_stats(gamestate.stats, hint)
    pygame.display.update()

def draw_stats_screen(gamestate):
    SCREEN.fill(BACKGRD_COLOR)
    titlefont = pygame.font.SysFont('Times New Roman', 50)
    font = pygame.font.SysFont('Times New Roman', 30)
    title = titlefont.render("Puzzle completed in:", True, (0,0,139), BACKGRD_COLOR)
    moves = font.render("Moves: " + str(gamestate.stats.moves), True, (0,0,255), BACKGRD_COLOR)
    time = font.render("Time: " + gamestate.stats.timestring, True, (0,0,255), BACKGRD_COLOR)
    stgstitle = titlefont.render("Settings Used: ", True, (0,0,139), BACKGRD_COLOR)
    mode = font.render("Game Mode: " + gamestate.settings.modestr, True, (0,0,255), BACKGRD_COLOR)
    search = font.render("Search Method: " + gamestate.settings.searchstr, True, (0,0,255), BACKGRD_COLOR)
    heuristic = font.render("Heuristic: " + gamestate.settings.heuristicstr, True, (0,0,255), BACKGRD_COLOR)
    puzzledb = font.render("Puzzle Database: " + gamestate.settings.puzzledbstr, True, (0,0,255), BACKGRD_COLOR)
    it = 0
    itlist = [title, moves, time, stgstitle, mode, search, puzzledb]
    if gamestate.settings.search == 5 or gamestate.settings.search == 6: itlist.append(heuristic)
    for text in itlist:
        it+=1
        rect = text.get_rect()
        rect.center = (WIDTH//2, 75*it)
        SCREEN.blit(text, rect)
    smallf = pygame.font.SysFont('Times New Roman', 20)
    smallt = smallf.render("Press SPACE or ESC to continue to the main menu", True, (0,0,255), BACKGRD_COLOR)
    smallt_rect = smallt.get_rect()
    smallt_rect.center = (WIDTH//2, HEIGHT-20)
    SCREEN.blit(smallt, smallt_rect)
    pygame.display.update()


def set_mode(value, mode):
    #print("Not yet implemented")
    gamesettings.mode = mode
    gamesettings.updatestrs()

def set_search(value, mode):
    #print("Not yet implemented")
    gamesettings.search = mode
    gamesettings.updatestrs()

def set_heuristic(value, mode):
    #print("Not yet implemented")
    gamesettings.heuristic = mode
    gamesettings.updatestrs()

def set_puzzle_selection(value, mode):
    #print("Not yet implemented")
    gamesettings.puzzledb = mode
    gamesettings.updatestrs()


def game_loop():
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


def draw_replay(pathlist, timestr):
    for i in range(len(pathlist)):
        SCREEN.fill(BACKGRD_COLOR)
        draw_replay_stats(timestr, i)
        draw_board(pathlist[-(i+1)].board)
        pygame.display.update()
        pygame.time.wait(500)

def ai_loop(GameState):
    GameState.stats.start_timer()
    pathlist = []
    if GameState.settings.search == 1:
        pathlist = GameState.bfs(GameState)

    elif GameState.settings.search == 2:
        GameState.dfs(GameState)
        pathlist = GameState.dfs_result
        GameState.stats.moves = len(pathlist) - 1
        print(pathlist)

    elif GameState.settings.search == 3:
        print("Not yet implemented")

    elif GameState.settings.search == 4:
        print("Not yet implemented")

    elif GameState.settings.search == 5:
        if GameState.settings.heuristic == 1:
            print("Not yet implemented")
        elif GameState.settings.heuristic == 2:
            print("Not yet implemented")

    elif GameState.settings.search == 6:
        if GameState.settings.heuristic == 1:
            print("Not yet implemented")
        elif GameState.settings.heuristic == 2:
            print("Not yet implemented")
    if(len(pathlist) != 0):
        GameState.board = pathlist[0]
        GameState.stats.update_timer()
        draw_replay(pathlist, GameState.stats.timestring)
    return GameState.board.check_game_over()

def player_loop(GameState):
    previouskey = "None"
    hint = "None"
    running = True
    GameState.stats.start_timer()
    while running:
        gameover = GameState.board.check_game_over()
        running = not gameover
        GameState.stats.update_timer()
        if(pygame.key.get_pressed()[pygame.K_h]):
            hint = "Not yet implemented" #get_hint(GameState.settings): (...) return up; down; right; left
        draw_screen(GameState, hint)
        previouskey2 = handle_movement(GameState, previouskey)
        if(previouskey2 != previouskey): hint = "None"
        previouskey = previouskey2
        if(pygame.key.get_pressed()[pygame.K_ESCAPE]): running = False # missing pause menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    return GameState.board.check_game_over()


main_menu = menu.Menu('Match The Tiles', WIDTH, HEIGHT, theme=menu.themes.THEME_BLUE)
main_menu.add.button("Start game", game_loop)
main_menu.add.selector("Mode: ", [('Player vs Puzzle', 1), ('AI vs Puzzle', 2)], onchange=set_mode)
main_menu.add.selector("Search Method: ", [('Breadth-First Search', 1), ('Depth-First Search',2), ('Iterative Deepening',3), ('Uniform Cost',4), ('Greedy Search',5), ('A* Algorithm',6)], onchange=set_search)
main_menu.add.selector("Heuristic: ", [('Simple Algorithm', 1), ('Complex Algorithm',2)], onchange=set_heuristic)
main_menu.add.selector("Puzzle Database: ", [('Easy', 1), ('Medium', 2), ('Hard', 3), ('Random Generation', 4)], onchange=set_puzzle_selection)
main_menu.add.button("Quit Game", menu.events.EXIT)

def main():
    running = True
    global gamesettings
    gamesettings = Settings(1,1,1,1)
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        if main_menu.is_enabled():
            main_menu.update(events)
            main_menu.draw(SCREEN)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()