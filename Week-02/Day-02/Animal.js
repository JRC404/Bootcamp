class Animal {
    constructor(name, hungerLevel, energyLevel, strength) {
        this.name = name // these values are going to be given to us by the "user"
        this.hungerLevel = hungerLevel
        this.energyLevel = energyLevel
        this.strength = strength
        this.origin = "Earth" // why is this one not in the parameters?
    }

    eat() {
        this.hungerLevel -= 10
    }

    sleep() {
        this.energyLevel += 10
    }

    train() {
        this.strength += 10
        this.energyLevel -= 5
        this.hungerLevel += 5
    }

}

const terry = new Animal("Terry Kuhl", 100, 5, 80)
console.log(terry)

const nadia = new Animal("Nadia Scally", 6, 5, 30)
console.log(nadia)
nadia.sleep()
nadia.sleep()
nadia.sleep()
nadia.sleep()
nadia.sleep()
nadia.sleep()
nadia.sleep()
nadia.sleep()
nadia.sleep()

nadia.train()

console.log(nadia)