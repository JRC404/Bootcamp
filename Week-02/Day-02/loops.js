let myFavouriteThings =  ["Miley Cyrus", "The colour purple", "cheese", "shoes", "hoodies"]

let counter = 0
while (counter < myFavouriteThings.length) {
    console.log(myFavouriteThings[counter])
    counter++
}

for (let i = 0; i < myFavouriteThings.length; i++) {
    console.log(myFavouriteThings[i]);
}
// 1. initialisation: let i = 0
// 2. condition: i < myFavouriteThings.length
// iteration / increment / decrement: i++