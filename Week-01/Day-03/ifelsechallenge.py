'''
Write a program to ask the user to enter the length of a square and
calculate the area. Print "This is a square of area n".
1 -> 1
2 -> 4
3 -> 9
'''
string_length = input("Enter length of square: ")
length = int(string_length)
area = length * length
print(area)



'''
extension 1:
Write a program to allow the user to enter the length and width of a rectangle and
calculate the area. If the length and width are equal, print "This is a square of
area nn.nn". Otherwise, print "This is a rectangle of area nn.nn".
'''

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = round(length*width,2)
if length == width:
    print("This is a square of area",area)
else:
    print("This is a rectangle of area",area)          


'''
program 2:
Write a program to display a menu of options:
Menu
1. Music
2. History
3. Design and Technology
4. Exit
Please enter your choice:
The user then enters a choice and the program prints a message such as "You
chose History". If they choose option 4, the program prints "Goodbye".
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

input("\nPress Enter to exit ")



'''
program 3:
Write a program to input the value of goods purchased in a shop. A discount is
subtracted from the value to find the amount owed.
If the value is £200 or more, 10% discount is given.
If the value is between £100 and £199.99, 5% discount is given.
Print the value of goods, discount given and amount owed.

'''
goodsValue = float(input("Enter value of goods purchased: "))

if goodsValue >= 200:
    discount = 0.1*goodsValue
elif goodsValue >= 100:
    discount = 0.05*goodsValue
else:
    discount = 0

amountOwed = goodsValue - discount
print("Value of goods:",goodsValue," Discount:",discount, \
      " Amount owing:",amountOwed)
    

