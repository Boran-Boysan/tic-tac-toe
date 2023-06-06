def display_board(board):

    print(board[7]+ "|"+board[8]+ "|"+board[9])
    print(board[4]+ "|"+board[5]+ "|"+board[6])
    print(board[1]+ "|"+board[2]+ "|"+board[3])

test = [" "]*10

display_board(test)

def player_input():

    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O:")
    
    player1 = marker
    player2 = "empty"

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    #print(player1,player2)

    return (player1,player2)


#player_input()

player1_marker, player2_marker = player_input()
print(player1_marker)
print(player2_marker)

