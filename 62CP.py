from itertools import permutations
import math

"""
#This is the naive approach
def insertPF(primeFact, fact) :
 
    if (fact in primeFact) :
     
        primeFact[fact] += 1
      
    else :
      
        primeFact[fact] = 1
 
    return primeFact
def primeFactors (n) :
 
    primeFact = {}

    while (n % 2 == 0) :
     
        primeFact = insertPF(primeFact, 2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2) :
        while (n % i == 0) :
     
            primeFact = insertPF(primeFact, i)
            n = n // i

    if (n > 2) :
        primeFact = insertPF(primeFact, n)
   
    return primeFact

def perfectCube (n) :
 
    primeFact = {}
    primeFact = primeFactors(n)
    for x in primeFact :
     
        if (primeFact[x] % 3 != 0) :
            return False
      
    return True


def check(n):
    for i in range(345, n):
        cube = i**3
        nums = permutations(list(str(cube)))
        count = 0
        for j in nums:
            v = int("".join(list(map(str, list(j)))))
            if perfectCube(v) is True:
                count+=1
        if count == 1:
            print(i)
            
"""

nums = {}
min = 100000000
for i in range(1, 100000):
    cube = i**3
    t = ("".join(sorted(list(str(cube)))))
    if t not in nums:
        nums[t] = [1, i]
    else:
        nums[t][0]+=1
        if nums[t][0] == 5 and nums[t][1]<min:
            min = nums[t][1]
print(min**3)