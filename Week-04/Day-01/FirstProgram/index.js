let myFloat = 57.75;
let myAge = 0;

if (myFloat < 58) {
    console.log("Congratulations on being less than 58");
}
else if (myFloat < 100) {
    console.log("Well done on being less than 100");
}
else {
    console.log("Oh. Awkward.");
}

while (myAge < 100) {
    console.log(myAge);
    myAge++;
    // myAge += 1
}


for (let i = 0; i < 100; i++) {
    console.log(i);
}

let myName = "Jacob";

switch (myName) {
    case "Jacob":
        console.log("Hello, Jacob");
    case "John":
        console.log("Hello, John");
    default:
        console.log("Oh, you must be Kasim");
        break;
}