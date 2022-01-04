import pygame
from Button import Button

from pygame.locals import (
    K_0,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_ESCAPE,
    QUIT
)

def create_buttons(screen):

    buttons = []
    x = 21
    for i in range(1, 10):
        y = 18
        for j in range(9):
            if (j % 3 == 0):
                y += 3
            buttons.append( Button((x, y)) )
            y += 50
        if (i % 3 == 0):
            x += 3
        x += 50

    for button in buttons:
        button.show(screen)
    return (buttons)

def init_screen():

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill(pygame.Color("White"))
    pygame.draw.rect(screen, pygame.Color("Black"), pygame.Rect(16, 16, 464, 464), border_radius=3)
    pygame.display.flip()
    return (screen)

def main():
    
    screen = init_screen()
    keys_possible = {K_0: '', K_1: '1', K_2: '2', K_3: '3', K_4: '4', K_5: '5',
                K_6: '6', K_7: '7', K_8: '8', K_9: '9'}
    buttons = create_buttons(screen)
    running = True
    current_button = None

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.check_click(screen) == True:
                        if (current_button is not None):
                            current_button.draw_borders(screen, pygame.Color("White"))
                        current_button = button

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key in keys_possible.keys() and current_button is not None:
                    current_button.change_text(keys_possible[event.key])
                    current_button.show(screen)

        pygame.display.flip()
            
    pygame.quit()

if __name__ == '__main__':
    main()