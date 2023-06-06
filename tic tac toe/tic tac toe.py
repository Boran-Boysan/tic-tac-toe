row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]


def display_game():
    print("Welcome to the tic tac toe game!!!\n")
    print(row1)
    print(row2)
    print(row3)

def select_row():
    row = 100
    while row < 0 or row >2:
        try:
            row = int(input("Please enter a row number:"))
            if row <0 or row>2:
                print("Your value is out of range. Try again!")
        except:
            print("You chose wrong value. Try again!")
    if row == 0:
        return row1
    elif row == 1:
        return row2
    else:
        return row3

def position():
    position_index = 100
    while position_index <0 or position_index>2:
        try:
            position_index = int(input("Please enter a index value: "))
            if position_index <0 or position_index>2:
                print("Your value is out of range. Try again!")
            
        except:
            print("You chose wrong value. Try again!")
    return position_index

def replacement_choice(game_list,position):
    r = False
    while r == False:
        user_placement = input("Type a string to place at the position:")
        if user_placement == "X" or user_placement == "O":
            r == True
            game_list[position] = user_placement
            break
        


    


    #game_list[position] = user_placement
    

def gameon_choice():
    choice = "wrong"
    while choice not in ["Y","N"]:
        choice = input("Would you like to kepp playing?(Y or N):")
        if choice not in ["Y","N"]:
            print("Sorry, but you did not choose a valid position (Y,N).")
        elif choice == "Y":
            return True
        else:
            return False

        

def game():
    if row1[0] == "X" and row1[1] == "X" and row1[2] == "X":
        print("You win!!")
    elif row2[0] == "X" and row2[1] == "X" and row2[2] == "X":
        print("You win!!")
    elif row3[0] == "X" and row3[1] == "X" and row3[2] == "X":
        print("You win!!")
    elif row1[0] == "O" and row1[1] == "O" and row1[2] == "O":
        print("You win!!")
    elif row2[0] == "O" and row2[1] == "O" and row2[2] == "O":
        print("You win!!")
    elif row3[0] == "O" and row3[1] == "O" and row3[2] == "O":
        print("You win!!")
    elif row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
        print("You win!!")
    elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
        print("You win!!")
    elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
        print("You win!!")
    elif row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
        print("You win!!")
    elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
        print("You win!!")
    elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
        print("You win!!")
    elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
        print("You win!!")
    elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
        print("You win!!")
    elif row3[0] == "X" and row2[1] == "X" and row1[2] == "X":
        print("You win!!")
    elif row3[0] == "O" and row2[1] == "O" and row1[2] == "O":
        print("You win!!")
    else:
        print("You lose")


game_on = True



while game_on:

    display_game()
    r = select_row()
    print(r)
    p = position()
    print(p)

    replacement_choice(r,p)

    display_game()

    game_on = gameon_choice()

game()


   