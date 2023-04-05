class Person {
    constructor(fullName, age, location, legs) {
        this.fullName = fullName
        this.age = age
        this.location = location
        this.legs = legs // having this below employer doesn't change the code but isn't logically sound
        this.employer = "Lloyds Banking Group"
        // each new instance will by default have Lloyds Banking Group as its value, this can be modified later
    }

    birthday() {
        this.age += 1
        // this.age++
    }

    moveCity(chosenCity) {
        this.location = chosenCity 
    }

    // create a birthday method
    // moveCity... this one should be fun!
}


const terry = new Person("Terry Kuhl", 28, "North London", 2)
terry.moveCity("Leeds")
console.log(terry.location)
terry.birthday()
console.log(terry.age)


const kyle = new Person("Kyle McKenzie", 56, "North London", 2)
console.log(kyle) // fullName = Kyle M, age = North London, location = 2, legs = undefined
kyle.birthday()
kyle.moveCity() // if I leave this blank?
console.log(kyle.location)

const jon = new Person("Jonathan Stevens", 39, "Halifax", 2)
const andre = new Person("Andre Patterson", 29, "South London", 2) // creating a new instance of Person
const george = new Person("George", 17, "Timbuktu", 2)

// console.log(terry) // will employer show in this print?
// console.log(jon) // will employer show in this print?
// console.log(andre) // will employer show in this print?

//? fullName, age & location are arguments / parameters that the constructor is going to use to build the Person class

// storing the information given to the constructor - receive the information from somewhere and is given to...
// this.fullName is assigning whatever the value of fullName in the new Person object is to the fullName variable in the template / class
// using the new keyword, we are creating a NEW instance of the Person class
// instance = version / copy / event... it's another thing