# Day 01 Notes

* What on earth is Python?
* Python Fundamentals
    * Syntax
    * Logic
    * Variables
    * Conditionals

## What is Python?

* Programming Language
    * A very forgiving programming language
    * A very helpful programming language
    * The syntax is very structured

### Python Installed?

```
python --version
```

* python hello.py
* py hello.py

## Powershell basics

* If you get: fwd-i-search: - press ctrl + c to exit and then try saving again

## Python Fundamentals

### Naming Conventions

* Consistency, Clarity

#### Camel Casing
* every new word except the first starts with a capital letter
* everyNewWordExceptTheFirstStartsWithACapitalLetter

#### Pascal Casing
* Every new word including the first starts with a capital letter
* EveryNewWordIncludingTheFirstStartsWithACapitalLetter

#### Snake Casing
* Every word is lower case and split by an underscore
* every_word_is_lower_case_and_split_by_an_underscore

* A naming convention is a standard, it makes no difference to your code except the consistency and structure... the implementation of the code doesn't change one bit.

* Try to be consistent. Do not change naming conventions halfway through your code

## Variables

* Storage place / Box / A location / A container for our data
* variable_name = variable value
* A variable can change

* If you have variables like below:
```python
first_name = "Jacob"
firstName = "Jacob"
first_Name = "Jacob"
First_Name = "Jacob"
print(first_name)
print(firstName)
print(first_Name)
print(First_Name)
```

```python
print("Hello, my name is " + first_name + " " + last_name + ". I am " + age + " years old and I live in " + location + ".")
# You will use a lot of "speech marks", you need to double / triple check where you have used them

print(f"Hello, my name is {first_name} {last_name}. I am {age} years old and I live in {location}.")
```

## Data Types

* **String** - this is displayed with a ""
    * A collection of data / characters
    * "My Name in a String would be Jacob"
    * "asdfghjkl"
* **int** - whole number
    * 14, 85, -898565, 988744
* **float** - decimal number
    * 14.1, 85.25, -898565.258, 988744.01
* **boolean** -  True / False
    * It is one or the other... 

* In Python, we do not need to declare which data type we are using, the language is smart enough (most of the time) to infer which data type you are trying to use

# User Input
```python
# userInput.py

first_name = "Bob"
last_name = "Bobbington"

employer = input("Where do you work?\n")

print(f"{first_name} works at {employer}")

print(type(employer)) # what is the type expected when I type Firebrand?
```

# Conditionals

# Data Structures