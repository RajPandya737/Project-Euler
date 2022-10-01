import math
an = []
def divisorsum(n) -> int:
    sumlist = []
    sum = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            sumlist.append(i)
            sumlist.append(n//i)
        if math.sqrt(n).is_integer():
            sumlist.append(int(math.sqrt(n)))

    for i in list(set(sumlist)):
        sum+=i
    return sum - n

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return True
 
    # If we reach here, then the element was not present
    return False

def isabundant(n):
    if divisorsum(n)>n:
        return True
    return False



def can_be_written_abundant(n):
    global an
    needednum = []

    for i in an:
        needednum.append(n-i)
    for i in needednum:
        if binary_search(an, i):
            return True
    return False




    ''' 
    #This code is way too slow, it is o(n^3), ill try creating a new list and see how that turns out
    #UPDATE: IT WORKED :) still took about 45 seconds to print so maybe in the future I will try to make some optimizations
    for i in an:
        if i>n:
            break
    
        for j in an:
            if j>n:
                break
            if i + j == n:
                return True
    return False
    '''


for i in range(1, 28124):
    if isabundant(i):
        an.append(i)
t = 0

for i in range(1, 28124):
    if not can_be_written_abundant(i):
        t+=i
print(t)