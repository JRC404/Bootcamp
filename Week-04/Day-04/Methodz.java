public class Methodz {

    /*
     * String[] args is the parameter that we are passing to main
     * the way to think about the 'main' function is were writing code outside a function in other languages - when the program runs this is the first thing that will be executed
     *
     */
    public static void main(String[] args) {
        // your method call needs to follow the method signature, for example in how many and of what type the arguments are
        String printMe = "";
        if (args.length > 0) {
            printMe += printSmth(2, args[0]);  // method call
        }
        if (args.length > 1) {
            printMe += printSmth(5, args[1]);  // method call
        }
        System.out.println(printMe);
    }
    
    /*
     * Method definition:
     * static we will cover soon!
     */ 
    static String printSmth(int x, String upliftingText) {    // this line is the method signature
        String returnString = "";
        for(int i = 0; i < x; i++) {
            returnString += upliftingText + "\n";
        }
        return returnString;
    }

}