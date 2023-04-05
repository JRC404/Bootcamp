# FOLDER STRUCTURE

* Please do not create folders or files with spaces in them
    * Either use camel, pascal or snake casing to create your folders
    * OR seperate those bad boys with a hyphen

# JSON


* .json
* Key-value pair structure
* When you downloaded / installed prompt-sync, you created a package.json
* In future projects, for JavaScript, that uses packages, we will create a package.json before we install anything

* At the start of every JavaScript project, we need to create a package.json file
* Inside of the terminal where our index.js is located, for me it is Day-02, please run the following command:
```
npm init -y
```
* node-package-manager initialise -yes for all options

## Classes and Objects

* Objects on their own are useful but lengthy... and tiresome
```js
let terry = {
    fullName : "Terry Kuhl",
    age : 28,
    location : "North London",
    favouriteArtist : "The Weeknd",
    interestingFact : "5 siblings, likes 2 of them",
    boringThing : "Eats the same food every day. Chicken and rice",
    favouriteThingToDoAt2pmOnASaturday : "Work out"
}

let jon = {
    fullName : "Jonathan Stevens",
    age : 39,
    location : "Halifax",
    favouriteArtist : "UNKLE",
    interestingFact : "can't spell the word uncle"
}
```

### What is a Class?

* In JavaScript, a class is a blueprint / template for our objects