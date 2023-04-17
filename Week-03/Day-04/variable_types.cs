//Semicolon at the end of every sentence

//C# is 'strictly typed' which means that we have to provide the 'type' (string, int) on variable declaration - the first time you mention the variable
//the 'type' goes before the variable name 

//a variable of type string
string name;
name = "George";
Console.WriteLine(name);

string anotherName = "Ben";  //variable declaration
Console.WriteLine(anotherName);

anotherName = "John"; //variable assignment / re-assignment
Console.WriteLine(anotherName);

int number = 10;
Console.WriteLine(number);

//variable declaration - the first time you mention the variable - use the type
int anotherNumber = 10;

//variable re-assignment - do not use the type
anotherNumber = 15;
Console.WriteLine(anotherNumber);

//making an int varable and assigning the addition of the values of two other variables
int result = number + anotherNumber;
Console.WriteLine("Result = " + result);

//add variables with numbers 
result = number - 36;
Console.WriteLine("Result = " + result);

// try adding, subtracting, multiplying - use brackets, try modulo (%)
// long is like an int put it is for very large numbers
long longNumber = 12345678;
Console.WriteLine(longNumber);

// float is decimal number
float decNumber = 13.14F;
Console.WriteLine(decNumber);

//user input - for a string
Console.WriteLine("what is your name?");
string userName = Console.ReadLine();  //There's a warning here - I need to look at this later
Console.WriteLine("You have entered: " + userName);

//user input - for a number
Console.WriteLine("what is your age?");
string stringAge = Console.ReadLine();  //There's a warning here - I need to look at this later

//when we convert one type of variable to another type of variable we call that 'casting':
int age = Convert.ToInt32(stringAge); //explicitly converting user input (string) to an int  
Console.WriteLine("You have entered: " + age);