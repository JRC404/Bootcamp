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