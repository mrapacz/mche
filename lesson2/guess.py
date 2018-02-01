hidden_number = 20
guessed = False
while not guessed:
    guess = int(input("Guess the number! "))
    if guess == hidden_number:
        guessed = True
        print("Correct!")
    else:
        print("Incorrect, let's try again.")
