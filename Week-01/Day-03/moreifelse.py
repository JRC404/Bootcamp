string_mark = input("enter your mark 0-100: ")
mark = float(string_mark)

#int: 4  62  2983
#float: 0.06  45.7834   41.0
#-----------50--------60-------75-------100------
if mark > 100:
    print("invalid mark please enter the mark again")
elif mark >= 75:
    print("you have a grade A")
elif mark >= 60:
    print("you have a grade B")    
elif mark >= 50:
    print("you have a grade C") 
else:
    print("please do your exam again")

print("end")
