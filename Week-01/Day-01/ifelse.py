a = 30
b = 20

#the if statement
if a>b:
    #body of the if statement
    print("a is bigger than b")
    print("this is another line") 

#this is the code AFTER the if statement
print("this is the last line") 


#taking user input
string_number = input("Enter a number ")
print(f"the number is {string_number}")
number = int(string_number)

result = 7 + number
print("the result is ")
print(result)


#input with if/else
string_number = input("Enter a number ")
number = int(string_number)

if number >= 5:
    print("number equal, or larger than 5")
else:
    print("number is smaller than 5")


#selecting from options - elif
word = input("push a button ")

# if the user entered play
if word == "play":
    print("playing video")

# otherwise (else-if) if the user entered stop  
elif word == "stop":    
    print("stopping video")

# otherwise (else-if) if the user entered stop  
elif word == "rwd":
    print("rewinding tape")

# in all other situations    
else:
    print("I don't understand")

