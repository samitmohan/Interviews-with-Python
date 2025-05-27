from time import sleep
from threading import Thread, Condition
from queue import Queue
import random


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


# 2 ways to create a thread:
# using the Thread() constructor and passing functions along with the arguments that the function uses.
#   The created thread object is started using start() method.
# Extending the Thread class and overloading the run method and then the thread object is started using the start method
# Create 2 threads
producer = Producer()
consumer = Consumer()
p = Thread(target=producer.produce())
c = Thread(target=consumer.consume())
p.start()
c.start()


"""
Wait and Notify
Assign a Condition object (lock 🔒) to the producer.
In the producer's produce method, call acquire() on lock, do any producing work. Once the work is done, call notify() to
    notify the waiting thread and call release.
In the consumer thread's consume method, call acquire() on the lock of the producer object that is avaialble to the
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
