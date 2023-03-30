# Create a program that generates a random number between 1 and 100 and asks the user to guess the number. The program should give hints if the guess is too low or too high, and should continue until the user correctly guesses the number.

# Good luck! 🍀

# import random

# Loop
# if statement
# variable for the number
# input
# higher or lower
# random number generator

import random

number = random.randint(1, 100)

while True:
    user_input = int(input("Guess a number between 1 & 100: \n"))

    if user_input == number:
        print("Well done, yo.")
        break # seen this before?
    elif user_input < 0 or user_input > 100:
        print("You, my friend, are an idiot.")
    elif user_input < number:
        print("Your guess is lower... unlucky.")
    elif user_input > number:
        print("Your guess is too daaaamn high.")