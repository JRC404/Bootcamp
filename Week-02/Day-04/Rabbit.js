class Rabbit {
    constructor(HP, attack) {
        this.HP = HP
        this.attack = attack
    }

    fight(otherRabbit) {
        otherRabbit.HP -= this.attack
        console.log(otherRabbit.HP)
    }
}

const buggs = new Rabbit(100, 20)
const steve = new Rabbit(100, 10)

buggs.fight(steve) // buggs has an attack of 20... what is Steve's HP going to be?