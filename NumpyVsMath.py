import numpy as np
import math
import timeit
from functools import cache

@cache
def a (L,c):
    m =  0.5* math.sqrt(2 * L * math.sqrt(-1*(L**2) + 2*L*c + c**2)+2*c*c - 2*c*math.sqrt(-1*(L**2) + 2*L*c + c**2))
    pass
def b (L,c):
     n = 0.5*math.sqrt(2 * L * math.sqrt(-1*(L**2) + 2*L*c + c**2)+2*c*c - 2*c*math.sqrt(-1*(L**2) + 2*L*c + c**2))

print(timeit.timeit(lambda: a(120, 50)))