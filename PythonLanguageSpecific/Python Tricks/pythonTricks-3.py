# Context Manager : close resources automatically
import itertools
import pickle
import random
from asyncio import sleep, Queue
from collections import Counter
from threading import Thread, Condition

import mysql.connector

f = open("test.txt", "w")
f.write("Hi samit")
f.close()

# Better way
with open("test.txt", "w") as f:
    f.write("Hi samit")

# Any and All
l1 = [3, 5, 6, 7, 10]
all_odd = all(i % 2 == 1 for i in l1)
one_add = any(i % 2 == 1 for i in l1)

# Manual String formatting : never use + when you can use f-String
name = "samit"
age = "18"  # 18
print("My Name is " + name + " and I am " + age + " years old")
print(f"My name is {name} and I am {age} years old")

# Difference between identity and equality (pass by value and pass by reference)
# to check pass by value
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # true

# pass by reference
print(a is b)  # false

# Map
numbers = [1, 2, 3, 4, 5]
# create square
sq_nums = []
square = lambda n: n**2

for num in numbers:
    sq_nums.append(square(num))

# instead of this : use map() : applies function to iterable that is passed
# 2 arguments : function that will modify and iterable
# need to convert to list
sq_nums2 = list(map(lambda n: n**2, numbers))

# Similarly the filter()
numbers = [234, 1, 23, 3213, 55, 23, 24]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(list(filter(lambda x: x % 2, range(15))))


# *args and **kwargs
# *args : accept variable number of arguments


def add(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add())
print(add(1, 2))
print(add(1, 2, 23, 5))  # works no matter how many arguments passed


# kwargs : for dictionaries


def printer(**kwargs):
    for x, y in kwargs.items():
        print(f"{x} - {y}")


printer(language="python")
printer(name="samit", company="MMT")

# CP Tricks
# Input : single line
input_list = list(map(int, input("enter numbers: ").split()))

# Get permutated strings
list(itertools.permutations("Happy", 2))  # ('H', 'A'), ('H', 'P'), ...

# Most common
arr = [1, 3, 4, 2, 1, 4, 1, 4, 2, 5, 2, 1, 4, 2, 1]
counter = Counter(arr)
top_three = counter.most_common(3)
print(top_three)

# A test object
test_dict = {"Hello": "World!"}

# Serialization
with open("test.pickle", "wb") as outfile:
    pickle.dump(test_dict, outfile)
print("Written object", test_dict)
# The byte stream representing test_dict is now stored in the file “test.pickle”

# Deserialization
with open("test.pickle", "rb") as infile:
    test_dict_reconstructed = pickle.load(infile)
print("Reconstructed object", test_dict_reconstructed)

if test_dict == test_dict_reconstructed:
    print("Reconstruction success")

# Abstract and Interface
# To create abstract classes : import from abc {abstract base class} module
# To make class abstract, extend abc and decorate the abstract method with @abstractmethod

from abc import abstractmethod, ABC


class Car(ABC):
    def __init__(self):
        pass

    # abstract method
    @abstractmethod
    def drive(self):
        pass

    def horn(self):
        print("Making sound")


# make all the methods of the class abstract to make a class an interface (add @abstractmethod to all)

"""
Regular expressions
import re [stands for regular expressions]

match, returns a matching string object. result.group() needs to be called for the result

search returns matching string result when result.group() is called,

findall returns a list of all matched strings,

split takes a regex which is used as a delimiter to split the string,

sub stands for substitute: ,

\d for any digit [single character]

\D for any non digit

\s for any white space

\S for any non white space

\w for any alpha numeric character

\W for any non alpha numeric character

\b space around words

\A start of the string

\Z end of the string

{} occurrence of the character

Special character

\ escape character used to escape

. any one character

^ beginning of a string

$ end of the string

[…] range of values

[^…] matches every character other than the range provided

() to pass regex

(R|S) to give two regex, match either of the two.
"""

# Date and Time : epoch :seconds since a certain timestamp
# time.time() : returns epoch seconds
# time.ctime(seconds) : returns time and date as a string
# FOR Performance benchmarking : perf_counter() from time module : returns time in seconds
# call it i beginning and then at end. Subtract to get time.

# Database
# install mysql-connector-python
# import module (mysql.connector)
# establish connection : call connect() (takes 4 parameters : host_name, db name, user, password)
# get cursor / pointer to insert and other operations
# cursor's execute is used to make query, cursor object stores data
# fetch, fetchall etc. can be used to get data from cursor
# close()

# get connection
conn = mysql.connector.connect(
    host="localhost", database="mydb", user="root", password="tiger"
)
# get cursor object
cursor = conn.cursor()

if conn.is_connected():
    print("connection made")

"""
emp has 3 columns : id, name, salary
"""

cursor.execute("select * from emp")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
cursor.close()
conn.close()


# Creating rows and deleting:
# execute(” insert into or delete from query”)


# Threading
class Producer:
    def __init__(self):
        self.products = []
        self.productsAvail = False

    # function to produce
    def produce(self):
        for i in range(1, 5):
            self.products.append("Products" + str(i))
            print("Product added!")
            sleep(1)
        self.productsAvail = True


class Consumer:
    def __init__(self):
        self.producer = producer

    def consume(self):
        while not self.producer.productsAvail:
            print("waiting...")
            sleep(0.2)
        print("Products added ", self.producer.products)


# Create 2 threads
producer = Producer()
consumer = Consumer()
p = Thread(target=producer.produce())
c = Thread(target=consumer.consume())
p.start()
c.start()

# 2 ways to create a thread:
# using the Thread() constructor and passing functions along with the arguments that the function uses.
#   The created thread object is started using start() method.
# Extending the Thread class and overloading the run method and then the thread object is started using the start method


# Wait and Notify
"""
Assign a Condition object (lock 🔒) to the producer.
In the producer’s produce method, call acquire() on lock, do any producing work. Once the work is done, call notify() to
    notify the waiting thread and call release.
In the consumer thread’s consume method, call acquire() on the lock of the producer object that is avaialble to the
    consumer object. And then call wait() with a timeout value passed.
Finally call release method() on the lock object in the consume.
"""


class Producer:
    # constructor
    def __init__(self) -> None:
        self.products = []
        self.c = Condition()
        # function to produce

    def produce(self):
        # acquire the lock
        self.c.acquire()
        for i in range(1, 5):
            self.products.append("Products" + str(i))
            print("product added!")
            sleep(1)
        # notify all the waiting threads
        self.c.notify()
        # release the lock
        self.c.release()


# defining Consumer
class Consumer:
    # constructor
    def __init__(self, producer):
        self.producer = producer

    # consume
    def consume(self):
        # acquire the lock of the producer
        self.producer.c.acquire()
        # now wait for the producer to call notify
        self.producer.c.wait(timeout=0)
        self.producer.c.release()
        print("products added: ", self.producer.products)


# create the two threads
producer = Producer()
consumer = Consumer(producer)
p = Thread(target=producer.produce)
c = Thread(target=consumer.consume)
p.start()
c.start()

"""
Queue and Thread communication

Queue class has two methods get and put. Both lock the queue while one is executing.

Hence, synchronization is taken care of.

Producer puts work done on a queue. Same queue is shared with consumer. Which then calls get() to get the data.

"""


# create a producer method
# that accepts a queue as parameter
def producer(q):
    # run an infinite loop that produces data
    while True:
        print("producing...")
        q.put(random.randint(1, 30))
        sleep(3)


# create a consumer method
def consumer(q):
    # keep asking for data
    while True:
        print("ready and waiting...")
        print("consume data: ", q.get())
        sleep(3)


# create a queue
q = Queue()
# create two threads
p = Thread(target=producer, args=(q,))
c = Thread(target=consumer, args=(q,))
p.start()
c.start()
