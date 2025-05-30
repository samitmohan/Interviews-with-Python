from recviz import recviz


@recviz
def fib(n):
    # base condition mimicking the first two numbers
    # in the sequence
    if n == 0:
        return 0
    if n == 1:
        return 1

    # every number is summation of the previous two
    return fib(n - 1) + fib(n - 2)


#  -> fib(3)
#     -> fib(2)
#        -> fib(1)
#        <- 1
#        -> fib(0)
#        <- 1
#     <- 2
#     -> fib(1)
#     <- 1
#  <- 3
