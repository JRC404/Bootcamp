// the double is the DEFAULT type for decimal numbers in C#
// double is decimal number - of greater accuracy than a float
//by default C# thinks that decimanl numbers e.g. 13.15 as 'doubles' not 'floats'
double doubleNumber = 13.15;
int intNumber = 10;

// I now want to add an int and a double 
double mixedResult = doubleNumber + (double)intNumber; //explicit casting
Console.WriteLine("mixedResult: " + mixedResult);

//c can implicitely cast a int to a double because an int has less information than a double
// double = double + int and that's OK because of implicit casting
double mixedResultTwo = doubleNumber + intNumber; 
Console.WriteLine("mixedResultwo: " + mixedResultTwo);


// int = double + int and that is NOT OK - you cannot implicetely cast LARGE things (doulbe) into small things (int)
//int mixedResultThree = doubleDecNumber + intNumber; //implicit casting - ERROR
//Console.WriteLine("mixedResulThree: " + mixedResultThree);

int mixedResultFour = (int)doubleNumber + intNumber; //explicit casting
Console.WriteLine("mixedResulFour: " + mixedResultFour);