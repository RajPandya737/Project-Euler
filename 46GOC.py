import math


def gen_composite():
  n = 10000
  primes = [True]*(n+1)
  pr = []
  primes[0] = False
  primes[1] = False
  for p in range(2, int(math.sqrt(n))+1):
      if primes[p] == True:
          for i in range(p*p,n+1,p):
              primes[i] = False
  for i in range(2, len(primes) ):
      if primes[i] == False:
          pr.append(i)
  return pr

def gen_primes(n):
  primes = [True]*(n+1)
  pr = []
  primes[0] = False
  primes[1] = False
  for p in range(1, int(math.sqrt(n))+1):
      if primes[p] == True:
          for i in range(p*p,n+1,p):
              primes[i] = False
 
  for i in range(0, len(primes) ):
      if primes[i] == True:
          pr.append(i)
  return pr

def gen_squares(n):
  lst = []
  for i in range(n):
    lst.append(2*(i**2))
  return lst

"""
#n was first 3135, then 4005, 4487
for n in gen_composite():
  if n%2==1:
    print(n)
    found = True
    for p in primes:
      if p>n:
        break
      sl = True
      for s in range(n):
        if n == p+(2*(s**2)):
          sl = False
          found = False
          break
      if sl is False:
        break
    if found is True:
      print(n)
      break"""

squares = gen_squares(100)
primes = gen_primes(10000)
for n in gen_composite():
  if n%2 == 1:
    found = False
    for p in primes:
      if p>n:
        break
      elif n-p in squares:
        found = True
        break
    if found is False:
      print(n)
      break