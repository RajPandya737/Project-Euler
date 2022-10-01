# list of primes to the number 600851475143
n = 200000
primes = []

for i in range(2, n + 1):
    for j in range(2, int(i ** 0.5) + 1):
 		if i % j == 0:
            break
        else:
            primes.append(i)

num = 600851475143
i = 0
while num not in primes:
    if num%primes[i]==0:
        a=int(num/i)
        num = a
        i = 0
    else:
        i+=1
print(num)

