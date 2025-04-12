"""
You are given a target and list of records. Return the record with minimum value for the target. The records can contain negative values as well. If a record doesn't contain the target assume the value to be 0 in that particular record. Assume number of records to be N.

target: 'a' , records: [{'a':1,'b':3},{'a':3},{'a':4,'c':-5}] ans: {'a':1,'b':3}

target: 'a' , records: [{'a':1,'b':3},{'a':3},{'c':-5}] ans: {'c':-5}
"""


def get_min_record(target, record):
    min_record = None
    min_val = float("inf")

    for i in records:
        # if target key not in record : assume value 0
        value = i.get(target, 0)
        if value < min_val:
            min_record = i
            min_val = value
    return min_record


records = [{'a': 1, 'b': 3}, {'a': 3}, {'a': 4, 'c': -5}]
target = 'a'

min_record = get_min_record(target, records)
print(min_record)  # Output: {'a':1,'b':3}

# Similar Question

"""
You are given a target, param and list of records. 
Return the record with minimum value for the target if param is 'asc' or Return the record with maximum value for the target if param is 'dsc'. 
The records can contain negative values as well. 
If a record doesn't contain the target assume the value to be 0 in that particular record. Assume number of records to be N.
"""


def get_extreme_record(target, param, records):
    extreme_record = None
    extreme_val = float('inf') if param == 'asc' else float('-inf')

    for record in records:
        val = record.get(target, 0)
        if param == 'asc':
            if val < extreme_val:
                extreme_record = record
                extreme_val = value
        elif param == 'dsc':
            if val > extreme_val:
                extreme_record = record
                extreme_val = value
    return extreme_record
