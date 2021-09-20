names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random as r
k = r.randint(0,len(names)-1)
print(f"{names[k]} is going to pay the bill")

''' this can also be done by choice function as follows:
    print(f"{r.choice(names)} is going to pay the bill.")
    r.choice() function directly gives the random element from a SEQUENCE like list , dictionary,etc '''