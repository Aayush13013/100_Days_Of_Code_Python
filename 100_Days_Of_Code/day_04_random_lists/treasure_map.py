row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# here different convention is followed than a matrix i.e. 1st digit suggests the coloumn and 2nd digit suggets row
map[int(position[1])-1][int(position[0])-1] = "X" 
print(f"{row1}\n{row2}\n{row3}")