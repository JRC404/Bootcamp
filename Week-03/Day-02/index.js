// to format your page: shift + alt + f
const myClass = document.getElementsByClassName("myClass");
const myLovelyID = document.getElementById("myLovelyID");
// the first instance of the ID: myLovelyID is the one that it selects
// using getElementById... you can only choose one element...

const h1 = document.getElementsByTagName("h1")

h1[0].style.color = "green";



myLovelyID.style.color = "cyan";

//! myClass.style.color = "cyan"; // Uncaught TypeError: Cannot set properties of undefined (setting 'color')

myClass[0].style.color = "cyan";
myClass[1].style.color = "cyan";
myClass[2].style.color = "cyan";

for (let i = 0; i < myClass.length; i++) {
    myClass[i].style.color = "purple";
}
