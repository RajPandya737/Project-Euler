import math



"""count = 0
for i in range(1,9**40):
    l = len(str(i))
    base = i**(1/l)
    if base.is_integer() or round(base) ** l == i:
        count+=1
        print(i)
print(count)"""

# top has to be 9^4- because that is the point where the number of digits is less then the exponent
count = 0
for base in range(1,10):
    for expo in range(1,40):
        if len(str(base**expo)) == expo:
            count+=1
print(count)