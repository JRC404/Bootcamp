/*
// simple while loop, counting up
var i = 1
while (i < 6) {
    console.log("The number is " + i)
    //i = i + 1
    //i += 1
    i++
}
*/

/*
// simple while loop, counting down
var i = 10
while (i >= 1) {
    console.log("The number is " + i)
    //i = i + 1
    //i += 1
    i--
}
*/

/*
// while loop: CHECK first, then DO
var i = 0
i = 34
text = ""
while (i < 10) {
    text += "The number is " + i + "\n"
    i += 1
}
console.log(text)
*/

// do-while loop: DO first, then CHECK
/*
var i = 0
i = 34
text = ""
do {
    text += "The number is " + i + "\n"
    i += 1
}
while (i < 10)

console.log(text)
*/

/*
const prompt = require("prompt-sync")({ sigint: true });
const textVar = prompt("What's your name?");
console.log("Your name is "  + textVar);
*/


//while loop with a break
/*
var i = 1
while(i < 10) {
    console.log("i is " + i)
    if(i==3) {
        //console.log("WOW! i is now " + i + "!!!!!!!")
        break
    }
    i++
}
*/


// simple while loop, counting up
/*
var i = 1
while (i < 6) {
    console.log("The number is " + i)
    i++
}
*/

//FOR loop - we will use (from the while loop above):
// var i = 1
// i < 6 
// i++
// you will use this when you want to loop X times
/*
x = 4
for(var i = 1; i < x; i++) {
    console.log("The number is " + i)
    if(i==3) {
         break
    }
}
*/

//use with arrays
/*
numbers = [5, 2, 85, 134, 63] //an array called 'numbers'

n = 4
console.log("element " + n + " in the array " + numbers[n])
*/

//for (let x in numbers) {
//    console.log("position " + x + " = " + numbers[x])
//
// cars = ["Saab", "Volvo", "BMW"];
// cars[3] = "Ferrari"
// cars[0] = "Fiat"

// for IN loop -> gives you the array indeces 
// for (let x in cars) {
//     console.log("position " + x + " = " + cars[x])
// }

//for OF loop -> gives you the array elements
// for(let x of cars) {
//     console.log(x)
// }

/*
names = []
names[0] = "Mark"
names[1] = "Sophie"

for(var i = 0; i <= names.length-1; i++) {
    console.log(names[i])
}
*/

/*
cars = ["Saab", "Volvo", "BMW"]
bikes = ["Yamaha", "Honda", "Kawasaki"]
//cars.push("Ferrari")
cars[cars.length] = "Ferrari" //manual push

//cars.pop()
shiftedBrand = cars.pop()
//shiftedBrand = cars.shift()

vehicles = bikes.concat(cars)

joinedCars = vehicles.join(" ") //join all the cars into one string
console.log(joinedCars)
console.log(shiftedBrand)
*/

/*
x = 3
y = 4
// && means AND
if (x==3 && y==4) {
    console.log("x AND y")
}

// || means OR
if (x==3 || y==4) {
    console.log("x OR y")
}

// ! means NOT
if(x!=3) {  //the direct opposite of x==3
    console.log("x NOT 3")
}
//alternative notation
if(!(x==3)) {  //the direct opposite of x==3
    console.log("x NOT 3")
}
*/

// start exercise
// make an array
// print it

// exercise 1:
// start a string array
// add it to another string array
// for each array element count how many times the string "hello" is there
// print that number

// exercise 2:
// using 2D arrays
// print the following table:
// 1 2 3
// 2 4 6
// 3 6 9

/*
bikes = [   ["Yamaha", "Honda", "Kawasaki"],
            ["Saab", "Fiat", "Alpha Romeo"] ]

console.table(bikes)
*/