minRange=int(input("Enter the minimum range: "))
maxRange=int(input("Enter the maximum range: "))
number=int(input("Enter the number: "))
if number in range(minRange,maxRange+1):
    print(f"{number} is in the range of {minRange} and {maxRange}")
else:
    print(f"{number} is not in the range of {minRange} and {maxRange}")