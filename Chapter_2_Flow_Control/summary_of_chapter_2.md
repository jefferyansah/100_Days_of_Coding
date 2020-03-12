### Summary of What I learned in Chapter 2


What are modules in python.

Modules are built-in functions from the python's standard library that you import into your programs.


In Chapter 2 my key takes were :
* Modules are built-in functions from the python's standard library that you import into your programs.
### Summary of What I learned in Chapter 2



Answers to the Practice Questions
1. What are the two values of the Boolean data type? How do you 
write them?

* `True` and `False`
* They start with a capital letter

2. What are the three Boolean operators?

* `AND`, `OR` `NOT` 

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
`AND TABLE`
* `TRUE AND TRUE`: `TRUE`
* `TRUE AND FALSE`: `FALSE` (vice versa)
* `FLASE AND FALSE`: `FALSE`

`OR TABLE`
* `TRUE OR TRUE`: `TRUE`
* `TRUE OR FALSE`: `TRUE` (vice versa)
* `FLASE AND FALSE`: `FALSE`

`NOT TABLE`
* `NOT FALSE`: `TRUE`
* `NOT TRUE`: `FALSE`

4.  What do the following expressions evaluate to?

Ans:
(5 > 4) and (3 == 5) : `True and False: False`
not (5 > 4) : `False`
(5 > 4) or (3 == 5): `True or False: True`
not ((5 > 4) or (3 == 5)): `not(True):False`
(True and True) and (True == False) : `True and False: False`
(not False) or (not True) : `True or False: True`



4.  What is an expression made up of? What do all expressions do?
* `An expression is made up of a value and an operator`
* `All expressions evaluate to a single value`

5. What are the six comparison operators?

Ans
` '==', '>', '<', '>=', '<=', '!='`

6. What is the difference between the equal to operator and the assign-
ment operator? 

Ans: The equal operator `(==)` is used to compare the two values while the assigment operator `(=)` is used to store a value in a variable.

7. Explain what a condition is and where you would use one.
A condition is a state of a program execution where a some paremeters are checked before the program execution continues. (answers both questions)

8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

* `Statement block: spam = 0`
* `Condition block: if spam == 10:`
* `If Clause block: print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam'):`

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is 
stored in spam, and prints Greetings! if anything else is stored in spam.

Ans: Code Attached.

10. What can you press if your program is stuck in an infinite loop?

Ans: `CTRL C`

11. What is the difference between break and continue?

Ans: `break` will jump out of the loop while `continue` stop execution at the current and go back to the beginning of the loop

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) 
in a for loop?

13. Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalent program that prints the numbers 1 to 10 using 
a while loop.

14.  If you had a function named bacon() inside a module named spam, how 
would you call it after importing spam?

Ans: spam.bacon()


