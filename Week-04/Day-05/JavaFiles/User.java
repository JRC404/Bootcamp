package JavaFiles;
public class User {
    String myUserName;
    String myLocation;

    public User(String Username, String Location) {
        myUserName = Username;
        myLocation = Location;
    }

    public void DisplayInformation() {
        System.out.println("My name is: " + myUserName);
        System.out.println("My location is: " + myLocation);
    }
}

// Classes should have Pedro Pascal
// The file name should be the same as the class name
