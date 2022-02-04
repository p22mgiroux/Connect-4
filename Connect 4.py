import sys
import pygame
from pygame.locals import *

pygame.init()

width, height = 840, 840
screen = pygame.display.set_mode((width, height))

board = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

team = [1]

def play(board, slot, team):
    for x in range(6):
        if board[5 - x][slot - 1] == 0:
            board[5 - x][slot - 1] = team[0]
            team[0] *= -1
            print_board()
            pos[0] = 4
            break
        if x == 5:
            print("try again")
            break


def check_for_win():
    win = 0
    # Vertical Checks
    for x in range(6-3):
        for y in range(7):
            if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] and board[x][y] != 0:
                print("{} Wins".format(board[x][y]))
                win = board[x][y]
    # Horizontal Checks
    for x in range(6):
        for y in range(7-3):
            if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] and board[x][y] != 0:
                print("{} Wins".format(board[x][y]))
                win = board[x][y]
    # Diagonal Right Checks
    for x in range(6-3):
        for y in range(7-3):
            if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] and board[x][y] != 0:
                print("{} Wins".format(board[x][y]))
                win = board[x][y]
    # Diagonal Left Checks
    for x in range(2,6):
        for y in range(7-3):
            if board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] and board[x][y] != 0:
                print("{} Wins".format(board[x][y]))
                win = board[x][y]
    return win


def display_chip(surface, team, pos):
    if team[0] == 1:
        color1 = (255,220,0)
        color2 = (220,190,0)
    else:
        color1 = (220,0,0)
        color2 = (190,0,0)

    pygame.draw.circle(surface, color1, (120 * pos - 60, 60), 50)

    pygame.draw.circle(surface, color2, (120 * pos - 60 - 45, 60), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 - 42, 60 - 18), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 - 32, 60 - 32), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 - 18, 60 - 42), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60, 60 - 45), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 + 18, 60 - 42), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 + 32, 60 - 32), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 + 42, 60 - 18), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 + 45, 60), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 + 42, 60 + 18), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 + 32, 60 + 32), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 + 18, 60 + 42), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60, 60 + 45), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 - 42, 60 + 18), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 - 32, 60 + 32), 2)
    pygame.draw.circle(surface, color2, (120 * pos - 60 - 18, 60 + 42), 2)

    pygame.draw.circle(surface, color2, (120 * pos - 60, 60), 40)
    pygame.draw.circle(surface, color1, (120 * pos - 60, 60), 38)
    pygame.draw.circle(surface, color2, (120 * pos - 60, 60), 34)
    pygame.draw.circle(surface, color1, (120 * pos - 60, 60), 31)
    pygame.draw.circle(surface, color2, (120 * pos - 60, 60), 27)
    pygame.draw.circle(surface, color1, (120 * pos - 60, 60), 25)
        

def display_board(surface, board):
    pygame.draw.rect(surface, (0,0,255), (0,120,840,840))
    for i, x in enumerate(board):
        for n, val in enumerate(x):
            pygame.draw.circle(surface, (0,100,255), (n * 120 + 60, i * 120 + 180), 55)
            if val == 0:
                color1 = (255,255,255)
                color2 = (255,255,255)
            elif val == 1:
                color1 = (255,220,0)
                color2 = (220,190,0)
            else:
                color1 = (220,0,0)
                color2 = (190,0,0)

            pygame.draw.circle(surface, color1, (n * 120 + 60, i * 120 + 180), 50)

            pygame.draw.circle(surface, color2, (n * 120 + 60 - 45, i * 120 + 180), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 - 42, i * 120 + 180 - 18), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 - 32, i * 120 + 180 - 32), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 - 18, i * 120 + 180 - 42), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60, i * 120 + 180 - 45), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 + 18, i * 120 + 180 - 42), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 + 32, i * 120 + 180 - 32), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 + 42, i * 120 + 180 - 18), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 + 45, i * 120 + 180), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 + 42, i * 120 + 180 + 18), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 + 32, i * 120 + 180 + 32), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 + 18, i * 120 + 180 + 42), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60, i * 120 + 180 + 45), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 - 42, i * 120 + 180 + 18), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 - 32, i * 120 + 180 + 32), 2)
            pygame.draw.circle(surface, color2, (n * 120 + 60 - 18, i * 120 + 180 + 42), 2)

            pygame.draw.circle(surface, color2, (n * 120 + 60, i * 120 + 180), 40)
            pygame.draw.circle(surface, color1, (n * 120 + 60, i * 120 + 180), 38)
            pygame.draw.circle(surface, color2, (n * 120 + 60, i * 120 + 180), 34)
            pygame.draw.circle(surface, color1, (n * 120 + 60, i * 120 + 180), 31)
            pygame.draw.circle(surface, color2, (n * 120 + 60, i * 120 + 180), 27)
            pygame.draw.circle(surface, color1, (n * 120 + 60, i * 120 + 180), 25)


def print_board():
    for x in range(6):
        print(board[x])

print_board()
pos = [4]

while True:
    screen.fill((255,255,255))
    display_board(screen,board)
    display_chip(screen, team, pos[0])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if pos[0] < 7:
                    pos[0] += 1
                    print(pos)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if pos[0] > 1:
                    pos[0] -= 1
                    print(pos)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                play(board, pos[0], team)
                check_for_win()

    pygame.display.flip()
