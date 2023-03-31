#prints "this is a paragraph" 
#this is a function definition
#function names should be VERBS
#functions should do ONE thing
def print_paragraph():
    print("this is a paragraph")

# print whatever I say 
#this is a function definition
#when the function is being called, one argument/parameter will be used called 'words'
def simon_says(words): 
    print(words)


#variable names should be NOUNS
simon_1 = "hello"
simon_2 = "goodbye"
#simon_says(simon_1) #function call with parameter/argument
#simon_says(simon_2)


'''
Write a function which:
    takes in a number
    print true if and only if 
        the integer is an even number 
        and between 1 and 1000
    print false otherwise
'''

#--------1------1000-----  odd/even
number = int(input("please enter a number "))
if number % 2 == 0 and number >= 1 and number <= 1000:
    print("true")
else:
    print("false")






