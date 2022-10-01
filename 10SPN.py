import math
sum = 0
for num in range(2,2000000):
    prime = True
    for i in range(2,int(math.sqrt(num))+1):
        if (num%i==0):
            prime = False
    if prime:
       sum+=num
print(sum)