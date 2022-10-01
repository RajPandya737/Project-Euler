import math
def gen_primes(n):
    primes = [True]*(n+1)
    pr = []
    primes[0] = False
    primes[1] = False
    for p in range(2, int(math.sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False


    for i in range(0, len(primes) ):
        if primes[i] == True:
            pr.append(i)
    return pr


def is_prime(n):
    if n<2 or n%2 == 0:
        return False
    elif n == 2 or n == 3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True


def concat_prime(i,j,k,l):
    if is_prime(int(str(i)+str(j))) and is_prime(int(str(j)+str(i))) and is_prime(int(str(i)+str(k))) and is_prime(int(str(k)+str(i))) and is_prime(int(str(i)+str(l))) and is_prime(int(str(l)+str(i))) and is_prime(int(str(j)+str(k))) and is_prime(int(str(k)+str(j))) and is_prime(int(str(j)+str(l))) and is_prime(int(str(l)+str(j))) and is_prime(int(str(k)+str(l))) and is_prime(int(str(l)+str(k))):
        return True

primes = gen_primes(1000)

for i in primes:
    for j in primes:
        for k in primes:
            for l in primes:
                if concat_prime(i,j,k,l):
                    print(i,j,k,l)
            
