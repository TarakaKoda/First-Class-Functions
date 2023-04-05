# First-Class Functions:
# "A programming language is said to have first-class function if it treats function as fist-class citizens."

# First-Class Citizen (Programming): "A first-class citizen  (sometimes called first-class objects) in a programming
# language is an entity which supports all the operations generally available to other entities. These operations
# typically include being passed as an argument, returned from a function, and assigned to a variable."

# In Python, a first-class function is a function that can be treated as a value, just like any other data type such
# as an integer or a string. Specifically, a first-class function can be:

# 1. Assigned to a variable
# 2. Passed as an argument to another function
# 3. Returned as a value from a function

# "This means that functions in Python are not just pieces of code that execute when called, but they are also objects
# that can be manipulated and passed around like any other data type. This feature is particularly useful when
# working with higher-order functions, which are functions that take one or more functions as arguments or return a
# function as their result."

# Here's an example of a first-class function in Python:
def greet(name):
    return "Hello, " + name


# Assigned the function to a variable
greeting_function = greet
print(greeting_function("srinu"))


# Passing as an argument to another function
def call_function(fun):
    return fun("pavan")


result = call_function(greet)
print(result)


# returning as a value from a function
def return_as_value():
    return greet


return_function = return_as_value()
print(return_function("naruto"))