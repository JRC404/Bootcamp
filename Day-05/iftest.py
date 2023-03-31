age = int(input("Tell me your age: "))

if age < 18: # yes
    print("Leave.")
    # break won't work because it is not inside of a loop
elif age < 30: # yes
    print("Young persons discount")
elif age < 60: # yes
    print("Full price. You don't need a discount")
elif age < 100: # yes
    print("£5 off your ticket")
else: 
    print("Free entry, you're old. Very old. Fair play.")

favourite_colour = 12

if favourite_colour == "purple":
    print("Nice choice")
elif favourite_colour == "orange":
    print("Good choice")
else: 
    print("I don't know that colour... try again")

# error?
# would work but doesn't know what to do
# leave?
# print all options?
# print all except else
# print all of the ones relevant to you