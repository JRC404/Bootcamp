class Hero {
    constructor(name, power, weakness) {
        this.name = name
        this.power = power
        this.weakness = weakness
    }
}

class Villain extends Hero {
    constructor(name, power, weakness) {
        super(name, power, weakness)
    }

    defeat() {
        console.log("The villain has been defeated.")
    }
}

class Antihero extends Hero {
    constructor(name, power, weakness) {
        super(name, power, weakness)
    }

    defeat() {
        console.log("The antihero has been defeated.")
    }
}

const homelander = new Villain("Homelander", 100, "joy")
homelander.defeat()

const batman = new Hero("Batman", 100, "talking in a high pitched voice")
batman.defeat()

/* 
5. 🦸 Superheroes
Create a class called Hero that has properties for a superhero's name, power, and weakness. Create two subclasses called Villain and Antihero that inherit from the Hero class. Add a method to each subclass called defeat that logs a message saying that the villain or antihero has been defeated.
*/