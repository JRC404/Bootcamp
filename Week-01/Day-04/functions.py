light_on = True # True means on, False means off

# I want to be able to switch the light off if it is on, and on if it is off

def light_switch():
    global light_on
    if light_on: # short hand for light_on == True
        light_on = False
        print("The light has been turned off.")
    else:
        light_on = True
        print("The light has been switched on. Pricey.")

# how do we call a function? We simply say its name
light_switch()
light_switch()
light_switch()
light_switch()

# def addition(number_one, number_two):
#     print(number_one + number_two)

def addition():
    first_number = int(input("Please give me your first number: \n"))
    second_number = int(input("Please give me your second number: \n"))
    print(first_number + second_number)

def subtraction():
    first_number = int(input("Please give me your first number: \n"))
    second_number = int(input("Please give me your second number: \n"))
    print(first_number - second_number)

def multiplication():
    first_number = int(input("Please give me your first number: \n"))
    second_number = int(input("Please give me your second number: \n"))
    print(first_number * second_number)

def division():
    first_number = int(input("Please give me your first number: \n"))
    second_number = int(input("Please give me your second number: \n"))
    print(first_number / second_number)

# TODO: Make one function that takes three user inputs: 1. first number, 2. The operand, 3. second number

def calculator():
    first_number = float(input("Gimme your first number or else: \n"))
    operand_selection = input("Please supply your operand: (+, -, /, *)\n")
    second_number = float(input("Gimme your second number or else: \n"))
    result = 0
    
    if operand_selection == "+" or operand_selection == "plus":
        result = first_number + second_number
    elif operand_selection == "-" or operand_selection == "subtract":
        result = first_number - second_number
    elif operand_selection == "*" or operand_selection == "x" or operand_selection == "multiply":
        result = first_number * second_number
    elif operand_selection == "/" or operand_selection == "divide":
        result = first_number / second_number
    else:
        print("You're an idiot.")
    print(result)

# addition() #! needs two values to give to number_one and number_two
#! TypeError: addition() missing 2 required positional arguments: 'number_one' and 'number_two'

# first_number = int(input("Please give me your first number: \n"))
# second_number = int(input("Please give me your second number: \n"))

print("---------")

calculator()

# addition()
# subtraction()
# multiplication()
# division()
# addition(first_number, second_number) # what will the answer be?



# addition(1, 2) # 3
# addition(6, 8) # 14
# addition(345, 789) # 1134
# addition(123, 456)