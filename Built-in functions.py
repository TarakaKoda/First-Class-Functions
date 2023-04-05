# Creating a built-in functions such as map, filter
numbers = [x for x in range(1, 11)]
# map function for multiplication expression
example = list(map(lambda a: a * a, [1, 2, 3, 4, 5, 6, 7]))


# print(example)


def square(num):
    return num * num


def map_function(fun, list_of_numbers):
    my_list = []
    for i in list_of_numbers:
        my_list.append(fun(i))
    return my_list


my_map = map_function(square, numbers)


# print(my_map)


# filter function
def even(num):
    if num % 2 == 0:
        return num


def odd(num):
    if num % 2 != 0:
        return num


def filter_function(fun, list_of_numbers):
    result_list = []
    for num in list_of_numbers:
        result_list.append(fun(num))
    return [x for x in result_list if x is not None]


even_number = filter_function(even, numbers)
odd_number = filter_function(odd, numbers)
print(even_number)
print(odd_number)


# reduce
def reduce_fun(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


print(reduce_fun([x for x in range(1,6)]))
