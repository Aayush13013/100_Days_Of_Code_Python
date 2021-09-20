#  this treasure isfrom ASCII 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

LR = input("you are at a cross road , where do you want to go? please type left' or 'right'\n").lower()

if LR == "left" :
  swim_or_wait = input ("you have come to a lake. there is an island at the middle of the lake. type 'wait' to wait for the boat and 'swim' to swim across the lake.\n").lower()
  if swim_or_wait == "wait":
    island = input("You have reached the island unharmed. There is a house at the middle of the island with three doors with three different colors red , blue and yellow. To select one of them type 'red' for red , 'blue' for blue and 'yellow' for yellow.\n").lower()
    if island == "yellow":
      print("You win")
    else :
      print("Game Over")  
  else :
    print("Game Over")  
else :
  print("Game Over")











