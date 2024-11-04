number=int(input("Enter a number: "))
noOfDigits=0
while number>0:
    noOfDigits+=1
    number//=10
print("Number of digits in the number is:",noOfDigits)