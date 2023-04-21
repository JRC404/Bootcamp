using Firebrand; // I have now brought Firebrand into this file to use

namespace Lloyds
{
    public class Program
    {
        public static void Main(string[] args)
        {
            User jacob = new User("Jacob", "Manchester");
            Car drew = new Car("Drew", "Jaguar Land Rover", 1999, false);

            Firebrand.Example example = new Firebrand.Example();
            // Example example = new Example();

            example.addition(15, 10);

            Console.WriteLine(jacob.myUserName);
            Console.WriteLine(jacob.myLocation);

            drew.DisplayCarInformation();
            
            jacob.DisplayInformation();
        }
    }
}