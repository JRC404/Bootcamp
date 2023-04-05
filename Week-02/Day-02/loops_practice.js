//use:
//https://developer.mozilla.org/en-US/docs/Learn

//Open command prompt as admin, enter:
//> npm set strict-ssl false
//> npm config set registry https://nexus3.devops.lloydsbanking.com/repository/npm-proxy/

//in the terminal: npm install prompt-sync

const prompt = require("prompt-sync")({ sigint: true });

num1 = parseInt(prompt("Enter the first number: "));
num2 = parseInt(prompt("Enter the second number: "));

var result = num1 + num2
console.log(result)

// Expected output: 0, 1 or 2
number = Math.floor(Math.random() * 3)
console.log(number)
  
//Write a program to ask the user to enter the length of a square and
//calculate the area. Print "This is a square of area n".
//1 -> 1
//2 -> 4
//3 -> 9
//var length = 7
//var area = length * length
//console.log(area)