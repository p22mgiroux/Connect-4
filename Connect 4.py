import sys
import pygame
from pygame.locals import *

pygame.init()

width, height = 840, 840
screen = pygame.display.set_mode((width, height))
smallfont = pygame.font.SysFont('Corbel', 40)
instructions1 = smallfont.render('Connect four of your checkers in a row', True, (0,0,0))
instructions2 = smallfont.render('while preventing your opponent from doing', True, (0,0,0))
instructions3 = smallfont.render('the same. But, look out - your opponent', True, (0,0,0))
instructions4 = smallfont.render('can sneak up on you and win the game!', True, (0,0,0))
smallfont = pygame.font.SysFont('Corbel', 70)
start_text = smallfont.render('Which Color Starts?', True, (0,0,0))
smallfont = pygame.font.SysFont('Corbel', 120)
yellow_wins = smallfont.render('Yellow Wins!', True, (255,220,0))
red_wins = smallfont.render('Red Wins!', True, (220,0,0))

logo = pygame.image.load(r'connect4logo.png')
yellow = pygame.image.load(r'connect4yellow.png')
red = pygame.image.load(r'connect4red.png')
shadow = pygame.image.load(r'connect4shadow.png')
logo = pygame.transform.scale(logo, (840, 258))
yellow = pygame.transform.scale(yellow, (350, 200))
red = pygame.transform.scale(red, (350, 200))
shadow = pygame.transform.scale(shadow, (360, 210))


board = [
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
]

team = [0]

def play(slot, side):
    for x in range(6):
        if board[5 - x][slot - 1] == 0:
            board[5 - x][slot - 1] = side
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


def display_chip(surface, pos):
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
    pygame.draw.rect(surface, (0,0,255), (0,120,840,720))
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


def start_screen():
    screen.fill((255,255,255))

    if 50 <= mouse[0] <= 400 and 590 <= mouse[1] <= 790:
        screen.blit(shadow, (45,585))

    if 440 <= mouse[0] <= 750 and 590 <= mouse[1] <= 790:
        screen.blit(shadow, (435,585))

    screen.blit(logo, (0,0))
    screen.blit(yellow, (50,590))
    screen.blit(red, (440,590))
    screen.blit(instructions1 , (420 - instructions1.get_rect()[2] // 2, 250))
    screen.blit(instructions2 , (420 - instructions2.get_rect()[2] // 2,300))
    screen.blit(instructions3 , (420 - instructions3.get_rect()[2] // 2, 350))
    screen.blit(instructions4 , (420 - instructions4.get_rect()[2] // 2, 400))
    screen.blit(start_text, (420 - start_text.get_rect()[2] // 2, 500))


def print_board():
    for x in range(6):
        print(board[x])

print_board()
pos = [4]
moving = [0]

while True:           
    mouse = pygame.mouse.get_pos()

    screen.fill((255,255,255))  
    display_board(screen,board)
    if moving[0] == 1:
        display_chip(screen, pos[0])

    if check_for_win() != 0:
        if check_for_win() == 1:
            screen.blit(yellow_wins, (420 - yellow_wins.get_rect()[2] // 2, 10))
        if check_for_win() == -1:
            screen.blit(red_wins, (420 - red_wins.get_rect()[2] // 2, 10))
        display_chip(screen, 1)
        display_chip(screen, 7)
        moving[0] = 2

    if moving[0] == 0:
        start_screen()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if moving[0] == 1:
                    if pos[0] < 7:
                        pos[0] += 1
                        print(pos)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if moving[0] == 1:
                    if pos[0] > 1:
                        pos[0] -= 1
                        print(pos)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if moving[0] == 1:
                    play(pos[0], team[0])
                    check_for_win()
            if event.key == event.key == pygame.K_q:
                moving[0] = 1
        if event.type == pygame.MOUSEBUTTONUP:
            if moving[0] == 0:
                if 50 <= mouse[0] <= 400 and 590 <= mouse[1] <= 790:
                    team[0] = 1
                    moving[0] = 1

                if 440 <= mouse[0] <= 750 and 590 <= mouse[1] <= 790:
                    team[0] = -1
                    moving[0] = 1

    pygame.display.flip()
