import math
'''
#BRUTE FORCE DOES NOT WORK, IT IS TOO SLOW 
sum = 0
for i in range(1, 5000000900):
    sum+=i
    divisors = 0
    for j in range(1, int(sum/2)+1):
        if sum%j == 0:
            divisors+=1
    print(divisors)
    if divisors>=500:
        print(sum + "here")
        break
    '''

#Method 2: number theory
sum = 0
for i in range(1, 5000000900):
    sum+=i
    divisors = 0
    for j in range(1, int(math.sqrt(sum))):
        if sum%j == 0:
            divisors+=1
    divisors*=2
    if math.sqrt(sum).is_integer():
        divisors+=1
    print(divisors)
    if divisors>=500:
        print(sum)
        break
