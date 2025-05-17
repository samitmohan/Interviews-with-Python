# Avoid nested python loops : product()
"""
list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a in list_a:
    for b in list_b:
        for c in list_c:
            if a + b + c == 2077:
                print(a, b, c) # 70 2000 7
"""

from itertools import product

list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)

# Walrus Operator : assign values to variables as a part of a larger expression
"""
author = "Yang"
print(author)
# Yang
"""

print(author := "Yang")
# Yang
# Another example
while (line := input()) != "stop":
    print(line)
# Assigns value to variables WITHIN an expression, rather than assigning them seperately

# Ternary
min = a if a < b else b

# Lambda : anonymous functions
"""
def fib(x):
    if x <= 1: return x
    else:
        return fib(x - 1) + fib(x - 2)
"""


def fib(x):
    return x if x <= 1 else fib(x - 1) + fib(x - 2)


# List comprehensions
Genius = ["samit", "rishabh", "amisha"]
l1 = [name if name.startswith("y") else "Not genius" for name in Genius]
print(l1)  # Not genius

# Higher order functions
"""
For example, the map() function is a famous and frequently-used higher-order function. It receives two parameters, one is a function and the other is an iterable. Executing the map function will apply the function to each element of the iterable.

As the above example shows, with the help of the map() function, we can avoid writing a for loop to capitalize every word in the names list.
"""
names = ["yAnG", "MASk", "thoMas", "LISA"]
names = map(str.capitalize, names)
print(list(names))
# ['Yang', 'Mask', 'Thomas', 'Lisa']

# Merge dictionaries

cities_us = {"New York City": "US", "Los Angeles": "US"}
cities_uk = {"London": "UK", "Birmingham": "UK"}

cities_us |= cities_uk  # | is used to merge dictionaries (Union Operator)
print(cities_us)
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK'}

# F-Strings
pi = 3.1415
print(f"Pi is approximately = {pi:.2f}")

# Using Asterisks for Unpacking Iterables and Destructuring Assignments
# How to merge a list, a tuple and a set into one list?

A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = [*A, *B, *C]
print(L)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]


# More of map functions : in CP

input_list = list(map(int, input("enter numbers: ").split()))
# enter numbers: 1 2 3 4 5 6 7 8
# [Output] : [1, 2, 3, 4, 5, 6, 7, 8]
