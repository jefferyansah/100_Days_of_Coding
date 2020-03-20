### Summary of Chapter 4: LISTS

* 
In Chapter 4 my key takes were :

* Values inside a list are called are called items.

* An index value fo a list  is the position of an item inside a list

* The values in a list of list can be accessed using multiple indexes.

* the `del` statement can be used to remove an item from a list. It can be also be used to delete variables (quite rare tho).


* The multiple assigment Trick is a great way to assign multiple variables with the values in a list using one line of code

* You can use the augmented assigment operator (for eg.  spam += 1 is thesame as `spam= spam+1`) 

* As a side read. I explored some other methods in the list data type. These methods include: `insert`, `pop`, `append`

* You can find the index of a list using the `index` method. The index method can be used to print the location of a particlur element in a list.

* To access an item in a list of list using the index method, you will have to used the nested location of the at item.

* You can add variables to a list using `append`, `extend` and `insert` 

* Breaking down the append method: `list1.append(a)` == `list[len(list1):] = [a]`

* Note on using `append`. If you append a list to another list, you will get a `list of list`. If you want to get a flat list, you will have to use `+` operator

* You can use `remove` and `del` to remove item from a list . Eg:  `list1.remove[item]` and `del list[(indexofitem)]`

* By default Sort() in python uses the ASCIIbetical order.Thus if you need to sort it out in regular alphabetical order then you to pass the argument `key = str.lower` into the sort method.


* Differences between tuples and lists:  Tuples are quite identical to lists except that tuples are created with parenthesis and lists are created with square brackets. While you can create an empty list, you cannot create an empty tuple.

* while Lists are mutable, Strings and Tuples are immutable. Tuples cannot have their values removed, modified or appended.


* Why should you used tuples: Tuples are a great way to convey to anyone reading your code that you dont want the sequence of values to change. Another benefits is that becuase they are immutable python can optimise to make code using tuples faster.


* You create a tuple with single item buy placing a comma inside the parenthesis, otherwise python will think you create a string.

* You can easily convert a tuple to a list by using `list(tuple_name)`. This is very handy if you need a mutable version of an existing tuple.

* Variables do not store lists directly; they store references to the list. A List will transfer values to its referenced variable. The reference value will carry along what ever changes and modifications you make to the list.

* To prevent the situation of mutation a list or dictionary, you can use the `copy()` or `deepcopy()` fuction to create a mutable copy of the list you want to change. This way when the reference list is changes the original list not changed as well

Questions:

1. What is []?
`Ans: 'An empty list'`

2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
`Ans: spam[2] = 'hello' (inplace method) or spam.insert(2, 'hello')`

Preamlbe: For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd']

3. What does spam[int('3' * 2) / 11] evaluate to?
`Ans: 'd'`  * There is an error in the book, the correct operation should be int(int('3' * 2) / 11).

4. What does spam[-1] evaluate to?
`Ans: 'd' `

5. What does spam[:2] evaluate to?
`Ans: ['a', 'b']`

Preamble:

For the following three questions, let’s say bacon contains the list  
[3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?
`Ans: '1`

7. What does bacon.append(99) make the list value in bacon look like?
`Ans : [3.14, 'cat', 11, 'cat', True, 99] `

8. What does bacon.remove('cat') make the list value in bacon look like?
`Ans: [3.14,  11, 'cat', True, 99] `

9. What are the operators for list concatenation and list replication?
`Ans  : Addition (+), multiplication (*)`

10. What is the difference between the append() and insert() list methods?

`Ans: Append will always add an element at the end of the list while insert specifies the postion at which the new element is to inserted`

11. What are two ways to remove values from a list?
`Ans: 'list.remove(item)' and del list[item_index] `


12. Name a few ways that list values are similar to string values.
`Ans: You can iterate through the length of both list and strings, You can use the multiplication operation on both`

13. What is the difference between lists and tuples?

`Ans : List are mutable while tuples are immutable. List are created with square brackerts `[]`  while tuples are created with parenthesis`.

14. How do you type the tuple value that has just the integer value 42 in it?
`Ans: (42,)`


15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
`Ans: list(tuple_name),  tuple(list_name)`

16.  Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
`Ans: They contain the references to the list`

17. What is the difference between copy.copy() and copy.deepcopy()?
`Ans: They basically perform thesame tasks except deepcopy() is used when you have a list of list`

