number=int(input("Enter a number: "))
digitSum=0
while number>0:
    digitSum+=number%10
    number//=10
print("Sum of digits in the number is:",digitSum)