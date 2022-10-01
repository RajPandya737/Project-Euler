import math
from re import L

def gen_circle(n):
    pass

def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n<2 or n%2 == 0 or n%3 == 0:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

nums = []

for i in range(2, 1000000):
    if is_prime(i):
        p = True
        for j in gen_circle(i):
            if not is_prime(j):
                p = False
                break
        if p == True:
            nums.append(i)
        