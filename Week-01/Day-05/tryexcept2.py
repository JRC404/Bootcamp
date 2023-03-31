file_name="tryexcept.py"

# 1- get the user to type the file
# 2- put this code in a function and call it with filename
# 3- print the contents of the folder before you ask the user to type a file 
try:
    f = open(file_name, "r") #opened the file for (r)eading
    file_contents = f.read() #put all the file contents in a string called file_contents
    f.close()
    print(file_contents)
except FileNotFoundError:
    print("File not found:", file_name )