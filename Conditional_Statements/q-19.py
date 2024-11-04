word=input("Enter a word: ")
if word.islower():
    print("The word is in lowercase")
elif word.isupper():
    print("The word is in uppercase")
else:
    print("The word is in mixcase")