#!/usr/bin/python3
import random, time

def display_board(board):
    # Clears the screen and displays the current board
    print("\n"*50)
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[1]} | {board[2]} | {board[3]}')

def player_input():
    # Returns the Markers in Tuple, with the Player marker first
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    # Assigns the Marker to the Position
    board[position] = marker

def win_check(board, mark):
    # Returns any Winning conditions
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    # Returns who goes first
    return random.choice(["Player", "Computer"])

def space_check(board, position):
    # Returns only if the position is empty
    return board[position] == ' '


def full_board_check(board):
    # Returns True if there is any available moves
    # Returns False if no moves left
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    # Returns the position the User wants to place Marker
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

def replay():
    # Returns if the User wants to play again
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


## For AI
def choose_random_move(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if space_check(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

# Simple Algorithm for our Tic Tac Toe AI:
def get_computer_move(board, computer_letter):
    # Returns the Computers move
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = board.copy()
        if space_check(copy, i):
            place_marker(copy, computer_letter, i)
            if win_check(copy, computer_letter):
                return i

    # Give the Player a 50% chance to win
    if random.randint(0,100) >= 50:
        # Check if the player could win on their next move, and block them.
        for i in range(1, 10):
            copy = board.copy()
            if space_check(copy, i):
                place_marker(copy, player_letter, i)
                if win_check(copy, player_letter):
                    return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if space_check(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move(board, [2, 4, 6, 8])


# Start of Game Loop
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Computer'

        else:
            # Computers's turn.
            display_board(theBoard)
            time.sleep(2)
            position = get_computer_move(theBoard, player2_marker)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Computer has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player'

    if not replay():
        break