import math

def square(number):
        root = math.sqrt(abs(number))
        return root
        
while True:
    try:
        number= float(input("Give me a number, and I will give you a square root of that number:\n"))
    except ValueError:
        print("Not a number!")
        continue
    else:
        print("Yay, a number!")
        break
    
while number ==0:
    print("However, ya cannae do a square root of zero, ya bampot!")
    number= float(input("Give me a number WHICH ISNAE ZERO, and I will give you a square root of that number:\n"))

if number !=0 and number < 0:
    print("\nTrying to be a smarter than a chicken, eh?\nSquare root of a negative is always a positive.\n")
    square(number)
    

elif number !=0 and number > 0:
    square(number)

            
result = square(number)
    
print("The square root of ", number, " is", result, "\n")
