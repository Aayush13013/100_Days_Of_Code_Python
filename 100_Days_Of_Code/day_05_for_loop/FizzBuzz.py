lst = []
for i in range(1,101):
  lst.append(i)
for n in lst:
  if n%3==0 and n%5==0:
    print("FizzBuzz")
  elif n%5 ==0:
    print("Buzz")
  elif n%3==0 :
    print("Fizz")  
  else :
    print(n)

