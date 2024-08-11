#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9

# Update the game board with the user input
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def markBoard(position, mark):
    for key in board.keys():
        if key == int(position):
            board[key] = mark
    return board


# Print the game board after selection
print_board = ( '           \n' +
                ' 1 | 2 | 3 \n' +
                ' --------- \n' +
                ' 4 | 5 | 6 \n' +
                ' --------- \n' +
                ' 7 | 8 | 9 \n' +
                '           \n' )

def printBoard(position, player_sign):
    global print_board
    print_board = print_board.replace(position, player_sign)
    return print(print_board)


# Validate user move to include only 1-9 and no duplicate move
used_position = []
def validateMove(position):
    if position in ['1','2','3','4','5','6','7','8','9'] and position not in used_position:
        used_position.append(position)
        return True
    elif position in ['1','2','3','4','5','6','7','8','9'] and position in used_position:    
        print("\n\nUsed position. Try again")
        print(print_board)
        return False
    print("\n\n Wrong input. Try again.")
    print(print_board)
    return False


# List of all win combinations and the logic to get the winner
winCombinations = [
    [1, 2, 3],  # First row
    [4, 5, 6],  # Second row
    [7, 8, 9],  # Third row
    [1, 4, 7],  # First column
    [2, 5, 8],  # Second column
    [3, 6, 9],  # Third column
    [1, 5, 9],  # First diagonal
    [3, 5, 7],  # Second diagonal
]

def checkWin(player):
    for combination in winCombinations:
        xo_count = 0
        for position in combination:
            if player == board[position]:
                xo_count += 1
                if xo_count == 3:
                    return True
    return False


# To check if the game board is fully marked (Tie)
def checkFull():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


# To reset board if user decide to play again
def resetBoard():
    global board, print_board, used_position
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    print_board = ( '           \n' +
                    ' 1 | 2 | 3 \n' +
                    ' --------- \n' +
                    ' 4 | 5 | 6 \n' +
                    ' --------- \n' +
                    ' 7 | 8 | 9 \n' +
                    '           \n' )
    used_position = []


# Game starting point
def main():
    gameEnded = False
    currentTurnPlayer = 'X'
    resetBoard()

    print('\nGame started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n' +
        '           \n' )


# Game flow:
## 1. Ask for user input and validate, 
## 2. Update the board
## 3. Check win or tie situation
## 4. Switch User
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        while validateMove(move):
            markBoard(move, currentTurnPlayer)
            printBoard(move, currentTurnPlayer)
            if checkWin(currentTurnPlayer):
                print(f"Win for {currentTurnPlayer}!!!")
                gameEnded = True
                break
            elif checkFull():
                print("That's a Tie!")
                gameEnded = True
                break
            currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X' 
            break 
    print("Thanks for playing.\n")


# Mainly for play again function
while True:
    main()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("\nGoodbye!")
