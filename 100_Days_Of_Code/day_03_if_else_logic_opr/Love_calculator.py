print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name = name1 + name2
cnt_t = name.count("t")  
cnt_r = name.count("r") 
cnt_u = name.count("u") 
cnt_e = name.count("e") 
cnt_l = name.count("l") 
cnt_o = name.count("o") 
cnt_v = name.count("v") 

score_1 = cnt_t + cnt_r + cnt_u + cnt_e 
score_2 = cnt_l + cnt_o + cnt_v + cnt_e
score = int(str(score_1) + str(score_2))

if score <10 or score >90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score <50 and score >40:
  print(f"Your score is {score}, you are alright together.")  
else :
  print(f"Your score is {score}.")