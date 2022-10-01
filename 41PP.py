from itertools import permutations
import math
def is_prime(n):
    if n<2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n%2 == 0 or n%3 == 0:
      return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True


#the digits 8 and 9 in the pandigital list made no primes, so shrink it down to 7
digits = [1,2,3,4,5,6,7]


nums = sorted(list(permutations(digits)))

for i in range(len(nums)-1, -1, -1):
  print(int("".join(list(map(str, list(nums[i]))))))
  if is_prime(int("".join(list(map(str, list(nums[i])))))) is True:
    print(i)
    print("done")
    break
  