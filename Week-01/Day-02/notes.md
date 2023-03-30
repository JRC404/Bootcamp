# Day 02

**Please remember: To run a Python file, we need to use python filename.py**

## Arithmetic

* +, -, /, *, %
* Addition, Subtraction, Division, Multiplication and Modulus

* 10 % 3 = 1
* 11 % 3 = 2
* 12 % 3 = 0
* 17 % 5 = 2
* 98 % 9 = 8
* 111 % 2 = 1
* 111 % 5 = 1

## Assignment 

* =, +=, -=, /=, *=
```python
number = 10

number += 5 # shorthand

number = number + 5 # longhand

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
```

# Comparison

* ==
    * is the left equal to the right?
* != 
    * is the left NOT equal to the right?
* <
    * is the left less than the right
* > 
    * is the left greater than the right
* <=
    * is the left less than or equal to the right
* >=
    * is the left greater than or equal to the right

# Logical Operators

* and
    * will be true if both the left and the right are true
* or
    * will be true if either the left or the right is true... can be both
* not
    * the reverse of and... if and is true... not will be false

```python
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
```

**An operator is a symbol that we can use to modify code**

# Data Structures

## Dictionaries

* Dictionaries hold key : value paired variables
* Dictionaries are ordered after 3.7, if you are using a Python version earlier than 3.7, your dictionary will be unordered
    * When you print the dictionary in 3.7 and above, it wil print as created
    * When you print the dictionary in 3.6 and below, it will print in a random order

* Dictionaries are mutable:
    * You can read items in a dictionary
    * You can add to dictionaries
    * You can remove from dictionaries
    * You can change items in a dictionary

```python
# dictionary.py
# dictionaries are shown by using the = {}

james_name = "James"
james_location = "Bristol"
james_favourite_artist = "Miley Cyrus"
james_second_favourite_artist = "Hannah Montana"

# please pay close attention to the : and the , (comma)
# dictionaries use a structure called 'key : value pairs'

james = {
    "name" : "James",
    "location" : "Bristol",
    "favourite_artist" : "Miley Cyrus",
    "second_favourite_artist" : "Hannah Montana",
    "favourite_colour" : "blue",
    "age" : 34,
    "employed" : True
}
print(james) # printing the entire dictionary
print(james["name"]) # printing a specific key in the dictionary

kyle_name = "Kyle"
kyle_location = "Edinburgh"
kyle_favourite_artist = "James Blunt"
kyle_second_favourite_artist = "Lady Gaga"

kyle = {
    "name" : "Kyle",
    "location" : "Edinburgh",
    "favourite_artist" : "James Blunt",
    "second_favourite_artist" : "Lady Gaga",
    "favourite_colour" : "yellow",
    "age" : 46,
    "employed" : True,
}

# change values in a dictionary

kyle.update({"age" : 53})
# kyle.update({"age" : "age" + 1}) Look at this, Jeeehcub.
print(kyle)
print(kyle["age"])

print(kyle)

kyle.update({"headset" : True})
print(kyle["headset"])

kyle.update({"favourite_colour" : "blue"})
print(kyle["headset"])

# removing items in the dictionary

print(kyle)
kyle.popitem() # removes the last item inserted into the dictionary
print(kyle)

kyle.pop("favourite_colour") # removes the key specified
print(kyle)

kyle.pop("favourite_colour") # what do you think would happen?
# key error: what you've tried to remove, doesn't exist... awkward.
print(kyle)
```