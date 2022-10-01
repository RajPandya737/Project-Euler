import math
import numpy as np

a = np.array([2,5,7,4,2,5])
def d(n):
  d = [1]
  sum = 0
  for i in range(2, int(math.sqrt(n))):
    if n%i == 0:
      d.append(i)
      d.append(int(n/i))
  if math.sqrt(n).is_integer():
    d.append(int(math.sqrt(n)))
  for i in d:
    sum+=int(i)
  return sum


sum =0
a = d(284)
print(a)
print(d(220))
nums = []
for i in range(3, 10000):
  if int(i) == int(d(d(i))) and int(i) != int(d(i)):
    sum+=i
    nums.append(i)
print(sum)
print(nums)
  