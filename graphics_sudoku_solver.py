# run the program
# a sudoku board will appear
# select the grid u wanna edit
# and press the number from the keyboard
# press all the numbers in the same way
# when done, press the enter button
# it's answer will be printed in the board itself

import pygame
import sudoku_solver

pygame.init()

SCREEN_WIDTH = 365
SCREEN_HEIGHT = 365

WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [0, 255, 0]
GREEN = [0, 0, 255]
BLACK = [0, 0, 0]

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW.fill(WHITE)

DISTANCE_BETWEEN_GRIDS = 40

THICK_LINES = 7
THIN_LINES = 1
LINE_LENGTH = 360

# board = [[0 for i in range(9)] for j in range(9)]

board = [[0, 0, 0, 0, 8, 0, 0, 0, 0],
         [8, 0, 9, 0, 7, 1, 0, 2, 0],
         [4, 0, 3, 5, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 0, 7],
         [0, 0, 2, 0, 3, 4, 0, 8, 0],
         [7, 3, 0, 0, 0, 9, 0, 0, 4],
         [9, 0, 0, 0, 0, 0, 7, 0, 2],
         [0, 0, 8, 2, 0, 5, 0, 9, 0],
         [1, 0, 0, 0, 4, 0, 3, 0, 0]]



SIZE_OF_FONT = 50

font = pygame.font.SysFont(None, SIZE_OF_FONT)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    WINDOW.blit(screen_text, (x, y))
    pygame.display.update()







def emptyGrid():
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(WINDOW, WHITE, [i*DISTANCE_BETWEEN_GRIDS, j*DISTANCE_BETWEEN_GRIDS, DISTANCE_BETWEEN_GRIDS, DISTANCE_BETWEEN_GRIDS])

    pygame.display.update()


def displayNumbers(bo):
    emptyGrid()
    for i in range(9):
        for j in range(9):
            num = bo[i][j]
            if num == 0:
                continue
            text_screen(str(num), GREEN, j * 40 + 9, i * 40 + 5)
    pygame.display.update()


def drawGameWindow():
    x = 0
    y = 0
    while x <= 360:
        pygame.draw.line(WINDOW, BLACK, (x, y), (x, LINE_LENGTH))
        pygame.draw.line(WINDOW, BLACK, (y, x), (LINE_LENGTH, x))
        pygame.draw.line(WINDOW, BLACK, (x*3, y*3), (x*3, LINE_LENGTH), THICK_LINES)
        pygame.draw.line(WINDOW, BLACK, (y*3, x*3), (LINE_LENGTH, x*3), THICK_LINES)
        x += DISTANCE_BETWEEN_GRIDS
    pygame.display.update()


def highlightGrid(grid_x, grid_y, color):
    x_cord = grid_x * DISTANCE_BETWEEN_GRIDS
    y_cord = grid_y * DISTANCE_BETWEEN_GRIDS
    pygame.draw.line(WINDOW, color, (x_cord + 1, y_cord + 1), (x_cord + 1 + DISTANCE_BETWEEN_GRIDS, y_cord + 1), 4)
    pygame.draw.line(WINDOW, color, (x_cord + 1, y_cord + 1), (x_cord + 1, y_cord +1 + DISTANCE_BETWEEN_GRIDS), 4)
    pygame.draw.line(WINDOW, color, (x_cord + 38.5, y_cord), (x_cord + 38.5, y_cord + 39), 6)
    pygame.draw.line(WINDOW, color, (x_cord, y_cord + 39), (x_cord + 39, y_cord + 39), 6)


last_x, last_y = -1, -1
# THE GAME MAIN LOOP...
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            (grid_x, grid_y) = pygame.mouse.get_pos()
            grid_y = grid_y//40
            grid_x = grid_x//40
            highlightGrid(last_x, last_y, WHITE)
            last_x, last_y = grid_x, grid_y
            print(grid_x, grid_y)
            highlightGrid(grid_x, grid_y, BLUE)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                print("starting to solve the puzzle...")
                sudoku_solver.board = board
                if sudoku_solver.solveSudoku() == True:
                    print('solve sudoku returns true')
                    print(sudoku_solver.board)
                    displayNumbers(sudoku_solver.board)
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                    pygame.event.set_blocked(pygame.KEYDOWN)
                    pygame.event.set_blocked(pygame.KEYUP)
                    break
                else:
                    WINDOW.fill(WHITE)
                    text_screen("THis puzzle", BLUE, 30, 20)
                    text_screen("cant be solved", BLUE, 10, 80)
                break
                # here we will call the main sudoku solving function...



            ch = chr(event.key)
            print(ch)
            if ch.isalpha() or ch == 0:
                print(" an alphabet...")
                break
            board[grid_y][grid_x] = int(chr(event.key))
            print(" board is now ", *board)
            displayNumbers(board)
            highlightGrid(grid_x, grid_y, BLUE)


    drawGameWindow()
    pygame.display.update()