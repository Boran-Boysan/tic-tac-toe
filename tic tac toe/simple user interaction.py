



def display_game(game_list):
    print("here is the current list")
    print(game_list)



def position_choice():
    choice = "wrong"
    while choice not in ["0","1","2"]:
        choice = input("Please select your position:")

        if choice not in ["0","1","2"]:
            print("Sorry, but you did not choose a valid position (0,1,2).")
    return int(choice)


def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at the position:")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = "wrong"
    while choice not in ["Y","N"]:
        choice = input("Would you like to keep playing?(Y or N):")
        if choice not in ["Y","N"]:
            print("Sorry, but you did not choose a valid position (Y,N).")
        elif choice == "Y":
            return True
        else:
            return False

       



game_on = True

game_list = [0,1,2]

while game_on:

    display_game(game_list)
    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()
