#!/usr/bin/python3
add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        zer = 0,
        return tuple_c = tuple( x + y for x, y in zip(tuple_a + zer, tuple_b)
    if len(tuple_b) < 2:
        zer = 0
        return tuple_c = tuple( x + y for x, y in zip(tuple_a, tuple_b + zer)
    else:
        return tuple_c = tuple( x + y for x, y in zip(tuple_a, tuple_b)
