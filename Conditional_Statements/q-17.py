number=int(input("Enter a number: "))
if number%2==0:
    if number%3==0:
        print("Number is divisible by both")
    else:
        print("Number is divisible by 2 only")
elif number%3==0:
    print("Number is divisible by 3 only")
else:
    print("Number is not divisible by either 2 or 3")
