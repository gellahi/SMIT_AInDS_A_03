givenNumber=int(input("Enter a number: "))
oddSum=0
evenSum=0
for i in range(givenNumber):
    if i%2==0:
        evenSum+=i
    else:
        oddSum+=i

print(f"Sum of even numbers is: {evenSum}")
print(f"Sum of odd numbers is: {oddSum}")