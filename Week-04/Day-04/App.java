
public class App {

    public static void main(String[] args) {

        // calling a Method and

        // assigning the return value of that method

        // as String variable

        // into returnValue

        String returnValue = printSmth(11, "George"); // method call

        System.out.println(returnValue);

        int resultInt; // varable declaration (when you see the variable type it is ALWAYS a
                       // declaration)

        resultInt = multInts(2, 4); // putting the return value of multInts(2, 4) INTO resultINt
        int newResult = multInts(10, 20); // 200
        int answerBox = multInts(20, 5); // 100

        System.out.println(newResult);
        System.out.println(answerBox);
        System.out.println(resultInt);

    }

    /*
     * 
     * This function will multiply two integers and will return the integer result
     * 
     */

    static int multInts(int x, int y) { // in this line I am DECLARING the variables x,y

        int result = x * y; // I am DECLARING the result variable

        return result;
        // returning result means... multInts is going to hold the value of result
    }

    /*
     * 
     * Method definition:
     * 
     * static we will cover soon!
     * 
     * void means it is not returning anything
     * 
     */

    static String printSmth(int x, String upliftingText) { // this line is the method signature

        String returnText = upliftingText + " * " + x; // concatenating Strings and an int

        return returnText;

    }

}