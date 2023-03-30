peoples_names = ["Mark", "Juan", "Ali", "Cathy", "Sylvia", "Noah"]
listB = [56,78,100,45,88,71]

# vairables will hold or contain VALUES
is_it_raining = True # True is a boolean VALUE
no_of_people = 15 # 10 is an int VALUE
temperature = 21.5 # 23.45 is a float VALUE
message = "hello" # "hello" is a string VALUE


while(True):
    command = input("what number would you like to check - or enter 'exit' to exit")
    if command=="exit":
        break
    number = int(command)

    # number in listB: Is that item in the list?
    if number in listB: 
        print(number, " is in")
    else:
        print(number, " is not in the list")

