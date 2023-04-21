public class Example {
  public static void main(String[] args) {

    /* 
     *  All the data types that follow are called primitives - start with lower case eg int
     */

    // single quotes for a 'char'
    char character = 'A';
    System.out.println(character + " ");

    // number is calculated like so: 2 + (4 / 2) because divission has precedence over addition
    int number = 2 + 4 / 2;
    System.out.println(number + " ");

    //if you want the addition to happen before the divission you have to indicate this with brackets
    int numberTwo = (2 + 4) / 2;
    System.out.println(numberTwo + " ");

    //also uses camelCase
    double anotherNumber = 13.4;
    System.out.println(anotherNumber);

    //if I add a double and and integer what will the result be
    //like C# Java will autocast UP (implicit) eg it will cast and int to a double in this example
    //this is done implicitly because no information is lost
    double result = 13.4 + 6;   // - / * %
    System.out.println(result);

    //in this situation I am casting DOWN needs to be explicit
    //this is done explicitely because information WILL be lost
    int resultTwo = (int)13.4 + 6;
    System.out.println(resultTwo);

    boolean decision = false;
    System.out.println(decision);


    /*
     * msg is an object of class 'String'
     * double quote for a "String"
     * a String is not a 'primitive' but an 'object' - that's why it is in capitals
     * classes start with a Capital eg String
     */
    String msg = "Hello World ... ";
    System.out.println(msg + " ");     // string concatenation 
    System.out.println(msg.length());  // small differences with c sharp
    System.out.println(msg.toUpperCase());

    int whereIsTheW = msg.indexOf("W");
    System.out.println(whereIsTheW);

    System.out.println("My name's \n George");


    // Math class - has mathematics methods so we don't have to write them 
    System.out.println( Math.max(3, 15) );

    double rand = Math.random();
    int randomInt = (int)(50 * rand);
    System.out.println(randomInt); // Generates a random number from 0-1

    // this is a boolean OR ||
    // this is a boolean AND &&
    // this is a boolean NOT !


    // 
    int x = 50;
    int y = 50;
    if (x > y) {
      System.out.println("x is bigger than y");
    }
    else if (x < y) {
      System.out.println("y is bigger than x");
    }
    else {
      System.out.println("they are equal");
    }

    int num = 0;
    while (num < 10){
      System.out.println(num);
      num++;
    }

    for (int i = 10; i > 0; i--) {
      System.out.println(i);
    }
    
    // arrays are of defined sise
    // and they are of a particular type
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

    //shorthand for loop for an array
    for (String i : cars) {
       System.out.println(i);
    }

    // for an array you do cars.length
    for (int i = 0; i < cars.length; i++) {
      System.out.println(cars[i]);
    }

  }
}