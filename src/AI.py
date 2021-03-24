import pygame
from board import Board  

def handle_movement(gamestate, previouskey):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and previouskey!='up':
        if gamestate.board.move_up():
            gamestate.stats.moves += 1
            #print(gamestate.heuristics())
        return 'up'
    
    elif keys_pressed[pygame.K_DOWN] and previouskey!='down':
        if gamestate.board.move_down(): 
            gamestate.stats.moves += 1
            #print(gamestate.heuristics())
        return 'down'
    
    elif keys_pressed[pygame.K_LEFT] and previouskey!='left':
        if gamestate.board.move_left(): 
            gamestate.stats.moves += 1
            #print(gamestate.heuristics())
        return 'left'
    
    elif keys_pressed[pygame.K_RIGHT] and previouskey!='right':
        if gamestate.board.move_right(): 
            gamestate.stats.moves += 1
            #print(gamestate.heuristics())
        return 'right'
    
    else: return previouskey
