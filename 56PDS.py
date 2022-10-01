#ready to submit

p = []
max = 0
def sum(n):
    t = 0
    nums = list(map(int, list(str(n))))
    for i in nums:
        t+=i
    return t

for i in range(1, 100):
    for j in range(1, 100):
        p.append(i**j)

for i in p:
    v = sum(i)
    if max<v:
        max = v
print(max)