from unicodedata import name


print("Hello World")
# input() function
#name = input("What is your name? ")
# int() float() bool() function
# age = int(input("What is your age? "))
#height = float(input("What is your height? "))
# is_human = bool(input("Are you human? "))
# print("Hello " + name)
# print("You are " + str(age) + " years old")
# print("You are " + str(height) + " meters tall")
# print("You are human: " + str(is_human))

# len() function
name_length = len("Ammar")
print("Your name is " + str(name_length) + " characters long")
# str() function
age_string = str(25)
print("Your age is " + age_string)
# type() function
# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_human))
# print(type(name_length))
# print(type(age_string))

# Variables
# Variables are used to store data values.
# Variables are containers for storing data values.
# Unlike other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

# You can display the data type of a variable with the type() function:
x = "John"
print(type(x))

# The data type can be changed after the variable has been set:
x = "John"
print(x)
print(type(x))
x = 20
print(x)
print(type(x))

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
# Casting is done using constructor functions:
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x, y, z)

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"
# Assign Value to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x,y,z)

# Output Variables
# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

# You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
# print(x + y)

# To fix the code, you can use the format() method:
x = 5
y = "John"
print(str(x) + y)

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Create a variable outside of a function, and use it inside the function:
x = "test"
fun = lambda x: x + " is " + x
print(fun(x))

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.
# Create a variable inside a function, with the same name as the global variable:
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

# To create a global variable inside a function, you can use the global keyword.
# If you use the global keyword, the variable belongs to the global scope:
x = "globel"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

# constants are variables that cannot be changed.
# Python does not have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed.

class CONST(object):
    __slots__ = ()
    PI = 3.14
    G = 9.8
    R = 8.314
    def __setattr__(self, *_):
        pass
CONST = CONST()
CONST.PI = 3.15
print(CONST.PI)
print(CONST.G)
print(CONST.R)

# A final name can be assigned only once. If it is assigned a value a second time, a TypeError is raised at runtime:
from typing import Final, final
A: Final[int] = 1
# Executes fine, but mypy will report an error if you run mypy on this:
A = 2

# conditional statements
# if statement
# if statement is used to check if a condition is true or not.
# if the condition is true, the code inside the if statement will be executed.
# if the condition is false, the code inside the if statement will be skipped.
# Syntax:
# if condition:
#     code
# Example:
if 5 > 2:
    print("Five is greater than two!")

# if else statement
# if else statement is used to check if a condition is true or not.
# if the condition is true, the code inside the if statement will be executed.
# if the condition is false, the code inside the else statement will be executed.
# Syntax:
# if condition:
#     code
# else:
#     code
# Example:
if 5 > 7:
    print("Five is greater than seven!")
else:
    print("Five is not greater than seven!")

# if elif else statement    
# if elif else statement is used to check if a condition is true or not.
# if the condition is true, the code inside the if statement will be executed.
# if the condition is false, the code inside the elif statement will be executed.
# if the condition is false, the code inside the else statement will be executed.
# Syntax:
# if condition:
#     code
# elif condition:
#     code
# else:
#     code
# Example:
if 5 > 7:
    print("Five is greater than seven!")
elif 5 == 7:
    print("Five is equal to seven!")
else:
    print("Five is not greater than seven!")

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
# Example:
if 5 > 2: print("Five is greater than two!")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# Example:
print("Five is greater than two!") if 5 > 10 else print("Five is not greater than ten!")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
# Example:
x = 5
print(x > 3 and x < 10)

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
# Example:
x = 5
print(x > 3 or x < 4)

# Nested If
# You can have if statements inside if statements, this is called nested if statements.
# Example:
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
# Example:
a = 33
b = 200
if b > a:
    pass

# while loop
# With the while loop we can execute a set of statements as long as a condition is true.
# Example:
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# Example:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
# Example:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
# Example:
print("\n\nx")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
# Example:
for x in "banana":
    print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
# Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Example:
for x in range(6):
    print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
# Example:
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Example:
for x in range(2, 30, 3):
    print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Example:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Example:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
# Example:
for x in [0, 1, 2]:
    pass

# Calling a Function
# To call a function, use the function name followed by parenthesis:
# Example:
def my_function():
    print("Hello from a function")
    pass
my_function()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
# Example:
def my_function(fname):
    print(fname + " Refsnes")
    pass
my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
# Example:
def my_function(fname, lname):
    print(fname + " " + lname)
    pass
my_function("Emil", "Refsnes")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Example:
def my_function(*kids):
    print("The youngest child is " + kids[2])
    pass
my_function("Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# Example:
def my_function(**kid):
    print("His last name is " + kid["lname"])
    pass
my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
# Example:
def my_function(country = "Norway"):
    print("I am from " + country)
    pass
my_function("Sweden")
my_function("India")
my_function()

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
# Example:
def my_function(food):
    for x in food:
        print(x)
        pass
    pass
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
# To let a function return a value, use the return statement:
# Example:
def my_function(x):
    return 5 * x
    pass
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# Example:
def myfunction():
    pass

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
# Example:
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
        pass
    return result
    pass
print("\n\nRecursion Example Results")
tri_recursion(6)

# Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:
# Example:
x = lambda a : a + 10
print(x(5))

# A lambda function that adds 10 to the number passed in as an argument, and print the result:
# Example:
x = lambda a, b : a * b
print(x(5, 6))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# Example:
def myfunc(n):
    return lambda a : a * n
    pass
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# Or, use the same function definition to make both functions, in the same program:
# Example:
def myfunc(n):
    return lambda a : a * n
    pass
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# Python Modules
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

# Use a Module
# Example:
import mymodule
mymodule.greeting('Jonathan')
a = mymodule.person1["age"]
print(a)

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
# Example:
import mymodule as mx
a = mx.person1["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
# Example:
import platform
x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# Example:
import platform
x = dir(platform)
print(x)

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
# Example:
from mymodule import person1
print(person1["age"])

# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# Example:
import datetime
x = datetime.datetime.now()
print(x)

# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.
# Example:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime("%B"))

x = datetime.datetime.strptime("21/11/06 16:30:10", "%d/%m/%y %H:%M:%S")
print(x)

# Python JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a Python dictionary.
# Example:
import json
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# Example:
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# Example:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
        ]
    }
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# Python PIP
# PIP is a package manager for Python packages, or modules if you like.
# Note: If you have Python version 3.4 or later, PIP is included by default.
# Check if PIP is Installed
# Navigate your command line to the location of Python's script directory, and type the following:
# Example:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python37-32\Scripts>pip --version
# pip 19.0.3 from c:\users\your name\appdata\local\programs\python\python37-32\lib\site-packages\pip (python 3.7)

# Download a Package
# Download a package by using the following command:
# Example:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python37-32\Scripts>pip install camelcase
# Collecting camelcase

# Installing collected packages: camelcase
# Successfully installed camelcase-0.2

# Use a Package
# Now you can use the camelcase package to convert strings into camel case:
# Example:
import camelcase
c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))

# Find Packages
# Go to https://pypi.org/, and look for your package.
# Install a Package
# Navigate your command line to the location of Python's script directory, and type the following:
# Example:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python37-32\Scripts>pip install camelcase

# Uninstall a Package
# Navigate your command line to the location of Python's script directory, and type the following:
# Example:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python37-32\Scripts>pip uninstall camelcase

# List Packages
# List all the packages installed on your system by using the list command:
# Example:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python37-32\Scripts>pip list



# Python Try Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# Example:

try:
    x=int(input('Enter the first number: '))
    print(x)
except:
    print("An exception occurred")

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
# Example:
try:
    x=int(input('Enter the first number: '))
    if x<0:
        raise Exception("Sorry, no numbers below zero")
    print(x)
except ValueError:
    print("Value Error")
except Exception as e:
    print(e)

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
# Example:
try:
    x=int(input('Enter the first number: '))
    if x<0:
        raise Exception("Sorry, no numbers below zero")
    print(x)
except ValueError:
    print("Value Error")
except Exception as e:
    print(e)
else:
    print("Nothing went wrong")

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# Example:
try:
    x=int(input('Enter the first number: '))
    if x<0:
        raise Exception("Sorry, no numbers below zero")
    print(x)
except ValueError:
    print("Value Error")
except Exception as e:
    print(e)
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
# Example:
x = 1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
# Example:
x = 5
if not type(x) is int:
    raise TypeError("Only integers are allowed")

# The AssertionError Exception
# The AssertionError exception is raised when an assert statement fails.
# Example:
x = 5.6
assert x > 5, "x should be greater than 5"

# The pass Statement
# class definitions
# function definitions
# loops
# try-except statements
# Example:
try:
    pass
except:
    pass

# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
# Example:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:
# Example:
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
# Example:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
