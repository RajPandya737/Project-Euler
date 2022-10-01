import math

def gen_primes(n):
    primes = [True]*(n+1)
    pr = []
    primes[0] = False
    primes[1] = False
    for p in range(2, int(math.sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False
 
 
    for i in range(0, len(primes) ):
        if primes[i] == True:
            pr.append(i)
    return pr

# Binary Search in python


def binarySearch(array, x, low, high):
  while low <= high:
      mid = low + (high - low)//2
      if array[mid] == x:
          return mid
      elif array[mid] < x:
          low = mid + 1
      else:
          high = mid - 1
  return -1

  
primes = gen_primes(1000000)
num = 0
p_n = 0
for i in range(len(primes)-1):
  sum = 0
  p = 0
  for j in range(i, len(primes)-1):
    sum+=primes[j]
    p+=1
    if p>p_n and binarySearch(primes, sum, 0, len(primes)-1) !=-1:
      p_n = p
      num = sum
    if sum>1000000:
      break
print(num, p_n)
      