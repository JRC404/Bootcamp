try
{
    int age = 57;
    if (age < 0)
    {
        throw new ArgumentException("Age cannot be negative.");
    }
    Console.WriteLine("You are " + age + " years old.");
}
catch (ArgumentException ex)
{
    Console.WriteLine("Sorry, that's not a valid age. " + ex.Message);
    // what is the exception message?
}


// Console.WriteLine("How many slices would you like?");
// int numberOfSlices = int.Parse(Console.ReadLine());

// try
// {
//     if (numberOfSlices < 1)
//     {
//         throw new ArgumentException("You can't cook a pizza with fewer than one slice, silly!");
//     }

//     Console.WriteLine("Cooking your damn pizza.");
// }
// catch (ArgumentException ex)
// {
//     Console.WriteLine("Oops, something went wrong: " + ex.Message);
//     Console.WriteLine("Please try again with a valid number of slices.");
// }

