from itertools import count
from math import factorial

def fact_gen():
    for el in count(1):
        yield factorial(el)

fact = fact_gen()
i = 0
for el in fact:
    if i < 15:
        print(el)
        i += 1
    else:
        break