# Movie Trailer Website

This movie trailer website has movies with the poster images, and once you click on a movie image, a trailer video starts. The user needs to know how to run a python file to output a HTML website and automatically open a new tab. It requires Chrome web browser downloaded. If you want to run in a different web browser, go to the very bottom.

### Files included
* fresh_tomatoes.py
* entertainment_center.py
* media.py

### Install Folder
*Clone or Download* on GitHub to download three files.

### How to run the program
* Python 2 
  * Check if you have Python program by typing `python`
  * If the output is `Python 2.7.10 (default, DATE MM DD YYYY, TIME)` then Python is installed in your computer!
  * most mac users already have it installed when you first buy a mac. 
  
* Mac users: 
  * Open Terminal
  * Change to appropriate directory. `cd /Users/username/Downloads/FSND/Programming Fundamentals and the Web/movies/` or find your movies folder.
  * type `python entertainment_center.py` to run the code
* Windows users: 
  * Open cmd
  * Change to appropriate directory `cd /Users/username/Downloads/FSND/Programming Fundamentals and the Web/movies/`
  * `python entertainment_center.py` to run the code
* Linux users:
  * Open up the terminal program.
  * Change to appropriate directory `cd /Users/username/Downloads/FSND/Programming Fundamentals and the Web/movies/`
  * `python entertainment_center.py` to run the code
* If above three did not work, refer to this website for [Running Python Program](https://en.wikibooks.org/wiki/Python_Programming/Creating_Python_Programs)
  
### How the program works
* [`entertainment_center.py`](./movies/entertainment_center.py) is the code that needs to be run on Python. 
  * This script contains movie information and imports `fresh_tomatoes.py` to use `open_movies_page(input)` function.
* [`media.py`](./movies/media.py) is a file that has Movie() class. Movie() class takes in 4 inputs: movie title, movie storyline, poster image url, trailer Youtube url. 
* [`fresh_tomatoes.py`](./movies/fresh_tomatoes.py) file was given by Udacity team, which can do two things, create movie tiles content and open movies page. 
  * Personal touch via HTML:
  * Mouse cursor highlights pink color
  * Tomato logos on the tab title, or a *favicon*, and the website header top.
  * Line 17 contains `<link rel="icon" href="http://www.pngmart.com/files/1/Tomato-Clip-Art-PNG.png">` to allow *favicon* have tomato.

### Finished Product
Image:
![Alt text](./pictureerase.jpeg?raw=true "Optional Title")

### Issue with Chrome 

Don't have Chrome browser downloaded? Please open up `fresh_tomatoes.py` file and edit line 169 and 170.
Here is a snippet of my code for your reference.

![Alt text](./photoerase2.jpeg? "Optional Title")

If **Firefox** is more lit, then delete `    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
`  and 
replace 
`    webbrowser.get(chrome_path).open('file://' + url, new=2) `
with 
`    webbrowser.get('firefox').open('file://' + url, new=2) `

If **Internet Explorer**, then 
`
ie = webbrowser.iexplore
webbrowser.get(ie).open('file://' + url, new=2)`

### Copyright and Licensing Information

MIT License

Copyright (c) 2017 Hye Sun Hong.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  
