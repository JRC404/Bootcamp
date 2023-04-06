//functions and methods

// function: A named section of a program that does a SPECIFIC task
// a method is the same thing, but it is defined inside a class
//functions need the 'function' keyword before the name while methods do not
// there should be a verb in the name
// a function for converting fahrenheit to celsius
// we put 'parametres'/'arguments' in the brakets ()
// this function is taking in the degrees in fahrenheit as an argument
//function definition
/*
function convertTemperature(fahrenheit) {
    // the brackets () are there to indicate that the subtraction needs to happen before the multiplication and division
    //this is a function variable
    celsius = (fahrenheit - 32) * 5 / 9 
    return celsius 
}
*/

//function call
//const celsiusTemperature = convertTemperature(50)

// in JavaScript we can acceess function variables
//console.log("The temperature today is: " + celsiusTemperature + " degrees celsius")

/*
Exercise:
Have a function that accepts two different names as strings
and returns '[string1] and [string2] are friends'
then print your returned string
*/


/*
Exercise 1:
Write a function which 
takes in a number
returns Boolean true if and only if the integer is an even number between 1 and 1000
returns Boolean false otherwise
call this function inside an if statement
*/
number = 1000

function numberCheck(number) {
    if (number%2==0 && number>=1 && number<=1000) {
        return true
    }
    else {
        return false
    }
}

result = numberCheck(number)
console.log(result, number)




/*
Exercise 2:
Write a function which 
takes a single argument "height " 
displays a "ramp" of this height made up of "*" characters 
hint: use a two dimentional loop - search for two dimentional loop javascript

*
**
***
****
*/


/*
 * This code is throwing an error if the input (parametres) for a function is not the right type (isNaN). Do the same for Exercise1 and Exercise2, and do something meaningfull (eg print something) if you catch the error. 
 */
function getRectArea(width, height) {
    if (isNaN(width) || isNaN(height)) {
      throw new Error('Parameter is not a number!');
    }
  }
  
  try {
    getRectArea(3, 'A');
  } catch (e) {
    console.error(e);
    // Expected output: Error: Parameter is not a number!
  }

