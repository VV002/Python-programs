import random
import os 
width = os.get_terminal_size()

#Creating a Empty board
board=[[" " for i in range(3)] for j in range(3)]

#Function to display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("----------")
.0
#Function to check the winner
def winner_checker(board,player):
    
    #Checking the rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    
    #Checking the colums
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    #Checking the diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

print("..................WELCOME TO TIC TAC TOE GAME..................".center(width.columns))
while True:
    display_board(board)
    #User turn
    row = int(input("Select the row('0','1','2'): "))
    column = int(input("Select the column('0','1','2'): "))

    #Checking if the position is empty
    if board[row][column]==" ": 
        board[row][column] = "X"
    else:
        print("The position is already filled, Try again!!")
        continue
    
    #Checking if the user has won
    if winner_checker(board,"X"):
        display_board(board)
        print("Congratulations!! You have won the game!!")
        break
    
    #Checking if the game is a draw
    draw = True
    for row in board:
        if " " in row:
            draw = False
    
    if draw:
        display_board(board)
        print("The game is a draw!!")
        break

    #Computer turn
    while True:
        row = random.randint(0,2)
        column = random.randint(0,2)
        #Checking if the position is empty
        if board[row][column]==" ": 
            board[row][column] = "O"
            print(f"Computer Selected row and column: [{row},{column} ]")
            break
    
    if winner_checker(board,"O"): #Checking if the computer has won
        display_board(board)
        print("Computer has won the game!!")
        break