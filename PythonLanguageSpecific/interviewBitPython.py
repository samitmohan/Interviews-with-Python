# https://www.interviewbit.com/python-interview-questions/#what-is-python-what-are-the-benefits-of-using-python


# Generators
# Functions that return iterable collection of items one at a time. yield instead of return
import os


def fib(n):
    p, q = 0, 1
    while p < n:
        yield p
        p, q = q, p + q


x = fib(10)  # creates generator object
x.__next__()  # 0
x.__next__()  # 1
x.__next__()  # 1
x.__next__()  # 3

for i in fib(10):  # works : makes it an iterable
    print(i)

# Iterators
# Object that remembers it's state, __iter__() method initializes an iterator.
# __next__() returns next item in iteration and points to next.


class ArrayList:
    def __init__(self, lst) -> None:
        self.numbers = lst

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos < len(self.numbers):
            self.pos += 1
            return self.numbers[self.pos - 1]
        else:
            raise StopIteration


array_obj = ArrayList([1, 2, 3])
it = iter(array_obj)
print(next(it))  # 2
print(next(it))  # 3

# Delete file
os.remove("File.csv")
print("File removed")


# Args
# * : variable length, *ars : define to pass variable lenth arguments.


def multiply(a, b, *argv):
    mul = a * b
    for num in argv:
        mul *= num
    return mul


print(multiply(1, 2, 3, 4, 5))  # 120

# **kwargs : pass variable length keyworded argument (variable that has a name passed to a function)
# Dictionary of variable name and it's value


def tellArguments(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


tellArguments(arg1="argument 1", arg2="argument 2")
"""
Output
arg1 : argument 1
arg2 : argument 2
"""

# OOPs
# Access member of parent class in child class : super()


class Parent(object):
    # Constructor
    def __init__(self, name):
        self.name = name


class Child(Parent):
    # Constructor
    def __init__(self, name, age):
        """
        In Python 3.x, we can also use super().__init__(name)
        """
        super(Child, self).__init__(name)
        self.age = age

    def display(self):
        # Note that Parent.name cant be used
        # here since super() is used in the constructor
        print(self.name, self.age)


obj = Child("Interviewbit", 6)
obj.display()

# Access Specifiers
# _ = protected
# __ = private
# no prefix = public


class Employee:
    # protected
    _emp_name = None
    _age = None
    # private
    __branch = None

    def __init__(self, emp_name, age, branch):
        self._emp.name = emp_name
        self._age = age
        self.__branch = branch

    def display():
        print(self._emp_name + " " + self._age + " " + self.__branch)


# Empty class


class EmptyClass:
    pass


obj = EmptyClass()
obj.name = "Samit"
print(obj.name)  # creates member name and assigns it to samit

# Finalized is used for freeing up unmanaged resources and clean up before garbage collection is invoked.

# How to check if class is subclass of another class? issubclass(class1, class2)


class Parent(object):
    pass


class Child(Parent):
    pass


# Driver Code
print(issubclass(Child, Parent))  # True
print(issubclass(Parent, Child))  # False
