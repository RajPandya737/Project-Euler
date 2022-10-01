def factorial(n):
    if n == 0:
        return 1
    else:
        v = 1
        for i in range(1, n+1):
            v*=i
        return v

def factsum(n):
    nums = list(map(int, list(str(n))))
    sum = 0
    for i in nums:
        sum+=factorial(i)
    return sum

i = 3
total = 0
while i<2600000:
    if int(factsum(i)) == int(i):
        total+=i
        print(total)
    i+=1
