/*
for (int i = 0; i < 5; i++) {
  Console.WriteLine(i);
}
*/

/*
exercise #1
- print every second number backwards from 50 to 2
*/

/* 
exercise #2
1 - take in a number from the user
2 - if the number is 1 print 'success'
3 - else print 'try again'
4 - do this in a loop, if the number is 1 print 'success' and exit
*/

/*
arrays - the type followed by '[]' equals (assignment operator) '{}'
in C# you CANNOT have mixed type arrays
string[] cars = {"Saab", "Volvo", "BMW"};
int[] numbers = {23, 16, 58};

Console.WriteLine(cars[2]);
Console.WriteLine(numbers[1]);

//cars.Length will give use the array lenght
Console.WriteLine(cars.Length);
*/

/*
using a for loop to move through the array
you need to start at 0 (first index of this array)
you need to end at cars.Length-1

for (int i = 0; i < cars.Length; i++) {
  Console.WriteLine(cars[i]);
}
*/

/*
we are getting each one of the numbers in the 'numbers' array, 
which is named 'number', an int, for each itteration in this loop

foreach (int number in numbers) {
    Console.WriteLine(number);
}
*/

/*
exercise #3
- Write a program to generate 10 random numbers between 1 and 10, and print out
the 10 numbers and the total of the numbers
*/

/*
exercise #3.1: loops (2 dimensional)
Extend the program in Exercise 1 to repeat the generation of 10 random numbers
1000 times. Do not print out the random numbers or the total of each set of 10
numbers - just print the average of the totals at the end of the program.
*/

/*
exercise #4
arrays and foreach:
1 - make an integer
2 - ask the user to enter another integer
compare the two integers and print:
    3 -	success if they have entered the same integer
    4 -	failure if the have entered a different integer
do the same but compare the integer inputted with an array of integers
    5 -	print a message for every number in the list
    6 -	print a message only at the end
    7 -	'break' if the number is found
*/
//int age = Convert.ToInt32(Console.ReadLine());

/*
exercise #5
1- Define an array containing the names of students in a class.
2- Ask the user to input the exam results for each student. 
3- Print a report showing the data with column headings
    Student     Exam mark

4- At the end of the report, print the name of the student with the highest mark, and the
mark obtained.
*/

/*
exercise #5..1
Write a program to accept a student name, and the marks obtained on 10 weekly
tests. Print the name, average mark, top three marks and bottom three marks.
*/

/*
//this will try to apply an int to an array index
//if there is no such array index it will print the first element of the array
int[] numbers = {23, 16, 58};
try {
    int i = Convert.ToInt32(Console.ReadLine());

    // the exception happens on this line - you will see no output
    // from here it will go straight to the 'catch' part
    Console.WriteLine(numbers[i]); 

    //nothing under this until the block is closed } will run
}
catch (Exception e) {
   Console.WriteLine(numbers[0]);
}
*/

/*
//this will convert user input to an int
//if it fails to do so it will print a silly message
Console.WriteLine("Enter your age:");
try {

    // the exception happens on this line - you will see no output
    // from here it will go straight to the 'catch' part
    int age = Convert.ToInt32(Console.ReadLine());

    //nothing under this until the block is closed } will run
    Console.WriteLine("Your age is: " + age);
}
catch (Exception e) {
   Console.WriteLine("That's not a number silly");
}
*/

/*
Console.WriteLine("Enter your age:");
try {
    int age = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Your age is: " + age);
}
catch (Exception e) {
   Console.WriteLine("That's not a number silly");
}
*/

/*
//keep asking the user to enter a number, and stop when they do 
int age;
while(true) {
    Console.WriteLine("Enter your age:");
    try {
        string strAge = Console.ReadLine();

        // this is the offending line 
        // if an exception is thrown here the lines after it will NOT BE REACHED
        age = Convert.ToInt32(strAge); 

        break; // not reached (in case of exception)
    } 
    catch (Exception e) {
        Console.WriteLine("That wasn't a number");
    }
}

// an int has been provided it is now safe to run the rest of the code
Console.WriteLine("Your age is: " + age );
*/