import numpy as np
import random 
from replit import clear

def print_game_board(game_arr):
    for row in range(game_arr.shape[0]):     
        print(' '+game_arr[row,0]+' | '+game_arr[row,1]+' | '+game_arr[row,2]+' ')
        if row != 2:
            print('-----------')

def check_win(game_arr, player):
    for row in range(game_arr.shape[0]):
        if game_arr[row,0]==game_arr[row,1]==game_arr[row,2]:
            if game_arr[row,0]==player: 
                return 1
    for col in range(game_arr.shape[1]):
        if game_arr[0,col]==game_arr[1,col]==game_arr[2,col]:
            if game_arr[0,col]==player: 
                return 1
    if game_arr[0,0]==game_arr[1,1]==game_arr[2,2]:
            if game_arr[0,0]==player: 
                return 1
    elif game_arr[2,0]==game_arr[1,1]==game_arr[0,2]:
            if game_arr[2,0]==player: 
                return 1
    else:
        print('No winner !')
        return 0

def update_game_board(game_arr, player):
    print(f'Player {player}, select your postion.')
    
    row_pos = int(input('Row number(1-3): '))-1
    while row_pos not in [0,1,2]:
        row_pos=int(input('Invalid selection! Row number(1-3): '))-1
    
    col_pos = int(input('Column number(1-3): '))-1
    while col_pos not in [0,1,2]:
        col_pos=int(input('Invalid selection! Column number(1-3): '))-1
    
    if game_arr[row_pos,col_pos] == ' ':
        game_arr[row_pos,col_pos] = player
    else:
        print('This position is already used, please select a different one.')
        return update_game_board(game_arr, player) 
    
    return game_arr

def tic_tac_toe(copmuter):
    player_1 = input('Player 1, select X or O: ').upper()

    if player_1=='X':
        print('Player 2, you are: O')
    elif player_1=='O':
        print('Player 2, you are: X')
    else:
        player_1 = input('Invalid selection! Player 1, select X or O: ').upper()

    game_arr = np.empty((3,3), dtype=str)
    game_arr =  np.select([game_arr==''],' ',game_arr)

    game_over = 0
    player=random.choice(['X','O'])

    while not game_over:
        clear()
        print_game_board(game_arr)

        if any([' ' in game_arr.flatten()]):
            if (computer) & (player != player_1):
                
                row_pos = random.choice([0,1,2])
                col_pos = random.choice([0,1,2])
                while game_arr[row_pos, col_pos] != ' ':
                    row_pos = random.choice([0,1,2])
                    col_pos = random.choice([0,1,2])
                game_arr[row_pos, col_pos] = player
                game_over = check_win(game_arr, player)

            else:
                game_arr = update_game_board(game_arr, player)
                game_over = check_win(game_arr, player)
            if game_over == 1:
                clear()
                print_game_board(game_arr)
                print(f'Player {player}, you won!')
            if player == 'X':
                player='O'
            else:
                player='X'

        else:
            print('Game Over! No one won!')
            game_over=1

print('Welcome to Tic Tac Toe')
while input("Do you want to play a game of Tic Tac Toe? Type 'y' or 'n': ") == "y":
    clear()
    computer = input("Do you want to play with the computer? Type 'y' or 'n': ") == "y"
    tic_tac_toe(computer)

    
    




