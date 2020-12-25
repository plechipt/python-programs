import sys
import random

space = ('\n'*40)
game_board = [' ']*10

def display_board(board):
    print('\n'*20)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    while True:
        q = input('\nPlayer 1 wanna be X or O: ').upper()
        if q == 'X':
            return ('X','O')
        elif q == 'O':
            return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def wins(p_win,var,board):
    if win is True:
        if game_board[choice] == 'X':
            print('\nPlayer1 has won!')
            sys.exit()
        elif game_board[choice] == 'O':
            print('\nPlayer2 has won!')
            sys.exit()

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' in board

def full_board(fun):
    if fun is False:
        print('The game is draw!')
        sys.exit()

def player_choice(board):
    while True:
        q = int(input('\nChoose your position (1-9:): '))
        if q in (1,2,3,4,5,6,7,8,9):
            return q

def choose_first(p_marker):
    if p_marker == 'X':
        print('\nPlayer1 is first')
    else:
        print('\nPlayer2 is first')

#here comes the main part
print('\nWelcome to Tic Tac Toe game!')
p1_marker,p2_marker = player_input()
print(space)
choose_first(p1_marker)
q = input('\nReady to play (y/n): ')
if q == 'n':
    sys.exit()
while True:
    #player1
    display_board(game_board)
    choice = player_choice(game_board)
    place_marker(game_board,p1_marker,choice)
    display_board(game_board)
    win = win_check(game_board,p1_marker)
    wins(win,choice,game_board)

    #player2
    display_board(game_board)
    choice = player_choice(game_board)
    place_marker(game_board,p2_marker,choice)
    display_board(game_board)
    win = win_check(game_board,p2_marker)
    wins(win,choice,game_board)
