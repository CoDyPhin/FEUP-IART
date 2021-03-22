import os
import pygame
import pygame_menu as menu
from settings import Settings
from game import Game
from AI import *

pygame.init()

# Game Settings
BACKGRD_COLOR = (176,224,230)
FPS = 60
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
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(2):
                if(board[i][j][k] != 'empty'):
                    SCREEN.blit(SPRITES[board[i][j][k]], (350+110*(j),100+110*(i)))


def draw_stats(stats, receivedhint):
    font = pygame.font.SysFont('Times New Roman', 25)
    timer = font.render("Timer: " + stats.timestring, False, (0,0,139), BACKGRD_COLOR)
    timerRect = timer.get_rect()
    timerRect.topleft = (5, 50)
    SCREEN.blit(timer, timerRect)
    moves = font.render("Moves: " + str(stats.moves), False, (0,0,139), BACKGRD_COLOR)
    movesRect = moves.get_rect()
    movesRect.topleft = (5, 100)
    SCREEN.blit(moves, movesRect)
    hint = font.render("Press H to get a hint", True, (0,0,139), (192,192,192))
    hintRect = hint.get_rect()
    hintRect.topleft = (5, 200)
    SCREEN.blit(hint, hintRect)
    if(receivedhint != "None"):
        rec_hint = font.render("Try moving " + receivedhint + "!", False, (0,0,139), (192,192,192))
        rec_hintRect = rec_hint.get_rect()
        rec_hintRect.topleft = (5,250)
        SCREEN.blit(rec_hint, rec_hintRect)


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
    moves = font.render("Moves: " + str(gamestate.stats.moves), False, (0,0,255), BACKGRD_COLOR)
    time = font.render("Time: " + gamestate.stats.timestring, False, (0,0,255), BACKGRD_COLOR)
    stgstitle = titlefont.render("Settings Used: ", True, (0,0,139), BACKGRD_COLOR)
    mode = font.render("Game Mode: " + gamestate.settings.modestr, False, (0,0,255), BACKGRD_COLOR)
    search = font.render("Search Method: " + gamestate.settings.searchstr, False, (0,0,255), BACKGRD_COLOR)
    heuristic = font.render("Heuristic Algorithm: " + gamestate.settings.heuristicstr, False, (0,0,255), BACKGRD_COLOR)
    puzzledb = font.render("Puzzle Database: " + gamestate.settings.puzzledbstr, False, (0,0,255), BACKGRD_COLOR)
    it = 0
    for text in [title, moves, time, stgstitle, mode, search, heuristic, puzzledb]:
        it+=1
        rect = text.get_rect()
        rect.center = (WIDTH//2, 75*it)
        SCREEN.blit(text, rect)
    smallf = pygame.font.SysFont('Times New Roman', 20)
    smallt = smallf.render("Press SPACE or ESC to continue to the main menu", False, (0,0,255), BACKGRD_COLOR)
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
    clock = pygame.time.Clock()
    previouskey = "None"
    hint = "None"
    running = True
    GameState.stats.start_timer()
    GameState.board = GameState.bfs(GameState)

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
    if gameover:
        while True:
            draw_stats_screen(GameState)
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_ESCAPE] or keys[pygame.K_SPACE]): break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


main_menu = menu.Menu('Match The Tiles', WIDTH, HEIGHT, theme=menu.themes.THEME_BLUE)
main_menu.add.button("Start game", game_loop)
main_menu.add.selector("Mode: ", [('Player vs Puzzle', 1), ('AI vs Puzzle', 2)], onchange=set_mode)
main_menu.add.selector("Search Method: ", [('Breadth-First Search', 1), ('Depth-First Search',2), ('Iterative Deepening',3), ('Uniform Cost',4)], onchange=set_search)
main_menu.add.selector("Heuristic Algorithm: ", [('Greedy Search',1), ('A* Algorithm', 2)], onchange=set_heuristic)
main_menu.add.selector("Puzzle Database: ", [('Easy', 1), ('Medium', 2), ('Hard', 3), ('Random Generation', 4)], onchange=set_puzzle_selection)
main_menu.add.button("Quit Game", menu.events.EXIT)

def main():
    clock = pygame.time.Clock()
    previouskey = "None"
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