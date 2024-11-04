number=int(input("Enter a number: "))
reversedNumber=0
while number>0:
    remainder=number%10
    reversedNumber=reversedNumber*10+remainder
    number=number//10
print("Reversed number is:", reversedNumber)
