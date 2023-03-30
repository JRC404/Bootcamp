#the exercise from our ifelsechallinge...
'''
print("Menu")
print("1. Music")
print("2. History")
print("3. Design and Technology")
print("4. Exit")
choice = input("\nPlease enter your choice: ")

if choice == "1":
    print("Music is the food of love")
elif choice == "2":
    print("History is bunk")
elif choice =="3":
    print("Not as easy as you think...")
else:
    print("Goodbye")
'''

#becomes

#works with any string input that can be cast into an int
while(True):
    print("Menu")
    print("1. Music")
    print("2. History")
    print("3. Design and Technology")
    print("4. Exit")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        print("Music")
    elif choice == 2:
        print("History")
    elif choice == 3:
        print("Design and Technology")
    else:
        print("Goodbye")
        break



i = 1
while i <= 10:
    print(i)
    i = i + 1

for n in range(1,11):
    print(n)
    
