import sys

def number_is_valid(grid, number, x, y):

    for i in range(9):
        if grid[x][i] == number:
            return (False)
        if (grid[i][y] == number):
            return (False)
    if (x in [0,1,2]): start_x = 0
    elif (x in [3,4,5]): start_x = 3
    else: start_x = 6

    if (y in [0,1,2]): start_y = 0
    elif (y in [3,4,5]): start_y = 3
    else: start_y = 6

    for i in range(3):
        for j in range(3):
            if (grid[start_x + i][start_y + j] == number):
                return (False)
    return (True)


def make_grid(grid_file):

    with open(grid_file, 'r') as file:
        s = file.read()
        # put grid in nested list
        grid = [ [elem for elem in line.split(' ')] for line in s.split('\n')]
        return (grid)

def solver(grid, x, y):
    
    if (x == 9):
        return True
    if (y == 9):
        return (solver(grid, x + 1, 0))
    if (grid[x][y] != '0'):
        return (solver(grid, x, y + 1))
    for i in range(1, 10):
        n = str(i)
        if (number_is_valid(grid, n, x, y)):
            grid[x][y] = n
            if (solver(grid, x, y + 1)):
                return True
    grid[x][y] = '0'
    return False


def main(grid_file):

    grid = make_grid(grid_file)
    if (solver(grid, 0, 0)):
        for elem in grid:
            print(elem)
    else:
        print('No solutions exist for that grid')


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('1 argument required: path to sudoku grid file')
    else:
        main(sys.argv[1])