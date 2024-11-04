import time
import os
start=int(input("Enter the starting number: "))
if start>0:
    for i in range(start,0,-1):
        print(i)
        time.sleep(1)
        os.system('cls')
else:
    print("Invalid Starting Number")