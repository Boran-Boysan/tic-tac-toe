from operator import index


def user_choice():
    position_index = 100
    while position_index <0 or position_index>10:
        try:
            position_index = int(input("Please enter a value: "))
            if position_index <0 or position_index>10:
                print("Your value is out of range")
            
        except:
            print("You chose wrong value.")
        

        
           

    
    print(position_index)  
    return position_index
    

user_choice()