# Turns out I don't know a lot about generators.

"""
Generators return lazy iterators (delays evaluation of expression until value is needed)
After a function's value is computed for that parameter or set of parameters, the result is stored in a lookup table that is indexed by the values of those parameters;
the next time the function is called, the table is consulted to determine whether the result for that combination of parameter values is already available.

Memory-efficient: No need to store the entire sequence in memory.
Readable and concise
Composability: You can chain generators together for elegant pipelines.
"""


# This version opens a file, loops through each line, and yields each row, instead of returning it.
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


# This works instead of
def csv_reader2(file_name):
    with open(file_name, "r") as file:
        result = file.read().split("\n")
        return result


# Gives memory error as it tries to load file, read, split into one memory


# Similarily to generate numbers -> since computer has finite memory we use yield
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


#  Instead of loading everything into memory, you yield items one by one.
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (
    num**2 for num in range(5)
)  # <generator object <genexpr> at 0x102db6a80>
print(nums_squared_gc)
print(nums_squared_lc)
for num in nums_squared_gc:
    print(num)
