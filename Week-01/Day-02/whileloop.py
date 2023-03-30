'''
counter = 10

print("start")
while counter != 2:
    if counter != 5:
        print(counter)
    counter -= 1

print("end")

i = 10 #initial value for i
print("before the loop")

while i<15:
    print("inside the loop i=",i)
    i+=1

print("after the loop")
'''

print("before the loop")

inp = 200
if inp == 1:
    string_input = input("input 1 to continue, anything else to stop ") 
    inp = int(string_input)
    print(inp)

print("after the loop")