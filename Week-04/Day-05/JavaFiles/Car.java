package JavaFiles;

// TODO: Create a Car class or something of your choice that has:
    // TODO: Remember your namespace Lloyds {}
    // TODO: 2 strings minimum, an integer, a boolean
    // TODO: Create the constructor... remember the names can't be the same
    // TODO: Create a method like DisplayInformation
    // TODO: Create 2 instances of the Car class in Program.cs

public class Car {
    public String carName;
    public String carMake;
    public int carYear;
    public boolean hasTyiyres;
    public Car(String CarName, String CarMake, int CarYear, boolean HasTyiyres) {
        carName = CarName;
        carMake = CarMake;
        carYear = CarYear;
        hasTyiyres = HasTyiyres;
    }

    public void DisplayCarInformation() {
        System.out.println("My car is called " + carName);
        System.out.println("My car was made by " + carMake);
        System.out.println("My car was made in " + carYear);
        
        if (hasTyiyres) {
            System.out.println("Yes, my car has tyiyres.");
        }
        else {
            System.out.println("Who stole my tyiyres?");
        }
    }
}

