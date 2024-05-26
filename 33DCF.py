#33
from fractions import Fraction
mult = 1

nums = []
for n in range (10, 100):
    for d in range(n, 100):
        if n == d:
              continue
        nd1, nd2 = int(n/10), n%10
        dd1, dd2 = int(d/10), d%10
        num = None
        if nd1 == dd1 and dd2 != 0:
              num = nd2/dd2
        elif nd1 == dd2 and dd1 != 0:
              num = nd2/dd1
        elif nd2 == dd1 and dd2 != 0:
            num = nd1/dd2
        elif nd2 == dd2 and dd1 != 0 and nd2 != 0:
            num = nd1/dd1
        if num is not None and num == n/d:
            nums.append((n, d))

num = 1
den = 1
for pair in nums:
     num *= pair[0]
     den *= pair[1]

print(Fraction(num, den))

#answer is den