import random


def display_board(board):

    print(board[7]+ "|"+board[8]+ "|"+board[9])
    print(board[4]+ "|"+board[5]+ "|"+board[6])
    print(board[1]+ "|"+board[2]+ "|"+board[3])

def player_input():

    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O:").upper()
    
    player1 = marker
    player2 = "empty"

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"


    return (player1,player2)

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):

    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[9] == mark and board[5] == mark and board[1] == mark:
        return True
    else:
        return False

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board,position):
    return board[position] == " "

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9):"))
    
    return position

def replay():

    choice = input("Play again? Enter Yes or No:")

    return choice == "Yes"


print("--------------------Welcome to the game---------------------")

while True:

    Board = [" "]*10

    player1_marker , player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Do you want to play? y or n?:").lower()

    if play_game == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        
        if turn == "Player 1":

            display_board(Board)

            position = player_choice(Board)

            place_marker(Board,player1_marker,position)

            if win_check(Board,player1_marker):
                display_board(Board)
                print("Player 1 has won!!!")
                game_on = False


            else:

                if full_board_check(Board):
                    display_board(Board)
                    print("Tie game!!!!!")
                    game_on = False
                
                else:
                    turn = "Player 2"

        else:
            display_board(Board)

            position = player_choice(Board)

            place_marker(Board,player2_marker,position)

            if win_check(Board,player2_marker):
                display_board(Board)
                print("Player 2 has won!!!")
                game_on = False

            else:

                if full_board_check(Board):
                    display_board(Board)
                    print("Tie game!!!!!")
                    game_on = False
                
                else:
                    turn = "Player 1"


    if not replay():
        break