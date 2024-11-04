pyramidLength = int(input('Enter the length of the pyramid: '))
for i in range(pyramidLength):
    for k in range(pyramidLength - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end=' ')
    print()
