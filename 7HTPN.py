import math
primes = []
num = 1
l = 0
while l<10001:
    prime = True
    for i in range(2,int(math.sqrt(num))+1):
        if (num%i==0):
            prime = False
    if prime:
        primes.append(num)
        l+=1
    num+=2
    
print(primes[-1])