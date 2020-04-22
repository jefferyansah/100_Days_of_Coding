### Summary of Chapter 5: DICTIONARIES AND STRUCTURING DATA

* Indexes for dictionaries are called keys

* A key and its asscoaited value is called a key-value pair

* Unlike list, dictionaries are unordeded. While in list the order of the elements are essential in 
determining if two lists are the same, dictionaries do not work like that. In Dictionaries the order of the 
items does not matter so far as the contents are the same.


* You can only slice items in data structures that are ordered. Becuase dictionaries are unordered, you cannot slice a dictionary.

* Aha Moment : In dictionaries the keys are unique. Thus for every item in the dictionary the keys are unique. If you creat a dictionary with a two duplicate keys, python will overide the first key and keep the second key. This behavior is similar to variable reassigment

* There are three key methods in a dictionary.  These methods are keys(), values() and items(). The methods returns a tuple.

* You can use `in` or `not in` to check if a value exists in a dictionary.

* The `get()` method is an useful way to extract items from a dictionary. The methods allows you to return a user-defined value if the key you are looking for is not found in the dictionary

* What about if a certain key does not exist in a dictionary, then you can offcourse you the `setdefault()` method to set a deafult value if the key is not found. The  `setdefault()` method is  a way of appending items to a dictionary if they dont already exist

* You can modify the charactercount to count the occurences of world in a list



* The `pprint` method is a nice way of printing and formating the outputs of your print statements.



Answers to Questions

1. What does the code for an empty dictionary look like?
Ans: {}

2. What does a dictionary value with a key 'foo' and a value 42 look like?:

Ans: {'foo':42}

3. What is the main difference between a dictionary and a list?

`Ans`: While lists are ordered, dictionaries are unordered.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

`Ans:` KeyError

5.  If a dictionary is stored in spam, what is the difference between the 
expressions 'cat' in spam and 'cat' in spam.keys()?
`Ans:` There is no difference as both statments will check the keys in spam contains 'cat'


6. If a dictionary is stored in spam, what is the difference between the  expressions 'cat' in spam and 'cat' in spam.values() ? 
`Ans:`  'cat' in spam will check the keys to see if 'cat' is in the dictionary and  cat' in spam.values() will check the values.

What is a shortcut for the following code? 
`if 'color' not in spam:
    spam['color'] = 'black'`
`Ans:` spam.setdefault('color', 'black')

