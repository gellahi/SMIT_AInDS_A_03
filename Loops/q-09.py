limit=int(input("Enter the range: "))
fibonacciStart=int(0)
fibonacciEnd=int(1)
for i in range(limit):
    print(fibonacciStart)
    fibonacciEnd=fibonacciStart+fibonacciEnd
    fibonacciStart=fibonacciEnd-fibonacciStart
    