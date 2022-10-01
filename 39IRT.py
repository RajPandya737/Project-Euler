import math
import numpy as np



#Unfortunetely, the code here is too slow despite only having 2 for loops. Will try using Euclids formula regarding pythagorean triplets, m, and n
def num_tri(L):
  #keeps track of how many pairs there are
  count = 0
  #All values of c will at least be 1/3 and at more be 1/2
  for c in range(L//3, L//2):
    if calc(L, c) is True: count+=1
  return count
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
max = 0
v = 0
for L in range(13, 1001, 1):
     if num_tri(L) > max:
        v = L
        max = num_tri(L)
print(max)
print(v)

print(num_tri(840))

