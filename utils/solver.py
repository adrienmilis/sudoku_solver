import sys
import pygame

def print_instructions_cli():
    print()
    print('Welcome to this sudoku auto-solver ! Feel free to first play around')
    print('\t- The ESC key exits')
    print('\t- The RETURN key checks if the grid is a valid solution')
    print('\t- The SPACE key solves the sudoku with visualization of the backtracking algorithm')
    print('\t- The S key solves the sudoku without visualization')
    print('Enjoy!')

def grid_is_valid(grid):

    for i in range(9):
        for j in range(9):
            if (not number_is_valid(grid, grid[i][j], i, j)):
                print(i, j)
                return (False)
    return (True)

def number_is_valid(grid, number, x, y):

    for i in range(9):
        if grid[x][i] == number and i != y:
            return (False)
        if (grid[i][y] == number) and i != x:
            return (False)
    if (x in [0,1,2]): start_x = 0
    elif (x in [3,4,5]): start_x = 3
    else: start_x = 6

    if (y in [0,1,2]): start_y = 0
    elif (y in [3,4,5]): start_y = 3
    else: start_y = 6

    for i in range(3):
        for j in range(3):
            if (start_x + i == x and start_y + j == y):
                continue
            if (grid[start_x + i][start_y + j] == number):
                return (False)
    return (True)


def make_grid(grid_file):

    with open(grid_file, 'r') as file:
        s = file.read()
        # put grid in nested list
        grid = [ [elem for elem in line.split(' ')] for line in s.split('\n')]
        return (grid)

def solver(grid, x, y, buttons, screen, visu=False):
        
    # check events in case user wants to quit program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 2
    curr_button = None
    # big loop, that's a problem
    for button in buttons:
        if button.coord == (x, y):
            curr_button = button
    if (x == 9):
        return True
    if (y == 9):
        return (solver(grid, x + 1, 0, buttons, screen, visu))
    # button is not unmutable
    if (curr_button is None):
        return (solver(grid, x, y + 1, buttons, screen, visu))
    for i in range(1, 10):
        n = str(i)
        if (number_is_valid(grid, n, x, y)):
            grid[x][y] = n
            if (curr_button is not None):
                curr_button.change_text(n)
                curr_button.show(screen, update=visu, border_color=pygame.Color("Green"))

            ret = solver(grid, x, y + 1, buttons, screen, visu)
            if (ret == 2):
                return (2)
            if (ret):
                return True
    grid[x][y] = '0'
    if (curr_button is not None):
        curr_button.change_text('0')
        curr_button.show(screen, update=visu, border_color=pygame.Color("Red"))
    return False

def old_solver(grid, x, y):
    
    if (x == 9):
        return True
    if (y == 9):
        return (old_solver(grid, x + 1, 0))
    if (grid[x][y] != '0'):
        return (old_solver(grid, x, y + 1))
    for i in range(1, 10):
        n = str(i)
        if (number_is_valid(grid, n, x, y)):
            grid[x][y] = n
            if (old_solver(grid, x, y + 1)):
                return True
    grid[x][y] = '0'
    return False

def precheck_grid(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j] != '0':
                if (not number_is_valid(grid, grid[i][j], i, j)):
                    return False
    return True

def check_grid_format(grid):

    if (len(grid) != 9):
        return False
    for line in grid:
        if len(line) != 9:
            return False
        for elem in line:
            if not elem.isnumeric():
                return False
    return True
    

def main(grid_file):

    grid = make_grid(grid_file)
    if (not precheck_grid(grid) or not old_solver(grid, 0, 0)):
        print('No solutions exist for that grid')
    else:
        for elem in grid:
            print(elem)


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('1 argument required: path to sudoku grid file')
    else:
        main(sys.argv[1])