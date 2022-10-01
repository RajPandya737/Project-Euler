def is_bouncy(n):
    if n == int("".join(sorted(list(str(n))))) or n == int("".join(reversed(sorted(list(str(n)))))):
        return False
    return True

bouncy = 1
not_bouncy = 100
i = 101
while bouncy/not_bouncy <= 99:
    if is_bouncy(i):
        bouncy+=1
    else:
        not_bouncy+=1
    i+=1
print(i)

#we get 1587001 but the percent is 99.00006301197227 so we use the 
#value 1 earlier where the percent is exactly 99% and the count goes down