# Functions

* Allow developers to perform a task when we call it
* DRY:
    * Don't repeat yourself
* To recall information: variables, lists, dictionaries, loops or anything... without having to write it all out again

* A function starts with the keyword:
    * **def** - short for definition
    * def light_switch():
* Whitespacing is important, just like in if statements, while loops etc

* A function can take parameters AKA arguments

## A light switch without functions
```python
# light_switch_no_functions.py
light_on = True # True means on, False means off

# I want to be able to switch the light off if it is on, and on if it is off

if light_on: # short hand for light_on == True
    light_on = False
    print("The light has been turned off.")
else:
    light_on = True
    print("The light has been switched on. Pricey.")

if light_on: # short hand for light_on == True
    light_on = False
    print("The light has been turned off.")
else:
    light_on = True
    print("The light has been switched on. Pricey.")

if light_on: # short hand for light_on == True
    light_on = False
    print("The light has been turned off.")
else:
    light_on = True
    print("The light has been switched on. Pricey.")

if light_on: # short hand for light_on == True
    light_on = False
    print("The light has been turned off.")
else:
    light_on = True
    print("The light has been switched on. Pricey.")

```

## A light switch with functions

```python
# light_switch_with_functions.py
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

```

## A function without parameters / arguments
```python
def addition():
    number_one = 1
    number_two = 2
    print(number_one + number_two)
    # number_one and number_two not defined
    # it won't print "number_one + number_two" because it is not in quotes

# without arguments, our addition is always going to print(3) as its answer

addition()
addition()
addition()
addition()
```

## A function with parameters / arguments

```python
def addition(number_one, number_two):
    print(number_one + number_two)


# addition() #! needs two values to give to number_one and number_two
#! TypeError: addition() missing 2 required positional arguments: 'number_one' and 'number_two'

addition(1, 2) # 3
addition(6, 8) # 14
addition(345, 789) # 1134
addition("Jacob", "Reilly-Cooper") # JacobReilly-Cooper
# addition("Jacob", True) # error? JacobTrue?
addition(1234, True) # 1235 because 1234 + 1 (the value of True)
addition(True, 1234) # 1235 - Python is forgiving
# addition("Bob", 1234) # error? Bob1234?
# addition(1234, "Bob") # error? 1234Bob?

# string concatenation
# True = 1, False = 0
```
