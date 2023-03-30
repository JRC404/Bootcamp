favourite_artists = [ "Miley Cyrus", "Hannah Montana", "James Blunt", "Lady Gaga", "Queen" ]

# python allows us to store multiple data types inside of the same list
# please try and keep list items to the same data type

# Lists are ordered
# List items have an index
# Lists can be added to
# Lists can have items removed
# Lists can have their items changed

# Index in Python start at 0

print(favourite_artists[0]) # Miley Cyrus
print(favourite_artists[3]) # Lady Gaga
# print(favourite_artists[6]) #! IndexError: list index out of range
print(favourite_artists[-1]) # refers to the last item in the list
# print(favourite_artists[-6]) #! IndexError: list index out of range 

favourite_artists[0] = "miley cyrus" # this has changed Miley Cyrus to miley cyrus

# print(favourite_artists[0])

#? how do we change multiple items in the list?

#? append?
favourite_artists.append("George Ezra") # adding George Ezra to the end of the list

#? insert
favourite_artists.insert(2, "Cher") # what has happened 'ere?
# insert adds Cher to the position: index 2
#? Option 01: Miley Cyrus, Hannah Montana, Cher
#? Option 02: Miley Cyrus, Hannah Montana, James Blunt, Cher
print("--------------")
print(favourite_artists)
# ['miley cyrus', 'Hannah Montana', 'Cher', 'James Blunt', 'Lady Gaga', 'Queen', 'George Ezra']

# removing an item using a specific index from a list

favourite_artists.pop(1) #? what will this do?

print("--------------")
print(favourite_artists)
# removing a specific item from a list using a name

favourite_artists.remove("George Ezra") # this will remove Geore Ezra from the list

print("--------------")
print(favourite_artists)

favourite_artists.append("ZZ-Top")
favourite_artists.append("Rebecca Black")
favourite_artists.append("ZZ-Top")

print("--------------")
print(favourite_artists)

favourite_artists.remove("ZZ-Top")

print("--------------")
print(favourite_artists)

# pop

favourite_artists.pop() # last item removed

print("--------------")
print(favourite_artists)

# del 

del favourite_artists[4] # removes the 4th index item
# but try and use pop and remove as del is hungrier in terms of memory management and allocation

# print(favourite_artists.count())

favourite_artists.clear() # clears the list
# clears the list of items but the list remains

print("--------------")
print(favourite_artists)

# my_list_choice = ["something in here"]
# append, insert(), pop(), remove()
#? Create a list of your choice - and use 3 appends, 3 inserts, 2 pops and 2 removes

# Sorting items in a list? Is it possible?
# If it is, what can we do to sort?

favourite_colour = ["purple", "orange", "pink"]
favourite_colour.append("green")
favourite_colour.insert(1, "yellow")
favourite_colour.pop()
favourite_colour.pop(1) # remove index 1
favourite_colour.remove("purple")
favourite_colour[0] = "blue"
print(favourite_colour)