number = 10

 # what is the value of this line?
print(f"The value is {number + 7}")
# number + 7 is just an equation... it isn't affecting number in any way

number += 7 # what is the value of this line?
print(f"The value is {number}")
# here, we are saying number is equal to itself + 7

 # what is the value of this line?
print(f"The value is {number + 7}")
# again, we are just adding the two values together, we aren't assigning anything to number


print(number) # # what is the value of this line?

number = 50 # what is the value of number in the sums below?
number + 10 # 50 
number += 10 # 60
number + 10 # 60
number += 10 # 70 
number - 20 # 70
number -= 20 # 50
number - 150 # 50

number = 0
number += 10 # what is the value of number here?
print(f"{number}")
number -= 10 # what is the value of number here?
print(f"{number}")
number *= 10 # what is the value of number here?
print(f"{number}")
number /= 10 # what is the value of number here?
# TODO: Do 10 assignment operators and write down the value on each line

print(number) # what will the value be?

number = 10
number += 1
print(number)

# logical operator
print(10 < 20 and 20 < 40) # true

print(20 < 15 or 20 < 40) # true

print(not(10 < 20 and 10 < 30)) # false because inside of the brackets is true

silly_number = 50
random_number = 20

print(silly_number < random_number and random_number == 20) # false
print(silly_number < random_number and random_number == 10) # false 
print(silly_number > random_number and random_number == 10) # false
print(silly_number > random_number and random_number == 20) # true
print(silly_number > random_number or random_number == 20) # true
