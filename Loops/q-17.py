import random
while True:
    number=random.randint(1,20)
    guess=int(input("Guess the number between 1 and 20: "))
    if guess==number:
        print("You guessed it right!")
    else:
        print("You guessed it wrong! The number was:", number)
    
