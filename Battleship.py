from random import randint
from time import sleep

board = []

for x in range(6):
    board.append(["0"] * 6)

def print_board(board):
    for row in board:
        print((" ").join(row))

print("Lets play battleship")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)    

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(9):
    print("Turn"), turn 
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! Yous sank my battleship")
        break
    else:
        if (guess_row < 0 or guess_row > 5 ) or (guess_col < 0 or guess_col > 5):
            print("Oops, thats not even the ocean!")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already !")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("GAME OVER !")
        sleep(5) 
    turn =+ 1
    print_board(board) 

                       