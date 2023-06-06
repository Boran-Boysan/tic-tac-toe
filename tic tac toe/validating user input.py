


def display(r1,r2,r3):
    print(r1)
    print(r2)
    print(r3)

def user_choice():
    position_index = "empty"
    while position_index.isdigit() == False:
        position_index = (input("Chose an index position(0-10): "))
        if position_index.isdigit() == False:
            print("Your value is not digit! Try Again!")
    while int(position_index) <0 or int(position_index) >10:
        position_index = (input("Chose an index position(0-10): "))
        
           

    
        
    return position_index
    


row1 = [" "," "," "] 
row2 = [" ","X"," "] 
row3 = [" "," "," "]
display(row1,row2,row3)
print("\n")

user_choice()

