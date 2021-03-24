from menus import *

def main():
    running = True
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