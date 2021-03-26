import pygame_menu as menu
from gameloop import *

# Settings update

def set_mode(value, mode):
    gamesettings.mode = mode
    gamesettings.updatestrs()
    if(mode == 2):
        main_menu.remove_widget(quitbtn)
        main_menu.add.generic_widget(memorybtn)
        main_menu.add.generic_widget(searchbtn)
        if gamesettings.search in [4,5]:
            main_menu.add.generic_widget(heuristicbtn)
        main_menu.add.generic_widget(quitbtn)
    elif(mode == 1):
        main_menu.remove_widget(quitbtn)
        main_menu.remove_widget(memorybtn)
        main_menu.remove_widget(searchbtn)
        if gamesettings.search in [4,5]:
            main_menu.remove_widget(heuristicbtn)
        main_menu.add.generic_widget(quitbtn)

def set_search(value, mode):
    if gamesettings.search in [4,5] and mode not in [4,5]:
        main_menu.remove_widget(quitbtn)
        main_menu.remove_widget(heuristicbtn)
        main_menu.add.generic_widget(quitbtn)
    elif gamesettings.search not in [4,5] and mode in [4,5]: 
        main_menu.remove_widget(quitbtn)
        main_menu.add.generic_widget(heuristicbtn)
        main_menu.add.generic_widget(quitbtn)
    gamesettings.search = mode
    gamesettings.updatestrs()
        
def set_heuristic(value, mode):
    gamesettings.heuristic = mode
    gamesettings.updatestrs()

def set_puzzle_selection(value, mode):
    gamesettings.puzzledb = mode
    gamesettings.updatestrs()

def set_random_puzzle(value, mode):
    gamesettings.randompz = mode
    gamesettings.updatestrs()

def set_memtrack(value, mode):
    gamesettings.memtrack = mode
    gamesettings.updatestrs()


# Menu handling

main_menu = menu.Menu('Match The Tiles', WIDTH, HEIGHT, theme=menu.themes.THEME_BLUE)
main_menu.add.button("Start game", game_loop)
main_menu.add.selector("Puzzle Difficulty: ", [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_puzzle_selection)
main_menu.add.selector("Random Puzzle Generation: ", [('Off', 1), ('On', 2)], onchange=set_random_puzzle)
main_menu.add.selector("Mode: ", [('Player vs Puzzle', 1), ('AI vs Puzzle', 2)], onchange=set_mode)
memorybtn = main_menu.add.selector("Track memory usage: ", [('Off', 1), ('On', 2)], onchange=set_memtrack)
searchbtn = main_menu.add.selector("Search Method: ", [('Breadth-First Search', 1), ('Depth-First Search',2), ('Iterative Deepening',3), ('Greedy Search',4), ('A* Algorithm',5)], onchange=set_search)
heuristicbtn = main_menu.add.selector("Heuristic: ", [('Simple Algorithm', 1), ('Complex Algorithm',2)], onchange=set_heuristic)
quitbtn = main_menu.add.button("Quit Game", menu.events.EXIT)
main_menu.remove_widget(memorybtn)
main_menu.remove_widget(searchbtn)
main_menu.remove_widget(heuristicbtn)
