# 1. Name:
#      Andre Regino
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
	
    # Opening file.
	with open(filename, w) as game
    
    # Checking that the file is not empty
    if game != null:
        previous_board = game.blank_board[0]
        return previous_board
    
    # If empty start a new board.
    else:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    file = open (filename, w+)
    
    file.json.dumps(board)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    num_space = 0 

    # Count blank spaces on the board.
    for space in board:
        if space == BLANK:
            num_space += 1

    # Set the turn by oreder of even or odd.
    if num_space % 2 == 1:
        print('It is "X" turn.')
        return True
    else:
        print('It is "O" turn ')
        return False


def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''

    # Put game play code here. Return False when the user has indicated they are done.
    while True:
        "Game loop"

        # Determine whose turn it is and return boolean.
		condition = is_x_turn(board)
        
        # User input.
        answer = input('Type the number of the space you want to field (type "q" to quit) \n')
       
        # Option to quit and save the progress.
        if answer.lower() == 'q'
            save_board(game_file.json, board)
            
            # Exit game loop.
            return False    
        
        # Determine what sign to place based on the turn.
        elif condition == True:
            board[answer - 1] = X
        else:
            board[answer - 1] = O

        # Determine if game is finished and exit game loop.
		if game_done(board, True):
			return False

		

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.

# Once the file is provided we read it and verify if there is a saved game.
board = read_board(game_file.json)

display_board(board)
play_game(board)

