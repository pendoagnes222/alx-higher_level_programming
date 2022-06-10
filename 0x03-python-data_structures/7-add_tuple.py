#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a or tuple_b:
        results = []
        if len(tuple_a) == 0:
            tuple_a = tuple_a[:2]
            return tuple_b
        if len(tuple_b) == 0:
            tuple_b = tuple_b[:2]
            return tuple_a
        if len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
        if len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
        for x, y in zip(tuple_a, tuple_b):
            zipped = x+y
            results.append(zipped)
        results = tuple(results)
        return results
    return


