import math


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n<2 or n%2 == 0 or n%3 == 0:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True


def is_truncatable(n):
    nums = list(str(n))
    s = ""
    for i in nums:
        s+=str(i)
        if not is_prime(int(s)):
            return False

    s = ""
    num_reverse = reversed(nums)
    for i in num_reverse:
        s+=str(i)
        if not is_prime(int(s[::-1])):
            return False

    return True


count = 0
sum = 0
i = 10
while count <11:
    if is_prime(i):
        if is_truncatable(i):
            print(i)
            sum+=i
            count+=1
    i+=1
print(sum)
    
