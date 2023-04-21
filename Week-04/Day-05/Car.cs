// TODO: Create a Car class or something of your choice that has:
    // TODO: Remember your namespace Lloyds {}
    // TODO: 2 strings minimum, an integer, a boolean
    // TODO: Create the constructor... remember the names can't be the same
    // TODO: Create a method like DisplayInformation
    // TODO: Create 2 instances of the Car class in Program.cs

namespace Lloyds {
    public class Car {
        public string carName;
        public string carMake;
        public int carYear;
        public bool hasTyiyres;
        public Car(string CarName, string CarMake, int CarYear, bool HasTyiyres) {
            carName = CarName;
            carMake = CarMake;
            carYear = CarYear;
            hasTyiyres = HasTyiyres;
        }

        public void DisplayCarInformation() {
            Console.WriteLine("My car is called " + carName);
            Console.WriteLine("My car was made by " + carMake);
            Console.WriteLine("My car was made in " + carYear);
            
            if (hasTyiyres) {
                Console.WriteLine("Yes, my car has tyiyres.");
            }
            else {
                Console.WriteLine("Who stole my tyiyres?");
            }
        }
    }
}