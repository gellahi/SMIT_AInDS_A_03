while True:
    for i in range(1,50):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
            break
    break