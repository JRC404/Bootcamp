// string: "My string content" OR 'My string content'
// number - handles both int and float effortlessly
// boolean - true / false
// null: empty
// undefined: no value has been defined

// camelCasing for the majority of things in JS
// PascalCasing is used for Classes and sometimes objects

let myName = "Jacob" // Jacob
let myAge = 57 // 57
let lightOn = true // true
let emptyVariable = null // null
let undefinedVariable; // undefined

// TODO: Print these 5 variables to console
console.log(myName)

let myFavouriteArtist = "Miley Cyrus"
// IF statement that checks if it's Miley, Lady Gaga, Jimmy Blunt, Queen, OR something else is our favourite artist

if (myFavouriteArtist == "Miley Cyrus") {
    console.log("The only choice.")
} 
else if(myFavouriteArtist == "Lady Gaga") {
    console.log("Okay, she's pretty good.")
}
else if(myFavouriteArtist == "James Blunt") {
    console.log("He's a cheery fella.");
}
else {
    console.log("Who?")
}

let learnerName = "Yuhan Zhao"

switch (learnerName) {
    case "David Goodman":
        console.log("Hi, David")
        break;
    case "Kyle McKenzie":
        console.log("Hi, Kyle")
        break;
    case "Yuhan Zhao":
        console.log("Hi, Yuhan")
        break;

    default:
        console.log("Oh, don't know you... Sorreh.")
        break;
}

let carMake = "Mercedes"

switch (carMake) {
    case "Mercedes":
    case "Audi":
    case "BMW":
        console.log("German Makes")
        break;
    case "Toyota":
    case "Honda":
    case "Nissan":
    case "Subaru":
        console.log("Japanese Makes")
        break;
    case "Aston Martin":
    case "Rolls-Royce":
    case "Lotus":
        console.log("British Makes")
        break;
    default:
        break;
}
// please remember your breaks in the switch case, as this will allow the switch to stop once the correct answer / default has been given
// line-wrap = alt + z