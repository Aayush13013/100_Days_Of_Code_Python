#Password Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""

# for i in range (0, nr_letters ):
#   rand_num = r.choice(letters)
#   password +=rand_num
# for n in range (0, nr_symbols):
#     rand_num2 = r.choice(symbols)
#     password += rand_num2
# for x in range (0, nr_numbers):
#     rand_num3 = r.choice(numbers)
#     password+= rand_num3
# print(password)    

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for i in range (0, nr_letters):
    r1 = r.choice(letters)
    password_list += r1
for i in range (0, nr_symbols):
    r2 = r.choice(symbols)
    password_list += r2
for i in range (0,nr_numbers):
    r3 = r.choice(numbers)    
    password_list+=r3
    
r.shuffle(password_list)



password = ""
for i in password_list:
    password+= i
print(password)    


