nums = []
v = 1

for i in range(1, 1000000):
    nums.append(str(i))
n_temp = "".join(nums)
n = list(str(n_temp))

#v=

print(int(n[0])*int(n[9])*int(n[99])*int(n[999])*int(n[9999])*int(n[99999])*int(n[999999]))
print(v)