import pygame
import os
from game import *

pygame.init()

# Game Settings
BACKGRD_COLOR = (176,224,230)
WIDTH, HEIGHT = 1280, 720

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
LOADING = pygame.image.load(os.path.join('assets', 'loadingscreen.jpg'))

# Sprite organizing
SPRITES_IMG = {'bP': BLUE_PIECE_IMG, 'rP': RED_PIECE_IMG, 'gP': GREEN_PIECE_IMG, 'yP': YELLOW_PIECE_IMG, 'pP': PURPLE_PIECE_IMG, 
'bC': BLUE_INSIDE_IMG, 'rC': RED_INSIDE_IMG, 'gC': GREEN_INSIDE_IMG, 'yC': YELLOW_INSIDE_IMG, 'pC': PURPLE_INSIDE_IMG}

BLOCK = pygame.transform.scale(BLOCK_IMG, (110, 110))
GRASS = pygame.transform.scale(GRASS_IMG, (110, 110))
SPRITES = {'x': BLOCK, 'o': GRASS}

for (key,value) in SPRITES_IMG.items():
    SPRITES[key] = pygame.transform.scale(value, (110, 110))

LOADING_SCREEN = pygame.transform.scale(LOADING, (WIDTH, HEIGHT))

# Drawings

def draw_loading():
    SCREEN.blit(LOADING_SCREEN, (0,0))
    font1 = pygame.font.SysFont('Times New Roman', 40)
    font2 = pygame.font.SysFont('Times New Roman', 30)
    text1 = font1.render("Generating a random puzzle...", True, (0,26,51))
    #text1.set_alpha(127)
    text2 = font2.render("This might take a while depending on the difficulty", True, (0,89,179))
    #text2.set_alpha(127)
    text3 = font2.render("Selected Difficulty: " + gamesettings.puzzledbstr, True, (0,89,179))
    text1_rect = text1.get_rect()
    text2_rect = text2.get_rect()
    text3_rect = text3.get_rect()
    text1_rect.center = (WIDTH//2, 80)
    text2_rect.center = (WIDTH//2, 180)
    text3_rect.center = (WIDTH//2, 240)
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(text2, text2_rect)
    SCREEN.blit(text3, text3_rect)
    pygame.display.update()

def draw_board(board):
    multfactor = 7-len(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(2):
                if(board[i][j][k] != '-'):
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
        if(receivedhint == "Calculating..."):
            rec_hint = font.render(receivedhint, True, (0,0,139), (192,192,192))
        elif (receivedhint == "Impossible"):
            rec_hint = font.render("Impossible, ESC to reset", True, (0,0,139), (192,192,192))
        else:
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

def draw_screen(gamestate, hint):
    SCREEN.fill(BACKGRD_COLOR)
    draw_board(gamestate.board.board)
    draw_stats(gamestate.stats, hint)
    pygame.display.update()

def draw_calculating_screen(gamestate):
    titlefont = pygame.font.SysFont('Times New Roman', 35)
    title = titlefont.render("Calculating solution...", True, (0,0,139), BACKGRD_COLOR)
    title_rect = title.get_rect()
    title_rect.center = (WIDTH//2,20)
    SCREEN.fill(BACKGRD_COLOR)
    draw_board(gamestate.board.board)
    SCREEN.blit(title, title_rect)
    pygame.display.update()

def draw_stats_screen(gamestate):
    SCREEN.fill(BACKGRD_COLOR)
    titlefont = pygame.font.SysFont('Times New Roman', 50)
    font = pygame.font.SysFont('Times New Roman', 30)
    title = titlefont.render("Puzzle completed in:", True, (0,0,139), BACKGRD_COLOR)
    moves = font.render("Moves: " + str(gamestate.stats.moves), True, (0,0,255), BACKGRD_COLOR)
    time = font.render("Time: " + gamestate.stats.timestring, True, (0,0,255), BACKGRD_COLOR)
    stgstitle = titlefont.render("Settings Used: ", True, (0,0,139), BACKGRD_COLOR)
    puzzledb = font.render("Puzzle Difficulty: " + gamestate.settings.puzzledbstr, True, (0,0,255), BACKGRD_COLOR)
    puzzlernd = font.render("Random Puzzle Generation: " + gamestate.settings.randomstr, True, (0,0,255), BACKGRD_COLOR)
    itlist = [title, moves, time]
    if gamestate.settings.mode == 2:
        itfactor = 58
        mode = font.render("Game Mode: " + gamestate.settings.modestr, True, (0,0,255), BACKGRD_COLOR)
        search = font.render("Search Method: " + gamestate.settings.searchstr, True, (0,0,255), BACKGRD_COLOR)
        operations = font.render("Number of operations : " + str(gamestate.stats.operations) + " boards", True, (0,0,255), BACKGRD_COLOR)
        itlist += [operations]
        if gamestate.settings.memtrack == 2: 
            memory = font.render("Memory used: " + str(gamestate.stats.memoryused) + " memory blocks", True, (0,0,255), BACKGRD_COLOR)
            itlist += [memory]
        itlist += [stgstitle, puzzledb, puzzlernd, mode, search]
        if gamestate.settings.search in [4,5]:
            heuristic = font.render("Heuristic: " + gamestate.settings.heuristicstr, True, (0,0,255), BACKGRD_COLOR)
            itlist += [heuristic]
    elif gamestate.settings.mode == 1:
        itfactor = 100
        itlist += [stgstitle, puzzledb, puzzlernd]

    it = 0
    for text in itlist:
        it+=1
        rect = text.get_rect()
        rect.center = (WIDTH//2, itfactor*it)
        SCREEN.blit(text, rect)
    smallf = pygame.font.SysFont('Times New Roman', 20)
    smallt = smallf.render("Press SPACE or ESC to continue to the main menu", True, (0,0,255), BACKGRD_COLOR)
    smallt_rect = smallt.get_rect()
    smallt_rect.center = (WIDTH//2, HEIGHT-20)
    SCREEN.blit(smallt, smallt_rect)
    pygame.display.update()

def draw_replay(pathlist, timestr):
    for i in range(len(pathlist)):
        pygame.event.pump()
        SCREEN.fill(BACKGRD_COLOR)
        draw_board(pathlist[-(i+1)].board)
        draw_replay_stats(timestr, i+1)
        pygame.display.update()
        pygame.time.wait(500)
