# variable scope

# other language e.g. python will not let you use variables defined in a function OUTSIDE of that function
# degrees = 0 #outside the function

# a function definition
# the 'celcius' variable inside the function is a DIFFERENT variable 
# than the 'celcius' variable outside the function
# the scope of varibles defined inside a fucntion is only inside that function
# what is happening in the function does not affect things outside it
def convertTemperature(fahrenheit) :
    celsius = (fahrenheit - 32) * 5 / 9  #inside the function 
    return celsius # if I want to make somethinkg that is inside the function available outside this function, then I have to 'return' it

# a function call
degrees = convertTemperature(50)

print("The temperature today is: ", degrees, " degrees celsius") # outside the function

# write a function that calculate the square root of a number and return it
# then print the returned value