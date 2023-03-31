'''
try: #attempt to run this code
    print(x)
except: #if the code cannot run (an exception is thrown)
    print("x is not defined")

y=4
print(y)
'''


# convert this program to keep asking for a number (loop)
# until the user actualy correctrly enters an integer
i = 1
limit = 3
while i<=limit:
    try:
        x = int(input("enter a number "))
        y = x * 2
        print(y)
        break
    except ValueError:
        if i!=limit:
            print("Sorry you should have entered a number. Try again...")
        i += 1

print("You are an idiot!")
