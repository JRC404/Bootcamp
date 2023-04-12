// function declarations:

// changes the innerHTML, and fontWeight of HTML element with id="paragraphBox"
function georgeFunction() {
    var paragraph = document.getElementById('paragraphBox') 
    paragraph.innerHTML = 'HAHA no it is not George'
    paragraph.style.fontWeight = 'bold'
}

// changes the innerHTML, and color of HTML element with id="bxyBox"
function benFunction() {
    var paragraph = document.getElementById('boxyBox')
    paragraph.innerHTML = 'HAHA no it is not Ben'
    paragraph.style.color = 'blue'
}

// changes the src of (img) element with id="elephant"
function changePic() {
    document.getElementById('elephant').src = 'https://static.vecteezy.com/system/resources/previews/005/162/400/original/cute-cartoon-elephant-on-white-background-free-vector.jpg'
}