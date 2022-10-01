import time
import math
start = time.perf_counter()
def prime_factors(n):
  nums = []
  while n % 2 == 0:
      nums.append(2)
      n = n / 2

  for i in range(3,int(n)+1, 2):
      while n % i== 0:
          nums.append(i)
          n = n / i
          if len(list(set(nums)))>4:
            return 5
           
  return len(list(set(nums)))

"""def check(n):
  arr = [0,0,0,1,0,0,0]
  t = prime_factors(n-3)
  if t == 4:
    arr[0] == 1
  t = prime_factors(n-2)
  if t == 4:
    arr[1] == 1
  t = prime_factors(n-1)
  if t == 4:
    arr[2] == 1
  t = prime_factors(n+3)
  if t == 4:
    arr[6] == 1
  t = prime_factors(n+2)
  if t == 4:
    arr[5] == 1
  t = prime_factors(n+1)
  if t == 4:
    arr[4] == 1
    #95000
  return arr"""
    
l = 0
for i in range(5, 10000000):
  t = prime_factors(i)
  if t == 4:
    l+=1
    print(i)
  else:
    l = 0
  if l == 4:
    print(i)
    break
print(time.perf_counter()-start)