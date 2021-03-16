from itertools import count
from math import factorial


def my_fac(x):
    for num in count(1):
        if num == x:
            break
        yield num


gen = my_fac(4)
for i in gen:
    i = factorial(i)
    print(i)
