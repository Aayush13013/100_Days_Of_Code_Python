print("welcome to the calculator")
total_bill = float(input("what was the total bill?\n$"))
ask_tip_percent = int(input("what percentage of the bill will you tip? 10 , 12 or 15\n"))
number_of_people = int(input("how many people to split the bill\n"))
total_bill += total_bill*(ask_tip_percent/100)
split = total_bill/number_of_people
print(f"each person should pay: ${round(split,2)}" )