// 3. 🏀 Class: BasketballPlayer Create a class called BasketballPlayer that has a constructor which sets a name and team property for the basketball player. Add a method called shoot that logs the string "<name> shoots the ball!" to the console.

// class BasketballPlayer
// constructor that holds name and team
// method that logs name shoots the ball

class BasketballPlayer {
    constructor(name, team) {
        this.name = name
        this.team = team
    }

    shoots() {
        console.log(this.name + " shoots the ball.")
    }
}

const lebron = new BasketballPlayer("Lebron James", "LA Lakers")
lebron.shoots()