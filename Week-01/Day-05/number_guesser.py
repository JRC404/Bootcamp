import random


def guessing_game():
    guesses = 2
    number = random.randint(1, 100)
    print(f"For the cheaters: {number}")
    while True:
        if guesses > 0:
            user_input = int(input("Guess a number between 1 & 100: \n"))

            if user_input == number:
                print("Well done, yo.")
                break # seen this before?
            elif user_input < 0 or user_input > 100:
                print("You, my friend, are an idiot.")
            elif user_input < number:
                print("Your guess is too low... unlucky.")
            elif user_input > number:
                print("Your guess is too daaaamn high.")
            guesses -= 1
            print(guesses)
        elif guesses == 0:
            print("You lost.")
            break

#! variable named guesses to store how many guesses we have in the game, it's 5
#! while loop with a counter
#? guesses variable

# score variable that starts at 5 and minus 1 with each guess?

guessing_game()