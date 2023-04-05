# assign function to a variable
def square(a):
    return a*a


f = square
print(f(5))


# passing as an argument to another function
def call_fun(fun):
    return fun(5)


print(call_fun(f))


# returning as a value from a function
def return_fun():
    return f


result = return_fun()
print(result(5))