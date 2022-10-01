import math

a_file = open("99txt.txt", "r")

n = [(line.strip()).split() for line in a_file]

for i, v in enumerate(n):
    n[i] = list(map(int, v))
max = 0
nums = []
for i, v in enumerate(n):
    t = v[1]*math.log(v[0])
    if t>max:
        max = t
        nums.append(i+1)
print(nums[-1])
print(max)

a_file.close() 