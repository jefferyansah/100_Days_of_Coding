### Summary of What I learned in Chapter 3

* A parameter is a variable that an argument is stored in when a function is called.

* The value that a function call evaluates to is call the return value of the function.

* Python has a NoneDataType. None is the only value in the NoneDataType. 

* Most arguments are identified by their positions in a function call.

* Keyword arguments are identified by the keyword put before them in the function call.

* The print statement has some parameters, these parameters are: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`


* A variable that exists in a local scope is called a local variable, while a variable that exists in the global scope is called a global variable. A local sope is created whenever  a function is created.

Why do we need Scope:

Code in global scope cannot use any local variables.
A local scope can access a global variable
Code in a function's local scope cannot use variables in any other local scope.
You can use the same name for different variables if they are in different scopes

Questions:

1. Why are functions advantageous to have in your programs?
Ans: `Functions help you to put your programs in compartments. This also you organize your code to able to use global and local variable. They are also very useful for debugging.`

2.  When does the code in a function execute: when the function is defined or when the function is called?
Ans: `When the function is called`

3. What statement creates a function?

Ans: `def function_name()`

4.  What is the difference between a function and a function call?
Ans: `A Function defines a piece of code where a function call executes the peice of code.`

5. How many global scopes are there in a Python program? How many 
local scopes
Ans: `There is only one global scope. There can be many local scopes depending the number of number of functions and how the variables in the functions are defined`

6.  What happens to variables in a local scope when the function call returns?

Ans: `They get disposed`

7.  What is a return value? Can a return value be part of an expression?

Ans: ` A return value is the a value that is returned by a function and is usually the results of an evalution. Yes becuase expresssions evaluates to a value.`

8. If a function does not have a return statement, what is the return value 
of a call to that function?
Ans: `None`

9.  How can you force a variable in a function to refer to the global variable?
Ans: `Define the variable with the keyword 'global'`

10.  What is the data type of None?
Ans: `NoneDataType `

11.   What does the import areallyourpetsnamederic statement do? 
Ans: `Through and error`

12.   If you had a function named bacon() in a module named spam, how 
would you call it after importing spam?

Ans: `spam.bacon`


13. How can you prevent a program from crashing when it gets an error?

Ans: `You can use exception handling, to handle errors`

14. What goes in the try clause? What goes in the except clause?

Ans: `The statement goes into the try clause. What you want to hanppen if the program runs into an error will be put in the except clause `

15. 


#Practice Project











