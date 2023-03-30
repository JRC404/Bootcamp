'''
in-class exercise
1- Define a list containing the names of students in a class. 
2- Ask the user to input the exam results for each student. 
3- Print a report showing the data with column headings
    Student     Exam mark

4- At the end of the report, print the name of the student with the highest mark, and the
mark obtained.
'''

#1- Define a list containing the names of students in a class. 
student_names = ['George', 'Mark', 'Sophie', 'Hassan', 'Mariam']
marks = []


# 1 student
# student_mark = int(input("please enter a mark"))
# print(student_mark)

# 2- Ask the user to input the exam results for each student. 
for item in student_names:
    print("please enter a mark for", item )
    student_mark = int(input(""))
    print(item, student_mark)

    #store the mark yo the marks list
    marks.append(student_mark)
 

# 3- Print a report showing the data with column headings
#     Student     Exam mark
print ("Student \tExam mark")

#student_names = ['George', 'Mark', 'Sophie', 'Hassan', 'Mariam']
i = 0
array_length = len(marks)
while i < array_length:
    print (student_names[i], "\t\t", marks[i])
    i = i + 1




'''
exercise 1: loops 
Write a program to generate 10 random numbers between 1 and 10, and print out
the 10 numbers and the total of the numbers.
'''
#exercise 1
import random
total = 0
for num in range(10):
    num = random.randint(1,10)
    print(num)
    total += num
print("Total =",total)




'''
exercise 2: loops (2 dimensional)
Extend the program in Exercise 1 to repeat the generation of 10 random numbers
1000 times. Do not print out the random numbers or the total of each set of 10
numbers - just print the average of the totals at the end of the program. Is the
answer what you would expect?
'''
#exercise 2
import random

overallTotal = 0
numberOfTests = 1000
for test in range(numberOfTests):
    total = 0
    for num in range(10):
        num = random.randint(1,10)
        total += num
#don't print if your number of test is more than about 100!
#    print("Total =",total)

    overallTotal += total
averageTotal = overallTotal/numberOfTests
print("\nAverage total =",averageTotal)

input("\nPress Enter to exit ")



'''
exercise 3
Write a program to accept a student name, and the marks obtained on 10 weekly
tests. Print the name, average mark, top three marks and bottom three marks.
(Use sortedMarks = sorted (markList, reverse = True) to sort the list.)
'''












#exercise 3

markList = []
total = 0
name = input("Enter student name: ")
for test in range(10):
    testNumber = test + 1
    mark = int(input("Enter mark for test "+ str(testNumber) +": "))
    total+= mark
    markList.append(mark)

average = round(total/10,1)
sortedMarks = sorted(markList, reverse = True)
#print("Mark list",markList)
#print("Sorted mark list",sortedMarks)
print(name)
print("\nTop 3 marks")
for n in range(3):
    print(sortedMarks[n])
print("\nBottom 3 marks")
#newList = sortedMarks[7:10]
for n in range(9,6,-1):
    print (sortedMarks[n])

print("\nAverage mark: ", average)    
input("\nPress Enter to exit ")
