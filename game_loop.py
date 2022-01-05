import sys
import pygame
from game.Button import Button
import utils.solver as solver
import copy

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
    K_RETURN,
    K_BACKSPACE,
    K_SPACE,
    QUIT,
    K_s
)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

def create_buttons(screen, grid):

    buttons = []
    fake_buttons = []
    x = 21
    for i in range(9):
        y = 18
        for j in range(9):
            if (j % 3 == 0):
                y += 3
            if (grid[j][i] == '0'):
                buttons.append( Button((x, y), coordinates=(j, i)) )
            else:
                fake_buttons.append( Button((x, y), grid[j][i], pygame.Color("Grey")) )
            y += 50
        if ((i+1) % 3 == 0):
            x += 3
        x += 50

    for fake_button in fake_buttons:
        fake_button.show(screen, update=False)
    for button in buttons:
        button.show(screen, update=False)
    pygame.display.update()
    return (buttons)

def init_screen():

    pygame.init()
    # for performance, pygame doesn't register mouse motion as an event
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(pygame.Color("White"))
    pygame.draw.rect(screen, pygame.Color("Black"), pygame.Rect(16, 16, 464, 464), border_radius=3)
    print_message(screen, 'Let the game begin')
    pygame.display.flip()
    return (screen)

def print_message(screen, message):

    font = pygame.font.SysFont("Arial", 35)
    text = font.render(message, 1, pygame.Color("Black"))
    size = text.get_size()
    surface = pygame.Surface((400, 100))
    surface.fill(pygame.Color("White"))
    screen.blit(surface, (50, 500))
    pygame.draw.rect(surface, pygame.Color("Orange"), pygame.Rect(0, 0, size[0], size[1]))
    pygame.draw.rect(surface, pygame.Color("White"), pygame.Rect(5, 5, size[0] - 10, size[1] - 10))

    screen.blit(surface, (SCREEN_WIDTH/2 - size[0]/2, 510))
    screen.blit(text, (SCREEN_WIDTH/2 - size[0]/2, 510))
    pygame.display.update()

def main(grid_file):
    
    screen = init_screen()
    keys_possible = {K_BACKSPACE: '0', K_0: '0', K_1: '1', K_2: '2', K_3: '3',
                K_4: '4', K_5: '5', K_6: '6', K_7: '7', K_8: '8', K_9: '9'}
    original_grid = solver.make_grid(grid_file)
    if (solver.check_grid_format(original_grid) is False):
        print('\nPlease use a well formatted map')
        print('(9x9 grid, separated by spaces with only numbers between 0 and 9)')
        exit()
    solver.print_instructions_cli()
    grid = copy.deepcopy(original_grid)
    buttons = create_buttons(screen, grid)
    running = True
    current_button = None

    while running:

        event = pygame.event.wait()
        if event.type == QUIT:
            running = False

        # event to select a tile with the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.check_click(screen) == True:
                    if (current_button is not None and current_button != button):
                        current_button.draw_borders(screen, pygame.Color("White"))
                    current_button = button

        if event.type == pygame.KEYDOWN:
            # ESC quits the game
            if event.key == K_ESCAPE:
                running = False

            # enter (return) checks if the player's solution is valid
            if event.key == K_RETURN:
                if (solver.grid_is_valid(grid) == True):
                    print_message(screen, "Success")
                else:
                    print_message(screen, "Not quite right!")

            # space solves the sudoku automatically
            if event.key == K_SPACE or event.key == K_s:
                if (not solver.precheck_grid(original_grid)):
                    print_message(screen, 'No solution exists')
                else:
                    if (event.key == K_SPACE):
                        ret = solver.solver(original_grid, 0, 0, buttons, screen, visu=True)
                    elif (event.key == K_s):
                        ret = solver.solver(original_grid, 0, 0, buttons, screen, visu=False)
                    if (ret == False):
                        print_message(screen, 'No solution exists')
                    elif (ret == 2):
                        running = False
                    else:
                        print_message(screen, 'Solved')
                    pygame.display.update()

            # number keys to fill the tiles
            if event.key in keys_possible.keys() and current_button is not None:
                number_pressed = keys_possible[event.key]
                current_button.change_text(number_pressed)
                current_button.show(screen)
                grid[current_button.coord[0]][current_button.coord[1]] = number_pressed

        # pygame.display.flip()
            
    pygame.quit()

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('\nOne argument required: location to grid file')
    else:
        main(sys.argv[1])