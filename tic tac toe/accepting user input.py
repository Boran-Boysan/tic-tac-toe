from turtle import position


def display(r1,r2,r3):
    print(r1)
    print(r2)
    print(r3)

row1 = [" "," "," "] 
row2 = [" ","X"," "] 
row3 = [" "," "," "]
display(row1,row2,row3)
print("\n")
position_index = int(input("Chose an index position: "))
print(row2[position_index])