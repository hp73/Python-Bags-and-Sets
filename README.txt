Project 4 - Python Bags
CSCI 112 Winter 2019
By Harry Pinkerton, Laurie Jones, James Lawson
Required to run: python 3.7

==============
abstractBag.py
==============
Creates an abstractBag class that all other bags inheret from. Does nothing when run.

==============
arrayBag.py
==============
An array-based bag implementation. Objects that are added to the bag are added sequentially and returned in the same order that they were placed into the bag.
This means index 0 of the arrayBag is the first object placed into the bag. When run, it tests the functionalities of the arrayBag.

==============
arrays.py
==============
An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.

==============
arraySortedBag.py
==============
An array-based bag implementation that when a new object is added, automatically sorts it into alphabetical order by placing the new object in the
correct place in the list. Numbers are given higher priority than letters, so all numbers added to the bag are put in chronological order at the start
of the bag. When run, it tests the functionalities of the arraySortedBag.


==============
bagInterface.py
==============
Speficitactions of the methods for all bag classes.  Running this code will
not produce any results, but it shows the headers and docstrings of the methods
that MUST be included or supported in any bag class.


==============
linkedBag.py
==============
A link-based implemention of a bag that uses nodes to place each object within the bag. This means that the first object that is placed within the bag gets pushed to the end of the list as opposed to being the first in the list. When run, it tests the functionalities of the linkedbag.

==============
miniScrabble.py
==============
A mini scrabble game using and array bag to store letters. 25 letters are generated and every letter is one point. Run the program and write a word. If there are enough available letters in the bag to create that word, the game will return how many points you got for that round. Otherwise, the game will return an error.

==============
Node.py
==============
represents a singly linked node to be used in a linkedbag. When run, it does nothing.

==============
Node.py
==============
represents a singly linked node to be used in a linkedbag. Does nothing when run.

==============
testBag.py
==============
A more in depth test for all of the bags. By default, it tests the ArraySortedBag, but if you wish to test a linkedBag or an arrayBag, simply uncomment those sections in
the main section of this file and comment out the sections you do not wish to see.


