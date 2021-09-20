# two_digit_number = input("Please enter a two digit number:  ")
# unitDigit = int(two_digit_number[1])
# tenDigit = int(two_digit_number[0])
# sumOfDigits = unitDigit + tenDigit
# print(sumOfDigits)

def sumOfDigits(num) : 
    result = 0 
    while num : 
        a = num%10
        result += a 
        num = int(num/10)
    return result
print(sumOfDigits(13579))        