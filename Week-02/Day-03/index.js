let myName; // declaration
myName = "Jehcub"; // definition

// declaration and definition can happen in one line:
// let myName = "Jacob";

// ; in JavaScript?

// If you've come from Python, very rarely will you use ;
// If you've come from C#, Java, Objective-C, C, C++ etc, then you'll use semi-colons

try {
    for (let i = 0; i < 10; i++) {
        console.log(i);
    }

    console.log(i)
} catch (error) {
    if (error instanceof ReferenceError) {
        console.log("You created a reference error, you idiot.")
        // You created a reference error, you idiot.
    }
    else {
        console.log("Generic error. Don't know it. Sorreh.")
    }
}

// ReferenceError: i is not defined at Line 22

console.log("Wassup.")