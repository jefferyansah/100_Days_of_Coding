### Summary of Chapter 6: MANIPULATING STRINGS	

* Escape characters offers a way to use special characters in python. By using escape characters, you can use single quotes and apostrophes in the your strings.

* You can place `r` infront of string. This tell python to ignore all escape characters.


* Multi-line string: This can be acheived using tripple quotes. Python Indentation rules do not apply for blocks in a triple string.

* You can also use the multi-line concept to add multiple lines of comment in python. This is preferable to the using the `#` symbol.

import os
import glob


dirname = os.path.dirname(__file__) 
image_location = os.path.join(dirname,  'image_repo')
image_list = os.listdir(image_location)
