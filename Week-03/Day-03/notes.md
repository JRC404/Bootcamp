# Bash

* Command-Line Tool
* CLI (Command-Line Interface)
* This is **not** a GUI (Graphical User Interface)
* A directory is a folder

# Simple Commands

* cd ..
    * This will take us back a directory / folder
* pwd
    * print working directory - this will tell us which folder we are in
* ls
    * list the files inside this directory
* cd Day-03
    * This will take me into the Day-03 folder
    * A tip: if you have a long folder name, type cd and then a few letters of the folder name and then **press the tab key to auto-complete**

* mkdir MyNewFolder
    * This will create a folder called MyNewFolder
    * It does not take you inside of that folder

* cd MyNewFolder
    * This will take us into the newly created file :)

* touch index.js
    * this will create a new file called index.js

* touch index.html style.css
    * this will create 

* clear
    * Tidy up your bash terminal

## DANGER ZONE - PLEASE ONLY DO THIS IF YOU ARE 100% SURE YOU SHOULD BE DOING IT

* rm index.html
    * remove the file with no warning
* mkdir AnotherFolder
* cd AnotherFolder
* cd ..
* ls
* rm AnotherFolder
    * This will show the error: 'rm: cannot remove 'AnotherFolder/': Is a directory'
* rmdir AnotherFolder
    * This removes your folder
* ls
* mkdir AnotherFolder
* rm -r AnotherFolder
    * This will also remove your folder and all of it's files / sub-directories

## Extras

* cd ../..
* cd ../../..
* cd ../../../..

* touch css/style.css
    * Error: touch: cannot touch 'css/style.css': No such file or directory
* mkdir css
* touch css/style.css
    * This won't error anymore, it knows the css folder exists, and simply puts a file inside of it

### Moving and Renaming Files

* mkdir JS
* ls
* If you do not have an index.js in this folder, create one using 'touch index.js'
* mv index.js JS/
    * this will move my index.js into the folder JS
* cd JS
* ls
    * You SHOULD see index.js
* mv index.js main.js
    * this will rename our file from index.js to main.js
* touch error.js
* mv error.js ../
    * This will move error.js back a directory

## Lil' ol' Challenge

* Create a folder of your choice inside of our Day-03 (or whatever you've called today's folder)
* Inside of that folder, please create 2 new folders with 4 files inside of each, remove 2 files from each of those
* Move one file from one to the other
* Rename a file
* Remove a folder
* Have a bash... get it?