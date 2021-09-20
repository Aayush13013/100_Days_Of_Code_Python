# this art can be downloaded from ASCII art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random as r

comp_turn = r.randint(0,2)

your_turn = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors\n"))

if your_turn>2:
    print("You chose an invalid number . Try again")

elif comp_turn==your_turn:
  print(f"You both chose same thing. It's a tie!")

elif comp_turn == 0:
  print(f"comp chose\n{rock}")
  if your_turn == 1:
    print(f"you chose\n{paper}\nYou win")
  else:
    print(f"you chose\n{scissors}\nYou lose")

elif comp_turn == 1:
  print(f"comp chose\n{paper}")
  if your_turn == 0:
    print(f"you chose\n{rock}\nYou lose")
  else:
    print(f"you chose\n{scissors}\nYou win")

elif comp_turn == 2:
  print(f"comp chose\n{scissors}")
  if your_turn == 1:
    print(f"you chose\n{paper}\nYou lose")
  else:
    print(f"you chose\n{rock}\nYou win")
