#Solution at bottom

"""import math

#Unfortunetely, the code here is too slow despite only having 2 for loops. Will try using Euclids formula regarding pythagorean triplets, m, and n
def num_tri(L):
  #keeps track of how many pairs there are
  count = 0
  #All values of c will at least be 1/3 and at more be 1/2
  for c in range(L//3+1, L//2-1):
    if count==2: return False
    if calc(L, c) is True: count+=1
  if count == 1: return True
  return False
 # math equation that solves for one of the legs, if it is an integer, then the other leg will also be an integer.
 # If all 3 are integers then the triplet a,b,c work as a right triangle


equation = lambda L,c : 0.5* math.sqrt(2 * L * math.sqrt(-1*(L**2) + 2*L*c + c**2)+2*c*c - 2*c*math.sqrt(-1*(L**2) + 2*L*c + c**2))

def calc(L, c):
  try:

    a = equation(L,c)
    if a.is_integer(): return True
    else: return False
  except ValueError: 
    return False



  #loops through the possible values of L
count = 0
for L in range(2, 100000, 2):
     if num_tri(L) == 1:
      count+=1 
      print(L)
print(count)"""


'''
a_equation = lambda m, n : m**2 - n**2
b_equation = lambda m,n: 2*m*n
c_equation = lambda m,n: m**2 + n**2

def triples(n):
  count = 0
  for m in range(2, n//2):
    for n in range(2, m):
      if count == 2:
        return False
      a = a_equation(m,n)
      b = b_equation(m,n)
      c = c_equation(m,n)

      if a + b + c == n and a**2 + b**2 == c**2:
        count+=1
  return True

count = 0
for L in range(10, 20000, 2):
  if triples(L) == 1: 
    count+=1 
    print(L)

print(count)
'''

from math import gcd
import numpy as np
import time

start = time.perf_counter()
hash = {}
p_nums = []

for i in range(0, 1_500_001):
    hash[i] = 0

for n in range(1, 800):
    for m in range(1, 1000):
        if m > n:
            a = m**2 - n**2
            b = 2*m*n
            c = n**2 + m**2
            if gcd(a, b) == 1 and gcd(a, c) == 1 and gcd(b, c) == 1:
                p_nums.append(np.array([a, b, c]))

for j in p_nums:
    for i in range(1, (1_500_000//sum(j))+1):
        hash[sum(j*i)] += 1

v = 0
for i in hash:
    if hash[i] == 1:
        v += 1
print(v)

print(time.perf_counter()-start)


'''
i = 0
while sum(p_nums[i])<1_500_000:
  t =sum(p_nums[i])
  if hash[t][0] is True:
    hash[t][1]+=1
    if hash[t][1] >=2:
      hash[t][0] = False
  i+=1

print(p_nums[-1], count)

'''
