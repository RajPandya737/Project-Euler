import math
#equation: y = n^2 + an + b
def prime(n):
    if n<2:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True


amax = 0
max = 0
bmax = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            ans = (n*n)+(a*n)+b
            if not prime(ans):
                break
            else:
                n+=1
        if n>max:
            amax = a
            bmax= b
            max = n
print(amax,bmax, max, amax*bmax)