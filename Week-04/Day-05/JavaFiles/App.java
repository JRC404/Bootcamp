package JavaFiles;
public class App {
    public static void main(String[] args) {
        
        User jacob = new User("Jacob", "Manchester"); 
        Car drew = new Car("Drew", "Jaguar Land Rover", 1999, false);
        System.out.println(jacob.myUserName);
        System.out.println(jacob.myLocation);
        
        drew.DisplayCarInformation();
        jacob.DisplayInformation();
    }
}