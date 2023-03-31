import random

def guessing_game():
    number = random.randint(1, 100) # storing our random number in a variable called number
    guesses = 5 # this is how many guesses the player gets before the game is over
    print(f"For the cheaters: {number}") # here, we are cheating... booooo!
    user_input = int(input("Guess a number between 1 & 100: \n")) # requesting user input for our user's guess

    while user_input != number: # if the guess IS NOT the number... run this loop
        if user_input < number:
            print("Too low. Go again.")
        else: 
            print("Too high. Go again.")
        guesses -= 1 # remove a guess... we are in the loop, which means the guess wasn't correct

        if guesses == 0: # has the user ran out of guesses? If they do, end the loop
            print("Game over.")
            break
        user_input = int(input(f"You have {guesses} guesses left... Guess a number: ")) # if not... ask again
        # I don't need this in a else because... the only way we get to line 19, is if line 16 isn't true

    if guesses > 0:
        print("You won.")

guessing_game()