# Week 02. You made it! *insert celebration emoji here*

* JavaScript - Fundamentals
    * What is it?
    * Why do we use it?
    * Why is it statistically the most popular language around?
        * 63.87% of all stats are made up
    * How do we run it?
        * Why do we have so many options on how to run JavaScript?

* **JavaScript - Object-oriented programming**
    * Good luck.

* HTML
    * Why and how do we use that?
    * Why is it loved by some and hated by a few people?
    * You'll love the simplicity

* CSS
    * What is it?
    * Why does it make Jacob's hair fall out?
    * Is it the main thing used to style sites? Yes. Maybe.

* Git-Bash
    * Again, good luck.

## JavaScript Fundamentals

* Running JavaScript OUTSIDE of the browser, we need node
```
node -v
node --version
```
* When we have node installed, we can run JavaScript just like we ran Python, with a command
```
node *insert file name here*
node index.js
```

* JavaScript, like Python, is classed as a softly-typed language
    * We don't have to declare the data type for a variable
    * It infers the type from the value given

```js
// index.js
console.log("Hello, World")
// JavaScript comments work the exact same as Python comments
// ctrl + / will give you the comments
// cmd + / will give you the comments on a mac

var myName = "Bob" // pre-2016/17
let myAge = 57 // post-2016/17

const myDOB = "01/01/1901"
// myDOB = "01/02/1901" //! TypeError: Assignment to constant variable.

```

### What is JavaScript?

* JavaScript is a programming language - that is used to build websites, stand-alone applications and to add magic to other languages and their applications
* We are using something called vanilla JavaScript
    * Vanilla JavaScript is JavaScript without frameworks or libraries

* JavaScript is both a **front-end language** and a **back-end language**:
    * Facebook is built using React.js (React is a library)
    * Angular.js, Node.js, Express.js, Vue.js, Ember.js, Deno.js, Mithril.js, Svelte.js, Aurelia.js, Backbone.js, Meteor.js AND MANY MORE are frameworks

* Client-side: Front-end
* Server-side: Back-end

```js
let answer = 0.1 + 0.2

if (answer == 0.3) {
    console.log("That's right. That's enough slices.")
}
else {
    console.log("What the devil?")
}

// answer = Math.round(answer * 100) / 100

console.log(answer)
```


## Browsers

* When you're developing a website and you're using two browsers and your website looks different on each browser...
    * Chrome will be correct - V8 Web Engine
    * Firefox - MDN
    * Opera / Safari
    * Edge
    * Brick / House on fire / A lake / A wall
    * IE 7