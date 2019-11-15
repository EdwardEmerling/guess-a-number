import random     # imports the random number methods needed
play_again = True # initializes the control variable for continuous gameplay loop to start
correct = 0       # initializes correct guess count to zero
incorrect = 0     # initializes incorrect guess count to zero
while play_again: # continues playing the game as long as the player answers 'y'
    answer = "x"  # sets the answer value to an invalid value to allow the answer loop to be entered
    guess = 0     # sets the guess value to an invalid value to allow the guess loop to be entered
    actual= random.randint(1,10)  # generates a random number that the user must guess
    s_actual = str(actual)        # assigns the value of the random number to a string for other uses
    while guess != actual:        # makes the user keep guessing until they guess correctly
        while guess < 1 or guess > 10:    # checks the user's guess to see if it is valid
            s_guess = input("Guess a number between 1 and 10: ")   # user inputs a guess
            guess = int(s_guess)  # converts the input guess from a string to an integer for comparison
        if guess != actual:       # compares the guess to the random actual and executes if they aren't equal
            print("Nope, that's not it. Guess again!") # Ha ha!!
            incorrect = incorrect + 1     # increments the number of times the user guessed incorrectly
            guess = 0             # invalidates the guess variable to keep the loop in execution
    print("You guessed it! The number I was thinking of is " + s_actual +".") # Well done, Soldier!
    correct = correct + 1         # increments the number of times the user guessed correctly
    while answer != "y" and answer != "n": # checks the answer for validation
        answer = input('Would you like to play again? ("y" or "n"): ')  # user inputs 'y' or 'n'
    if answer == "n":             # checks the answer and executes if the player answered 'n'
        play_again = False        # switches the control variable so that the game loop exits
print("You made " + str(correct) + " correct guesses.")  # converts correct to a string 
print("You made " + str(incorrect) + " wrong guesses.")  # converts incorrect to a string
print("Thank you for playing. Goodbye!") # Adios, amigo!