### Summary of Chapter 6: MANIPULATING STRINGS	

* Escape characters offers a way to use special characters in python. By using escape characters, you can use single quotes and apostrophes in the your strings.

* You can place `r` infront of string. This tell python to ignore all escape characters.


* Multi-line string: This can be acheived using tripple quotes. Python Indentation rules do not apply for blocks in a triple string.

*isuppe()  an islower() methods will return a Boolean value.

*isX: Has some useful isX methods:
1. `isalpha()`: used to check if a string contains only letters and its not blank

2. `isalnum()` used to check whether the string contains only both letter and numbers

3. 'isdecimal()` used to check whether a string contains only numbers and is not blank

4. 'isspace()` is used to check whether the string contains only space, tabls and newline and it not blank

5. `istitle()` is title is used to check for title case. This checks whether the string contains only words that begins with a capital letter and all the rest are small letters.

6. `startswith` and `endswith` are use to evaluate whether a a string ends with some sub-strings.


* `join` and `split` Methods: The join is used to combine a list of strings. The split is used to seperate a list of strings. The join() method is called on a list string and then a list is passed into the method.


* The rjust and ljust is used to justify text. The first arugment to both methods is an interger length for the justified string. The justified string will be moved around depending on the number of characters you specify

* Whitespaces, tabs and newline can be stripped using the strip(), rstrip(), lstrip(). You can also pass a string patttern into the strip method. This remove all matches of the pattern that occurs infront and behind the string arguments.
NB: The strip just works on removing leading and trailing patterns.


Questions:

1. What are escape characters: 
`Ans`: Escape character are special characters that consists of a backlash '\'. In python escape characters helps you to use characters which you is normally impossible to use in strings.

 2. What do the \n and \t escape characters represent? Ans: newline and tab

 3. How can you put a \ backslash character in a string? Ans: by using raw strings `r`

 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t 
escaped?
Ans: Because the double qouate is used to wrap the string, hence the single quote is detected as normal string character

5. If you don’t want to put \n in your string, how can you write a string with newlines in it? 
Ans: You will have to use the tripple quoutes

6. What do the following expressions evaluate to?
•	'Hello world!'[1] : 'H'
•	'Hello world!'[0:5]: 'Hello'
•	'Hello world!'[:5] : 'Hello'
•	'Hello world!'[3:] : 'lo world! 


7. What do the following expressions evaluate to?
•	'Hello'.upper() : 'HELLO'
•	'Hello'.upper().isupper() : True
•	'Hello'.upper().lower() : 'hello'

8. What do the following expressions evaluate to?
•	'Remember, remember, the fifth of November.'.split() : ['Rememeber,', 'remember,  'the', 'fifth', 'of', 'November.' ]
•	'-'.join('There can be only one.'.split()) : 'There-can-be-only-one.'


9. What string methods can you use to right-justify, left-justify, and center 
a string?
Ans: rjust(), ljust(), center()
10. How can you trim whitespace characters from the beginning or end of 
a string?
Ans: strip()